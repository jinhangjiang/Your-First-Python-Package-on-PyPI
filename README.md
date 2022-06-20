# Your First Python Package on PyPI

Reference Blog: https://towardsdatascience.com/an-end-to-end-guide-to-publish-your-python-package-bdb56639662c

## [![Typing SVG](https://readme-typing-svg.herokuapp.com?multiline=true&width=1200&lines=An+end+to+end+project+helps+you+publish+your+first+python+package+in+a+simple+way.++++++++++)](https://git.io/typing-svg)

## Step 1

Go to the following two websites to register your own account, respectively.
- PyPI test: https://test.pypi.org/
- PyPI: https://pypi.org/

Note: I highly recommend trying your package on the test site first to avoid mistakes in the uploading process. Since any change, you make to your package on PyPI is not revertable, uploading errors may lead to a malfunctioning patch for your package. You want to avoid that!!


## Step 2

Fork this repository to your own GitHub account and make it available in your local. You can make the most changes on GitHub, but you will need to publish your package via cmd with those files available in local.

And here is the list of the core files you will need:

* src
  * \_\_init\_\_.py
  * your_main_code.py  (This is only one module, if you have multi-modules included in this package, you probably want to create subfolders for them. For details, check the OPTIONAL part following this section.)
* setup.py
* README.md
* MANIFEST.in
* LICENSE
* pyproject.toml
* CHANGELOG.md

I know that's a lot. But bear with me. You only need to make necessary changes to some of them, and the rest will stay as default.

## OPTIONAL - Multiple Modules
Suppose you have multiple classes with functions created in separate files. You want to make the folders (or subfolders) following this convention:

* Lib1
  * \_\_init\_\_.py
  * \_Class1.py
  * \_Class2.py

* Lib2
  * ...
  * ...

Inside each folder, update the "\_\_init\_\_.py" by doing this:

    from ._Class1 import Function1
    from ._Class1 import Function2
    from ._Class2 import Function1
    ... 

In the main folder, update the "\_\_init\_\_.py" by doing this:

    from Lib1._Class1 import Function1
    from Lib1._Class1 import Function2
    from Lib1._Class2 import Function1
    ... 

Then the users will be able to import your library properly like this:

    from YourPackage.Class1 import Function1
    
If You want to import something from the main (previous) folder, here is what you should do:

    from .._ClassFromThePreviousFolder import Function1
    
Consider adding a list in your "\_\_init\_\_.py", so that the users can check what functions are available:

    __all__ = [ 'Function1',
                'Function2',
                ...,
                'FunctionN'
    ]
    

## Step 3

Install the following python package in your cmd:

```css
pip install setuptools
pip install twine
pip install wheel
pip install pytest # optional
```

You will need them later.

## Step 4

Do the following changes in ANY order you want:

1. Replace your_main_code.py in src folder with your own python package and leave "\_\_init\_\_.py" as it is.
2. Make changes to setup.py, and instructions included in that file.
3. Pick your own license. 
  * Open the LICENSE file, click on Edit, click "Choose a license template", and select the license fullfills your needs.
  * If you have no idea which license works for you, you can use the MIT license, which is one of the most common choices.
  * Or, you can use this link to pick one: https://choosealicense.com/
4. Update CHANGELOG.md to reflect version information
5. Optional: create a "test.py" and put the file in the tests folder. Or you can remove the whole folder if you are confident that everything works great in your module.
6. Delete everything in this "README.md" file, and update the file with the long decription of your package.

## Step 5

You have multiple choices for step 5 to perform the rest of the steps. Here are two examples:

1. Do it in cmd - Command Prompt
- In your local, open the cmd, navigate to the directory where your package is and type the following:
```css
# First, change root disk
C:\User\Yourname> d:

# Second, navigate to the folder
D:\> cd D:\my_works\Your-First-Python-Package-on-PyPI
```

2. Do it in the Jupyter Notebook terminal:
```css
C:\User\Yourname> jupyter notebook --notebook-dir D:/my_works/Your-First-Python-Package-on-PyPI
```

## Step 6

In this step, we will use the following code in cmd/terminal to build your package:
```css
python setup.py sdist bdist_wheel
```

Once you run the code, you will see the following two folders in the current directory:
- build
- dist

Under the dist folder, you will see a 'tar' file called "TheNameofYourPackage-TheVersionofYourPackage.tar.gz". At this point of time, if you do not need to publish your code in public; instead, if you just want to share your code with your friends or colleagues, you may just share this file with them. All they need to do is to do "pip install" to use your code:
```css
pip install relative_path_to_yourpackage.tar.gz  
```

## OPTIONAL - Test Your Package on PyPI

Now, you are about to publish your package to PyPI. Before you make it public, one more thing you may want to do is to test if your package will work as expected once people download them. What you can do is to create a folder called "test", and create a test.py, which includes some sample implementations of your package. Then, type "pytest" in your cmd/terminal. If everything works fine, it will run your test.py automatically and pass. Otherwise, it will raise errors and you should fix the bugs accordingly before moving to the next step.

And here is one more thing you might want to try to test if the architecture of your package is good to go. In the cmd/terminal, type the following code:
```css
twine check dist/*
```
You should see something like this:
```
Checking distribution dist/TheNameofYourPackage-TheVersionofYourPackage-1.0.0-py3-none-any.whl: Passed
Checking distribution dist/TheNameofYourPackage-TheVersionofYourPackage.tar.gz: Passed
```

## Step 7

Upload your package to TestPyPI:
```css
twine upload --repository-url https://test.pypi.org/legacy/ dist/* #pay attention there is an extra space before dist.
```
Then you will see a link leading to the testing version of your package on TestPyPI. Check it out! If there are any typos or incompatible bugs, fix them before uploading your package to the real PyPI.

And, now, it is the most exciting moment, upload your package to PyPI to help hundreds of thousands of people in our community:
```css
twine upload dist/*
```
By this point, your package should be officially online and can be "pip install" by anyone at any time from anywhere. Big moment! I still remember how I felt at the moment when I saw my first package is out there. I told myself, that's why I code! CONGRATULATIONS!!!  


## A few tips

- Whenever you want to update your package, you should remove the 'build' and 'dist' folders, make changes to your code, edit the "CHANGLOG.txt" file, and revise the version number in the "setup.py". And repeat steps 5–7.
- You may upgrade your package after the updates by doing this: ___pip install YOURPACKAGENAME --upgrade___
- You can always find your package on PyPi here: ___ht<span>tp://</span>pypi.org/project/YOURPACKAGENAME/___
- Do not publish packages arbitrarily. Even though there are no hard restrictions on what you can or cannot publish, make sure you are uploading something that is actually meaningful and someone will benefit from your work. 
