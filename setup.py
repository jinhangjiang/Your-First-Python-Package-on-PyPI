from setuptools import setup

setup(
    name = 'cmdlogtime', 
    version = '0.0.2',
    description = (
        'This package does command line processing, allows for logging, and '
        'keeps track of start, end, and elapsed time, along with a bunch of '
        'other stuff.'
    ),
    py_modules = ["cmdlogtime"],
    package_dir = {'':'src'},
    author = 'Ron Stewart',
    author_email = 'rstewart@morgridge.org',
    long_description = open('README.md').read() + '\n\n' + open('CHANGELOG.md').read(),
    long_description_content_type = "text/markdown",
    url='https://github.com/stewart-lab/cmdlogtime',
    include_package_data=True,
    install_requires = [],
    keywords = [],
)

# Whenever you want to update your package, you should remove the ‘build’ and
# ‘dist’ folders, make changes to your code, edit the “CHANGLOG.txt” file, and 
# revise the version number in the “setup.py”.
#
# conda activate cmdlogtime
# rm -rf build/ dist/
# python setup.py sdist bdist_wheel
# pytest (NA yet)
# twine check dist/*
# twine upload --repository-url https://test.pypi.org/legacy/ dist/* 
#   #pay attention there is an extra space before dist.
# twine upload dist/*
