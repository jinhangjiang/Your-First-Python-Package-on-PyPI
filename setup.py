from setuptools import setup

######################################################################################################
################ You May Remove All the Comments Once You Finish Modifying the Script ################
######################################################################################################

setup(
    name = 'cmdlogtime', 
    version = '0.1.0',
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
