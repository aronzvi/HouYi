import json
import pathlib

# load config file
config_file_path = pathlib.Path("./config.json")
config = json.load(open(config_file_path))