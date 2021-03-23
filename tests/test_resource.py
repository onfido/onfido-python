from onfido.resource import Resource
import pytest


def test_resource_headers():
    r = Resource(api_token='test', region=None, timeout=None)
    
    assert r._headers['Authorization'] == 'Token token=test'
    assert r._headers['User-Agent'].startswith('onfido-python/')
