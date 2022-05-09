FROM python:3.10.4

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/support

COPY Pipfile Pipfile.lock /usr/src/support/
RUN pip install pipenv
RUN pipenv install --system

COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY . /usr/src/support

EXPOSE 8000