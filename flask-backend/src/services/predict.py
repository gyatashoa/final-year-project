import os
import pickle
import json

__symptom_headers: list[str] = None
__model = None


def load_artifacts():
    global __symptom_headers
    global __model
    with open(os.path.join(os.path.dirname(os.getcwd()), 'artifacts', 'symptom_columns.json'), 'r') as f:
        __symptom_headers = json.load(f)['symptom_names']

    with open(os.path.join(os.path.dirname(os.getcwd()), 'artifacts', 'mnb_model.pickle'), 'rb') as m:
        __model = pickle.load(m)


def make_prediction(symptoms: list[str]):
    encoded_values: list[int] = []
    if __symptom_headers is None or __model is None:
        load_artifacts()

    for s in __symptom_headers:
        try:
            index = symptoms.index(s)
            encoded_values.append(1)
        except ValueError as err:
            encoded_values.append(0)
    value = __model.predict([encoded_values])
    return value[0]


def get_symptoms():
    if __symptom_headers is None:
        load_artifacts()
    return __symptom_headers
