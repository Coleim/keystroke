import json
import matplotlib.pyplot as plt
import keyboard
import json
import os

frequency_json_file = 'keystroke_frequency.json'

def add_data(key, val, newData):
    if key in newData:
        oldVal = newData[key]
        newData[key] = oldVal + val
    else:
        newData[key] = val

def extract_modifiers(frequency_dict):
    new_frequency = {}
    for k,v in frequency_dict.items():
        if '+' in k:
            parts = k.split('+')
            for p in parts:
                add_data(p, v, new_frequency)
        else:
            add_data(k, v, new_frequency)
    return new_frequency 


def read_existing_frequency(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    return {}

frequency_dict = read_existing_frequency(frequency_json_file)


with open(frequency_json_file, 'r', encoding='utf-8') as file:
    data = json.load(file)
    newData = extract_modifiers(data)
    

