# Contributing

All contributors are welcome! This project needs help from many types of contributors, including people interested in code, design, community building, testing, and documentation. Please feel free to bring any ideas or suggestions forward in order to improve this project.

## Development

This section describes the steps necessary to set up an environment to run this project on your local computer. For example, you may want to try out the software to get ideas or even add some features.

### Prerequisites

You will need to make sure your computer has [Python 3 installed](https://www.python.org/downloads/). If you would like to checkout the code from GitHub, you will also need to [install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

### Get the code
There are two main ways to get the code for this project:

a) [download it from GitHub](https://github.com/brylie/wagtail-social-network/archive/refs/heads/develop.zip)
b) clone it using Git

For the Git instructions, 

1) go to the project on GitHub
2) copy the clone link under the "code" button
3) clone the repository into a local folder

E.g.
Using SSH:
```sh
git clone git@github.com:brylie/wagtail-social-network.git
```
Using HTTPS:
```sh
git clone https://github.com/brylie/wagtail-social-network.git
```

### Create a virtual environment

When developing or running Python code, you should try to make sure you are working in a virtual environment. The virtual environment will keep your computer in good order, particularly when managing multiple Python projects.

Run the following command, from within the code directory you cloned above, to set up a virtual environment on Linux/Mac

```sh
python -m venv env
```

That will create a new virtual environment in the `env` subdirectory wherever you ran the command.


### Activate the virtual environment

Once you have created a virtual environment, you need to activate it with the following command on Linux/Mac:

```sh
source env/bin/activate
```

### Install dependencies

Once you are inside of the virtual environment, you can make sure you have the latest dependencies installed by running the following command on Linux/Mac:

```sh
pip install project/requirements.txt
```

Note: the above example assumes you are running the `pip install` command from within the root directory of this repository, whereas the `requirements.txt` file is in the `project/` subdirectory.

### Run the project

Once you have installed the dependencies, you can run the project. However, first make sure you have run all database migrations and created a superuser.

```sh
python manage.py migrate
```

```sh
python manage.py createsuperuser
```

```sh
python manage.py runserver
```

From there, you should be able to access the project at [localhost:8000](http://localhost:8000)

### Using the DJANGO_SETTINGS_MODULE

We currently have some development settings contained in `core.settings.dev`. However, those settings are not used when running `python manage.py runserver`

You can use it by changing the `manage.py` file in `project` directory and `wsgi.py` in `project/core` directory.

All you have to do is change 

```py
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.dev")
```

To the setting you want to use, i.e:
```py
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.base")
```

or
```py
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.production")
```