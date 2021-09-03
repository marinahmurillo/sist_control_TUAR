## Creating a Python virtual environment to run the provided examples
(Tested with Ubuntu 20.04)

This repository provides a `virtualenv_requirements.txt` file to facilitate the installation of the required dependencies.

First, install `virtualenv` with `pip3` in order to configure an isolated Python environment to run the coding examples. 

`pip3 install virtualenv`

Next, you need to create a directory to contain your virtual environments and then create one for this project:

`~$ mkdir virtualenvs`

`~$ cd virtualenvs`

`~/virtualenvs$ virtualenv sist_control_tuar`

Now, the virtual environment needs to be activated:

`~/virtualenvs$ source sist_control_tuar/bin/activate`

The name of the current virtual environment will now appear on the left of the prompt to let you know that it’s active. From now on, any package that you install using pip will be placed in the sist_control_tuar folder, isolated from the global Python installation.

We need to make sure that the pip version contained in the virtual environment is up to date:

`$ pip3 install -U pip`

Now download the file `virtualenv_requirements.txt` and the `.py` scripts and place them in the current folder. Then, we can install the required dependencies

`~/virtualenvs$ pip3 install -r virtualenv_requirements.txt`

and test the provided code. For example, to test the script `example.py`, you can run

`$ python3 example.py`

Once you are done working in the virtual environment for the moment, you can deactivate it:

`$ deactivate`

Now running `python` will just use the system’s default Python interpreter, which is not modified by anything done while being inside the virtual environment.

To delete a virtual environment, just delete the corresponding folder. (In this case, it would be `rm -r sist_control_tuar`).

