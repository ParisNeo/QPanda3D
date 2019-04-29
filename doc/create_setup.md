# Create distribution

```bash
python setup.py sdist bdist_wheel
```

# Install it

```bash
python -m pip install --upgrade --force-reinstall dist/QPanda3D-0.2.2-py3-none-any.whl
```

# Publish it
python -m twine upload dist/*
