# Virtual Environment

# What is Virtual Environment?

A virtual environment is a tool that helps to keep dependencies required by different projects separate by creating isolated python virtual environments for them. This is one of the most important tools that most of the Python developers use.

## Why do we need a virtual Environment?

 - Python applications will often use packages and modules that don’t come as part of the standard library.
 - This means it may not be possible for one Python installation to meet the requirements of every application.
 - __for Example:__
     - A needs version 1.0 of a particular module but application B needs version 2.0, then the requirements are in conflict and installing either version 1.0 or 2.0 will leave one application unable to run.
 - __What's Solution Then:__
     - The solution for this problem is to create a virtual environment, a self-contained directory tree that contains a Python installation for a particular version of Python, plus a number of additional packages.
     
 - Different applications can then use different virtual environments. To resolve the earlier example of conflicting requirements, application A can have its own virtual environment with version 1.0 installed while application B has another virtual environment with version 2.0. If application B requires a library be upgraded to version 3.0, this will not affect application A’s environment.
 
 - __Virtual Environment should be used whenever you work on any Python based project. It is generally good to have one new virtual environment for every Python based project you work on. So the dependencies of every project are isolated from the system and each other.__

#### keep the project files outside the virtual environment.

# Creating Virtual Environments

- To create a virtual environment first we have to install package called __virtualenv__.
   - To install __virtualenv__ open terminal and type __pip install virtualenv__
   - you can test your virtual environment installation __virtualenv --version__
- Now after installing __virtualenv__ we are ready to create our first virtual environment.
- To __create__ virtual environment type __virtualenv demo_env__ (Note: you can chooose any name for your virtual environment. Here is choose __demo_env__)
    - If you want to specify Python interpreter of your choice, for example Python 3, it can be done using the following command:
        - __virtualenv -p /usr/bin/python3 virtualenv_name__
    - To create a Python 2.7 virtual environment, use the following command:
        - __virtualenv -p /usr/bin/python2.7 virtualenv_name__

- After creating virtual environment you have to __activate__ it.
- To __activate__ virtual environment type __source demo_env/bin/activate__
- Now __demo_env__ is activated successfully.
- To __deactivate__ the virtual environment type __deactivate__

# Managing packages in Virtual Environment with pip

- After activated virtual environment successfully you can manage packages with pip.
- __what is pip?__
    - __pip__ is a package management system used to install and manage software packages, such as those found in the Python Package Index(PyPI). pip is included by default in python version 3.4 or later.
    
    
- Type __pip list__ and you see that there is only few packages are installed.
- Now install packages that will require in your project.
- You can install python packages using __pip install__ command.
    - For example: __pip install sqlite3__
    - This will install the latest version on __sqlite3__.
- Now suppose you have to install specific version of package for your virtual environment then you have to provide version number too.
    - For example: __pip install numpy==1.9.1__
    - This will install the __numpy__ package of having __1.9.1__ version. 
- Command __pip install --upgrade numpy__ will upgrade the __numpy__ to the latest version.
- To uninstall package you have to write __pip uninstall numpy__. This command will remove __numpy__ package from your current activated environment.

- know more about __pip__ here:
    - Python Doc: __https://docs.python.org/3/tutorial/venv.html#managing-packages-with-pip__
    - Real Python: __https://realpython.com/what-is-pip/__

# Delete Virtual Environment


- To remove any virtual environment use __rm -rf demo_env/__ command.

# Alternatives to pip

- pip is an essential tool for all Pythonistas, and it is used by many applications and projects for package management. But the Python community is very active in providing great tools and libraries for other developers to use. These include other alternatives to pip that try to simplify and improve package management.


- __Other package management tools available for Python.__
    - __Conda__
     - Conda is a package, dependency, and environment manager for many languages including Python.Conda is widely used for data science and machine learning applications, and uses its own index to host compatible packages.
    - __Pipenv__
     - Pipenv is another package management tool. It’s gaining a lot of traction among the Python community because it merges virtual environment and package management in a single tool.
     - It also solves some of the most common hiccups you will run into when manually managing dependencies through pip, like versions of packages, separating development and production dependencies, and locking versions for production.
    - __Poetry__
     - Poetry is another pip alternative that is gaining a lot of traction. Like Pipenv, it simplifies package version management and separates development vs production dependencies, and it works by isolating those dependencies into a virtual environment.

# What is PyPI?

- The __Python Package Index (PyPI)__ is a repository of software for the Python programming language.
- PyPI helps to find and install software developed and shared by the Python community. 
- Official website of  PyPI: __https://pypi.org/__ 
