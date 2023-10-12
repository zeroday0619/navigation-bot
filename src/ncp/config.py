import os

def NCPMapsDirectionsKeyID() -> str:
    """Returns the NCPMaps API key ID"""
    _id = os.environ.get('NCPMapsDirections_API_KEY_ID')
    if _id is None:
        raise ValueError('NCPMapsDirections_API_KEY_ID environment variable not set')
    return _id

def NCPMapsDirectionsKey() -> str:
    """Returns the NCPMaps API key"""
    _key = os.environ.get('NCPMapsDirections_API_KEY')
    if _key is None:
        raise ValueError('NCPMapsDirections_API_KEY environment variable not set')
    return _key


def NCPMapsGeocodingKeyID() -> str:
    """Returns the NCPMaps API key ID"""
    _id = os.environ.get('NCPMapsGeocoding_API_KEY_ID')
    if _id is None:
        raise ValueError('NCPMapsGeocoding_API_KEY_ID environment variable not set')
    return _id

def NCPMapsGeocodingKey() -> str:
    """Returns the NCPMaps API key"""
    _key = os.environ.get('NCPMapsGeocoding_API_KEY')
    if _key is None:
        raise ValueError('NCPMapsGeocoding_API_KEY environment variable not set')
    return _key

__all__ = [
    'NCPMapsDirectionsKeyID',
    'NCPMapsDirectionsKey',
    'NCPMapsGeocodingKeyID',
    'NCPMapsGeocodingKey',
]