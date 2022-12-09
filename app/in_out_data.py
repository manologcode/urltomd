import yaml
import sys
import os

from yaml.loader import SafeLoader

class InOutData:

    def read_yaml(file_name):
        with open(file_name) as f:
            data = yaml.load(f, Loader=SafeLoader)
        return data

    config=read_yaml('config.yml')

    @staticmethod
    def input_data(config):
        data = {}
        print()
        print()
        print(config['title'])
        divider = '-' * len(config['title'])
        print(divider)
        print()
        for k in config['fields']:
            data[k] = input( config['fields'][k] )
            print()
        print(divider)
        return data

    @staticmethod
    def menu(config):
        ans=True
        divider = '-' * len(config['title'])
        print()
        print(divider)
        print(config['title'])
        print(divider)
        print()
        print(config['description'])
        print()
        for item in config['items']:
            print()
            print(item)
        print()
        print(divider)
        print()
        ans = input("Que opción quieres? ") 
        return ans


    
    @staticmethod
    def create_yaml_data( name, data):
        file_name = name + ".yml"
        print(f"Creando: {file_name}")
        with open( InOutData.config['folder_export'] + file_name, 'w') as f:
            data = yaml.dump(data, f, sort_keys=False)
    
    @staticmethod
    def read_params():
        response = {}
        print(sys.argv)
        if len(sys.argv) > 1:
            param = sys.argv[1]
            path_file = InOutData.config['folder_export'] + param
            if os.path.isfile(path_file):
                response['file'] = path_file
        response = response if response!={} else None
        return response