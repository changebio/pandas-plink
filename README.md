# pandas-plink

[![PyPI-License](https://img.shields.io/pypi/l/pandas-plink.svg?style=flat-square)](https://pypi.python.org/pypi/pandas-plink/)
[![PyPI-Version](https://img.shields.io/pypi/v/pandas-plink.svg?style=flat-square)](https://pypi.python.org/pypi/pandas-plink/) [![Anaconda-Version](https://anaconda.org/conda-forge/pandas-plink/badges/version.svg)](https://anaconda.org/conda-forge/pandas-plink) [![Anaconda-Downloads](https://anaconda.org/conda-forge/pandas-plink/badges/downloads.svg)](https://anaconda.org/conda-forge/pandas-plink) [![Documentation Status](https://readthedocs.org/projects/pandas-plink/badge/?style=flat-square&version=master)](https://pandas-plink.readthedocs.io/)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/279d016293724b79ad8e667c1440d3d0)](https://www.codacy.com/app/danilo.horta/pandas-plink?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=limix/pandas-plink&amp;utm_campaign=Badge_Grade)

PLINK reader for Python.
It reads binary PLINK files into [Pandas](http://pandas.pydata.org) data frame
and [Dask](http://dask.pydata.org/en/latest/index.html) array.
This package handles larger-than-memory data sets by reading the SNP matrix
on-demand.

## Install

The recommended way of installing it is via
[conda](http://conda.pydata.org/docs/index.html)

```bash
conda install -c conda-forge pandas-plink
```

An alternative way would be via pip

```
pip install pandas-plink
```

## Running the tests

After installation, you can test it
```
python -c "import pandas_plink; pandas_plink.test()"
```
as long as you have [pytest](http://docs.pytest.org/en/latest/).

## Usage

It is as simple as

```python
from pandas_plink import read_plink
(bim, fam, G) = read_plink('/path/to/data')
```

Refer to [documentation](http://pandas-plink.readthedocs.io/en/latest/)
for more information.

## Authors

* **Danilo Horta** - [https://github.com/Horta](https://github.com/Horta)

## License

This project is licensed under the MIT License - see the
[LICENSE](LICENSE) file for details
