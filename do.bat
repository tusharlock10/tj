cd "D:\Python Programs\Python Projects\TJ Module"
D:
python setup.py bdist_wheel
python setup.py sdist
twine upload dist/*
pip install tj -U
pip install tj -U
rmdir /s /q __pycache__
rmdir /s /q dist
rmdir /s /q tj.egg-info
rmdir /s /q build