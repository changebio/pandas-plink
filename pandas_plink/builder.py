from cffi import FFI

ffibuilder = FFI()

ffibuilder.cdef(r"""
    int read_bed_chunk(char*, uint64_t, uint64_t,
                       uint64_t, uint64_t,
                       uint64_t, uint64_t,
                       uint64_t*, uint64_t*);
""")

ffibuilder.set_source("pandas_plink._bed_reader", r"""
    #include <stdio.h>
    #include <math.h>
    #include <assert.h>

    #define MIN( a, b ) ( ( a > b) ? b : a )

    static int read_bed_chunk(char *filepath, uint64_t nrows, uint64_t ncols,
                              uint64_t row_start, uint64_t col_start,
                              uint64_t row_end, uint64_t col_end,
                              uint64_t *out, uint64_t *strides)
    {
            assert(sizeof(uint64_t) == 4);
            assert(sizeof(char) == 1);
            assert(col_start % 4 == 0);

            // in bytes
            uint64_t row_chunk = (col_end - col_start + 3) / 4;
            // in bytes
            uint64_t row_size = (ncols + 3) / 4;

            FILE* f = fopen(filepath, "rb");
            if (f == NULL)
            {
                    fprintf(stderr, "Couldn't open %s.\n", filepath);
                    return -1;
            }

            char* buff = malloc(row_chunk * sizeof(char));
            if (buff == NULL)
            {
                    fprintf(stderr, "Not enough memory.\n");
                    return -1;
            }

            char b, b0, b1, p0, p1;
            uint64_t r = row_start;
            uint64_t c, ce;
            size_t e;

            while (r < row_end)
            {
                    fseek(f, 3 + r * row_size + col_start / 4, SEEK_SET);
                    e = fread(buff, row_chunk, 1, f);

                    if (e != 1)
                    {
                            if (feof(f))
                            {
                                    fprintf(stderr, "Error reading %s: unexpected end of file.\n", filepath);
                                    return -1;
                            }
                            e = ferror(f);
                            if (e)
                            {
                                    fprintf(stderr, "File error: %zu.\n", e);
                                    return -1;
                            }
                    }


                    for (c = col_start; c < col_end; )
                    {
                            b = buff[(c - col_start)/4];

                            b0 = b & 0x55;
                            b1 = (b & 0xAA) >> 1;

                            p0 = b0 ^ b1;
                            p1 = (b0 | b1) & b0;
                            p1 <<= 1;
                            p0 |= p1;
                            ce = MIN(c + 4, col_end);
                            for (; c < ce; ++c)
                            {
                                    out[(r - row_start) * strides[0] + (c - col_start) * strides[1]] = p0 & 3;
                                    p0 >>= 2;
                            }
                    }
                    ++r;
            }

            free(buff);
            fclose(f);
            return 0;
    }
""")

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)