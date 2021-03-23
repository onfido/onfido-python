from onfido.resource import Resource
from onfido.regions import Region
import pytest


def test_resource_headers():
    r = Resource(api_token='test', region=Region.EU, timeout=None)
    
    assert r._headers['Authorization'] == 'Token token=test'
    assert r._headers['User-Agent'].startswith('onfido-python/')
