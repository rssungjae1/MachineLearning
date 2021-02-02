import json

def jsonReader():
    with open('./searchIndexs.json', 'r', encoding="utf-8") as f:
        json_data = json.load(f)
    result = json_data['cats']['category']
    print(result)
    return result