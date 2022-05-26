# Your First Python Package on PyPI

## [![Typing SVG](https://readme-typing-svg.herokuapp.com?multiline=true&width=1200&lines=An+end+to+end+project+helps+you+publish+your+first+python+package+in+a+simple+way.++++++++++)](https://git.io/typing-svg)

*Note: everything in this demo is conducted in Windows OS.

## Step 1

Go to the following two websites to register your own account, respectively.
- PyPI test: https://test.pypi.org/
- PyPI: https://pypi.org/

Note: Let's always try your package on the test site first to avoid mistakes in uploading process. Since any change you make to your package on pypi is not revertable, uploading errors may lead to a malfunctional patch for your package. You want to avoid that!!


## Step 2

Fork this repository to your own GitHub account and make it available in your local. You can make the most changes on GitHub, but you will need to publish your package via cmd with those files available in local.

And here is the list of the core files you will need:

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

## Step 3

Install the following pathon package in your cmd:

```css
pip install setuptools
pip install twine
pip install wheel
pip install pytest # optional
```

You will need them later.

## Step 4

Do the following changes in ANY order you want:

1. Replace your_main_code.py in src folder with your own python package and leave __init__.py as it is
2. Make changes to setup.py, instructions included in that file.
3. Pick your own license. 
  * Open the LICENSE file, click on Edit, click "Choose a license template", and select the license fullfills your needs.
  * If you have no idea which license works for you, you can use the MIT license, which is one of the most common choices.
  * Or, you can use this link to pick one: https://choosealicense.com/
4. Update CHANGELOG.md to reflect version information
5. Optional: create a test.py and put the file in the tests folder. Or you can remove the whole folder if you are confident that everything works great in your module.
6. Delete everything in this README.md file, and update the file with the long decription of your package.

## Step 5

You have multiple choices for step 5 to perform the the rest of steps. Here are two examples:

1. Do it in *[cmd]: Command Prompt
- In your local, open the cmd and navigate to the directory where your package is typing the following:
```css
# First, change root disk
C:\User\Yourname> d:

# Second, navigate to the folder
D:\> cd D:\my_works\Your-First-Python-Package-on-PyPI
```

2. Do it in Jupyter Notebook terminal:
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

Under the dist folder, you will see a 'tar' file called "TheNameofYourPackage-TheVersionofYourPackage.tar.gz". At this point of time, if you do not need to publish your code in public, instead, you just want to share your code with your friends or colleagues, you may just share this file with them. All they need to do is to do "pip install" to use your code:
```css
pip install relative_path_to_yourpackage.tar.gz  
```

## Step 7 (Optional)

Now, you are about publishing your package to PyPI. Before you make it public, one more thing you may want to do is to test if your package will work as expected once people download them. What you can do is to create folder called "test", and create a test.py, which include some sample implementations of your package. Then, type "pytest" in your cmd/terminal. If everything works fine, it will run your test.py automatically and pass. Otherwise, it will raise errors and you should fix the bugs accordingly before you move to next step.

And here is one more thing you might want to try to test if the architecture of your package is good to go. In the cmd/terminal, type the following code:
```css
twine check dist/*
```
You should see something like this:
```
Checking distribution dist/TheNameofYourPackage-TheVersionofYourPackage-1.0.0-py3-none-any.whl: Passed
Checking distribution dist/TheNameofYourPackage-TheVersionofYourPackage.tar.gz: Passed
```

## Step 8

Upload your package to TestPyPI:
```css
twine upload --repository-url https://test.pypi.org/legacy/ dist/* #pay attention there is an extra space before dist.
```
Then you will see a link leading to the testing version of your package on TestPyPI. Check it out! If there is any typo or incompatible bugs, fix them before you upload it to the real PyPI.

And, now, it is the most exciting moment, upload your package to PyPI to help hundreds of thousands of people in our community:
```css
twine upload dist/*
```
By this point, your package should be officially online and can be "pip install" by anyone at anytime from anywhere. Big moment! I still remember how I felt at the moment when I saw my first package is out there. I told myself, that's why I code! CONGRATULATIONS!!!  


## A few tips

- Whenever you want to update your package, you should remove the 'build' and 'dist' folders, make change to your code, and repeat steps 5-8.
- Do not publish packages arbitrarily. Even though there are no hard restrictions on what you can or cannot publish, make sure you are uploading something that is actually meaningful and someone will benefit from your work. 
