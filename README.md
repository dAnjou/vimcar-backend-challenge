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

## Notes

### State of the project

So far the project is still in a very rough state. There pretty much only *happy
path* code which means no error handling is done at all. There are tests missing
as well. The project is also not quite ready for production deployment yet. For
persistence SQLite is used which is not the best choice in the long run. The
Docker setup can be improved to make it run the tests as well (especially useful
in a CI system)
