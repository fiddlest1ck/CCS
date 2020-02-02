from flask import Flask, Response, request
import settings
import json

server = Flask(__name__)

if __name__ == "__main__":
    server.run(host=settings.HOST, port=settings.PORT)