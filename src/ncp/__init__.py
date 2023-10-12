from src.ncp.config import NCPMapsDirectionsKeyID
from src.ncp.config import NCPMapsDirectionsKey
from src.ncp.config import NCPMapsGeocodingKeyID
from src.ncp.config import NCPMapsGeocodingKey


class SearchOptions(object):
    @staticmethod
    def trafast() -> str:
        """실시간 빠른길"""
        return "trafast"
    @staticmethod
    def tracomfort() -> str:
        """실시간 편한길"""
        return "tracomfort"
    @staticmethod
    def traoptimal() -> str:
        """실시간 최적"""
        return "traoptimal"
    @staticmethod
    def traavoidtoll() -> str:
        """무료 우선"""
        return "traavoidtoll"
    @staticmethod
    def traavoidcaronly() -> str:
        """자동차 전용도로 회피 우선"""
        return "traavoidcaronly"


class NCPMapsGeocoding(object):
    def __init__(self, address: str):
        self.url = "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode"
        self.address = address
        self.headers = {
            "X-NCP-APIGW-API-KEY-ID": NCPMapsGeocodingKeyID(),
            "X-NCP-APIGW-API-KEY": NCPMapsGeocodingKey()
        }

class NCPMapsDirections(object):
    def __init__(self, departures: str, arrival: str, option):
        self.url = "https://naveropenapi.apigw.ntruss.com/map-direction/v1/driving"
        self.departures = departures
        self.arrival = arrival
        self.option = option

        self.headers = {
            "X-NCP-APIGW-API-KEY-ID": NCPMapsDirectionsKeyID(),
            "X-NCP-APIGW-API-KEY": NCPMapsDirectionsKey()
        }