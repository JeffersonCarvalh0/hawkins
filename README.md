# hawkins
Simple software for managing student's grades. It uses Django, but is made to
run locally from your computer, as any other GUI application.

# Getting Started
Installing dependencies after cloning the repository:

```
pip install -r requirements.txt
```

## Django's secret key
This project has the **DJANGO_KEY** variable hidden.

You can generate your DJANGO_KEY http://www.miniwebtool.com/django-secret-key-generator

To include it in your project, create a file named *secret_key.txt* inside the
*hawkins* folder with the generated key inside it, in the first line of the file.

The  application starts by running the *run.py* file.

# Built With
* [Django](https://www.djangoproject.com/) - Web framework
* [SQLite3](https://www.sqlite.org/) - DBMS
* [CEF Python](https://github.com/cztomczak/cefpython) - Desktop GUI
* [Materialize](http://materializecss.com/) - Front-end framework
* [django-cleanup](https://github.com/un1t/django-cleanup) - Automatically deletes model files

# License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.
