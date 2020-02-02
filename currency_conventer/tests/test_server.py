import pytest
from unittest.mock import patch
from settings import (BASE_CURRENCY, STATUS_400_BAD_REQUEST,
                      STATUS_200_OK)


mocked_data = [{'rates': [{'currency': 'bat (Tajlandia)', 'code': 'THB', 'mid': 0.1251},
               {'currency': 'dolar amerykański', 'code': 'USD', 'mid': 3.8999}]}]


@patch('requests.get')
def test_success_api(mock, client):
    mock.return_value.json.return_value = mocked_data
    response = client.post('/convert', data='{"currency1": "THB", "currency2": "USD", "amount": 100}',
                           headers={'Content-Type': 'application/json'})
    returned_data = b'{"currency1": "THB", "currency2": "USD", "amount": 100, "value2": 3.207774558322008}'
    assert response.data == returned_data
    assert response.status_code == STATUS_200_OK


@patch('requests.get')
def test_failed_code(mock, client):
    mock.return_value.json.return_value = mocked_data
    response = client.post('/convert', data='{"currency1": "TH", "currency2": "USD", "amount": 100}',
                           headers={'Content-Type': 'application/json'})
    assert response.data == b'"Wrong code value"'
    assert response.status_code == STATUS_400_BAD_REQUEST


@patch('requests.get')
def test_key_error(mock, client):
    mock.return_value.json.return_value = mocked_data
    response = client.post('/convert', data='{"currecy1": "TH", "currency2": "USD", "amount": 100}',
                           headers={'Content-Type': 'application/json'})
    assert response.data == b'"You need to pass keys: \\"currency1\\", \\"currency2\\", \\"amount\\""'
    assert response.status_code == STATUS_400_BAD_REQUEST


@patch('requests.get')
def test_base_currency_api(mock, client):
    mock.return_value.json.return_value = mocked_data
    response = client.post('/convert', data='{"currency1": "PLN", "currency2": "PLN", "amount": 100}',
                           headers={'Content-Type': 'application/json'})
    assert response.data == b'{"currency1": "PLN", "currency2": "PLN", "amount": 100, "value2": 100}'
    assert response.status_code == STATUS_200_OK

