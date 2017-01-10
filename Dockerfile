FROM python:3

RUN python3 -m venv /venv && \
    /venv/bin/pip install --no-cache-dir uwsgi==2.0.14
COPY ./requirements.txt /tmp
RUN /venv/bin/pip install --no-cache-dir -r /tmp/requirements.txt

RUN mkdir /vc
COPY ./vc /vc

EXPOSE 5000

#TODO: use configuration file!
CMD ["/venv/bin/uwsgi", "--http-socket", ":5000", "--manage-script-name", "--mount", "/=vc.main:app"]
