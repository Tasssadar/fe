FROM python:3.10-bullseye

ADD . .

RUN python3 setup.py install

CMD sleep 10 && python3 -m unittest postgresql/test_connect.py
