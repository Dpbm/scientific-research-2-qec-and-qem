import json
import os

def export_data_json(data, filename):
    with open(filename, "w", encoding="utf-8") as file:
        print(f"saving {filename}...")
        json_obj = json.dumps(data, indent=4)
        file.write(json_obj)

def generate_output_dir(path):
    if(os.path.exists(path)):
        print(f"{path} already exists!")
        return
        
    print(f"Creating folder: {path}")
    os.mkdir(path)

def generate_full_file_path(base_path, file):
    return os.path.join(base_path, file)

def import_json_data(path):
    print(f"Getting data from: {path}")
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)