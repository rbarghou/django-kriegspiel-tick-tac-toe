# django-kriegspiel-tick-tac-toe

[![Build Status](https://travis-ci.org/rbarghou/django-kriegspiel-tick-tac-toe.svg?branch=master)](https://travis-ci.org/rbarghou/django-kriegspiel-tick-tac-toe)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

A django implementation of Kriegspiel Tic-Tac-Toe https://www.smbc-comics.com/comic/tic. Check out the project's [documentation](http://rbarghou.github.io/django-kriegspiel-tick-tac-toe/).

# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)

# Initialize the project

Start the dev server for local development:

```bash
docker-compose up
```

Create a superuser to login to the admin:

```bash
docker-compose run --rm web ./manage.py createsuperuser
```
