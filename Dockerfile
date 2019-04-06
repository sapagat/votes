FROM python:3.6.6

ENV PYTHONPATH /opt/app/
WORKDIR $PYTHONPATH

RUN pip install pipenv

COPY Pipfile* $PYTHONPATH
RUN pipenv install

COPY . .
