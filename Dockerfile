FROM python:3
RUN apt update -y

RUN mkdir app

COPY . /app
RUN python3 --version
RUN pip3 install -r /app/requirements.txt

EXPOSE 5000
WORKDIR /app
ENTRYPOINT ["/app/docker-entrypoint.sh"]
