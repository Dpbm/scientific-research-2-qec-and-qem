import json
import os

def export_data_json(data:dict, filename:str):
    with open(filename, "w") as file:
        print(f"saving {filename}...")
        json_obj = json.dumps(data, indent=4)
        file.write(json_obj)

def generate_output_dir(path:str):
    if(os.path.exists(path)):
        print(f"{path} already exists!")
        return
        
    print(f"Creating folder: {path}")
    os.mkdir(path)

def generate_full_file_path(base_path:str, file:str) -> str:
    return os.path.join(base_path, file)