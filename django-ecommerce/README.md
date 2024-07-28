# Django Project Setup

This README provides the steps to set up a Django project, including the installation of necessary packages and running the development server.

## Prerequisites


- Create a virtual environment inside the folder:

```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

- Ensure you have Python and pip installed on your system. You can install running:

```bash
pip install asgiref django pillow setuptools sqlparse
```

- Go to the main folder and run the application:

```bash
cd django-ecommerce
```

- Run the application
```bash
python manage.py runserver
```

- Go to the local URL to se and navigate on the page:

```bash
http://127.0.0.1:8000/
```