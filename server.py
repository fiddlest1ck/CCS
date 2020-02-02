from flask import Flask, Response, request
from currency_conventer.utils import Conventer, schema_validator
import settings
import json

server = Flask(__name__)


@server.route('/convert', methods=['POST'])
def convert():
    data = request.get_json()
    if schema_validator(data):
        from_currency = data['currency1']
        to_currency = data['currency2']
        amount = data['amount']
        converter = Conventer(amount, from_currency, to_currency)
        if converter.validate():
            return Response(converter.convert())
        else:
            return Response(json.dumps("Wrong code value"), status=settings.STATUS_400_BAD_REQUEST)
    else:
        return Response(json.dumps('You need to pass keys: "currency1", "currency2", "amount"'),
                        status=settings.STATUS_400_BAD_REQUEST)

if __name__ == "__main__":
    server.run(host=settings.HOST, port=settings.PORT)