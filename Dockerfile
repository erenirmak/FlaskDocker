# syntax=docker/dockerfile:1

FROM python:3.11.7-slim-bullseye

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD [ "python", "-m", "FlaskDocker" ]