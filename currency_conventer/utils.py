import json
import requests
import settings

from cerberus import Validator


class Conventer:
    def __init__(self, amount, from_currency, to_currency):
        json_data = requests.get(settings.API_URL).json()
        self.response = json_data[0]
        self.from_currency = from_currency
        self.to_currency = to_currency
        self.amount = amount
        self.values = []
        self.collect_mid_values(self.from_currency, self.to_currency)

    def convert(self):
        self.initial_amount = self.amount
        if self.to_currency != settings.BASE_CURRENCY:
            self.amount = self.amount / self.to_currency_value
        if self.from_currency == settings.BASE_CURRENCY:
            return self.create_response(self.amount)
        else:
            return self.create_response(self.amount * self.from_currency_value)

    def collect_mid_values(self, from_currency, to_currency):
        if to_currency == settings.BASE_CURRENCY:
            self.values.append(1)
        if from_currency == settings.BASE_CURRENCY:
            self.values.append(1)
        for data in self.response['rates']:
            if data['code'] == from_currency:
                self.from_currency_value = data['mid']
                self.values.append(data['mid'])
            if data['code'] == to_currency:
                self.to_currency_value = data['mid']
                self.values.append(data['mid'])

    def validate(self):
        return len(self.values) == 2

    def create_response(self, value):
        return json.dumps({'currency1': self.from_currency,
                           'currency2': self.to_currency,
                           'amount': self.initial_amount,
                           'value2': value})


def schema_validator(data):
    schema = {'currency1': {'type': 'string'}, 'currency2':
              {'type': 'string'}, 'amount': {'type': 'float'}}
    validator = Validator(schema)
    return validator(data)
