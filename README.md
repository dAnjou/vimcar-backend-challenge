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

Furthermore, architecture-wise, I'd split authentication/authorization and
resources into separate applications to have one system in charge of all auth
for all other services behind it.

### Choice of libraries

I'm very opinionated when it comes to dependencies. I try to avoid adding too
many dependencies. I always evaluate multiple aspects of a dependency like how
well it is maintained, how popular it is, how many dependencies it comes with
itself, that it has proper releases, and whether it is easy and/or flexible
enough to be replaced.

*Flask* and *Flask-SQLAlchemy* are well maintained and even written by the same
author.

*Flask-JWT* on the other hand was a convenience choice for this very project and
in this very context of a coding challenge. It's not as well maintained and
while it's pretty flexible for what it does it has one or two quirks. But the
biggest issue I have with it is that it doesn't really take advantage of JWT's
authorization capabilities. JWT's claims are perfect for a permission system,
yet Flask-JWT basically only allows giving full access to everyone or no access
at all.

On a more meta level I'd like to say that I could have chosen any REST framework
that sits on top of Flask or at least something like *Flask-Security* and be
done with the whole thing but I explicitly didn't do this because as far as I
understood I was supposed to show that I understand certain concepts and I feel
like using such frameworks or bundle libraries wouldn't let me do this.
