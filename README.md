# Vimcar Coding Challenge: Backend

This project attempts to satisfy the
[Vimcar Coding Challenge: Backend][vimcar-challenge].

It is a [Flask][flask] project using Python 3.5, [SQLAlchemy][sqlalchemy] as ORM
(via [Flask-SQLAlchemy][flask-sqlalchemy]), and [JWT][jwt] for authorization
(via [Flask-JWT][flask-jwt]). [Docker][docker] and [uwsgi][uwsgi] are used for
production deployment.

[vimcar-challenge]: https://github.com/vimcar/backend-challenge
[flask]: http://flask.pocoo.org/
[sqlalchemy]: http://www.sqlalchemy.org/
[flask-sqlalchemy]: http://flask-sqlalchemy.pocoo.org/
[jwt]: https://jwt.io/
[flask-jwt]: https://pythonhosted.org/Flask-JWT/
[docker]: https://www.docker.com/
[uwsgi]: https://uwsgi-docs.readthedocs.io/

## Setup and usage

Please refer to the *Makefile*, it contains commands to setup a development
environment as well as commands for a minimal Docker setup.

### Quickstart

```
make dev_init
make dev_recreatedb
make dev_server
```
or
```
make docker_run
```
