cd D:\Python Projects\TJ Module
d:
python setup.py bdist_wheel
python setup.py sdist
twine upload dist/*
pip install --upgrade tj
pip install --upgrade tj
rmdir /S __pycache__
rmdir /S build
rmdir /S dist
rmdir /S tj.egg-info