from pyefa.classes import Station
from pyefa.networks import DING


def get_trip_for_university():
    origin_station = Station()
    origin_station.name = "Theater"
    origin_station.place = "Ulm"

    destination_station = Station()
    destination_station.name = "Universität Süd"
    destination_station.place = "Ulm"

    efa_api = DING()
    result = efa_api.tripRequest(origin_station, destination_station, apitype="xml")

    return result


if __name__ == "__main__":
    print(get_trip_for_university())
