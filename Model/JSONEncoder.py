import json
import numpy as np
from Model.model import dlnet


class NumpyEncoder(json.JSONEncoder):
    """ Special json encoder for numpy types """

    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


def Read(nn):
    f = open("preparation_data.json", "r")
    parsed_json = json.loads(f.read())
    nn.param = dict(parsed_json["param"])
    nn.ch = dict(parsed_json["ch"])
    nn.ch["Z1"] = np.array(nn.ch["Z1"])
    nn.ch["Z1"] = np.array(nn.ch["Z1"])
    nn.ch["A1"] = np.array(nn.ch["A1"])
    nn.ch["A2"] = np.array(nn.ch["A2"])
    nn.param["W1"] = np.array(nn.param["W1"])
    nn.param["W2"] = np.array(nn.param["W2"])
    nn.param["b1"] = np.array(nn.param["b1"])
    nn.param["b2"] = np.array(nn.param["b2"])


def Write(nn):
    json_object = json.dumps(nn.__dict__, cls=NumpyEncoder)
    with open('preparation_data.json', 'w') as outfile:
        outfile.write(json_object)