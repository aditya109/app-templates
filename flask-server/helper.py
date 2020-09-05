# try:
import json
# except Exception as e:
#     print(e)


def json_provider():

    with open("static/TestJSON.json", 'r') as file:
        json_string = file.read()
        return json.loads(json_string)

def error_provider():
    print(json.dumps({'error': 'Uh Oh ! Sorry Not Found'}))

