import yaml

with open ('YOUR YAML FILE' , 'r') as file:
    try:
        print(yaml.safe_load(file))
    except yaml.YAMLError as exc:
        print(exc)