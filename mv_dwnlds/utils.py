import yaml

def read_config(config_file_path):
    with open(config_file_path) as config_file:
        data = yaml.load_all(config_file, Loader=yaml.FullLoader)
    return data
