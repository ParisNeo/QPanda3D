# Project generation tutorial

## Create distribution

```bash
python setup.py sdist bdist_wheel
```

## Install it

```bash
python -m pip install --upgrade --force-reinstall dist/QPanda3D-*.*.*-py3-none-any.whl
```

or 

```bash
python -m pip install --upgrade -e .
```

replace * with the version you are using

## Publish it

python -m twine upload dist/*

## Update README.md

Do all updates in misc/unprocessed_README.md, then preprocess it using [pp](https://github.com/CDSoft/pp) :

```bash
pp misc/unprocessed_README.md > README.md
```

In windows, you may need to do it this way

```bash
.\pp.exe misc/unprocessed_README.md > README.md
```