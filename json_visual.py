from pyvis.network import Network
import json

file = "C:\\Users\\1\\PycharmProjects\\test\\alcuin_letters.json"

def get_data():
    with open(file, "r") as json_file:
        data = json.load(json_file)
        return (data["alcuin_letters"])


def prt_data():
    epp_data = get_data()
    return epp_data
