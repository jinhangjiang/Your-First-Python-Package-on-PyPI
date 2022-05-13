# Your First Python Package on PyPI

## [![Typing SVG](https://readme-typing-svg.herokuapp.com?multiline=true&width=1200&lines=An+end+to+end+project+helps+you+publish+your+first+python+package+in+a+simple+way.++++++++++)](https://git.io/typing-svg)

## Step 1

Go to the following two websites to register, respectively.
- PyPI test: https://test.pypi.org/
- PyPI: https://pypi.org/

Note: Let's always try your package on the test site first to avoid mistakes in uploading process. Since any change you make to your package on pypi is not revertable, uploading errors may lead to a malfunctional patch for your package. You want to avoid that!!


## Step 2

Fork this repository to your own github account.

And here is the list of core files you will need:

* src
  * __init__.py
  * your_main_code.py  (This is only one module, if you have multi-modules included in this package, you probably want to create subfolders for them)
* setup.py
* README.md
* MANIFEST.in
* LICENSE
* pyproject.toml
* CHANGELOG.md

I know that's a lot. But bear with me. You only need to make necessary changes to some of them and the rest will be stay as default.

