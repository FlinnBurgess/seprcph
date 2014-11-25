import json

def objs_from_json_file(file_path, cls):
    with open(file_path, 'r') as json_file:
        return json.load(json_file, object_hook=lambda x: cls(**x))
