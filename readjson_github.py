import json, datetime, os

# first part is to find all the directories that have .json
# compiles into an array that can be used later
#dir_path needs to be more specific just to avoid weird inputs

with open('C:/Users/Niraj/Desktop/ieor171_gsi/ieor_171_team2/ieor_171_team2.json', encoding='utf-8-sig') as json_file:
    json_data = json.load(json_file)
for i in range(len(json_data)):
    w = json_data[i]["edge_media_to_caption"]["edges"][0]["node"]["text"]
    v = datetime.datetime.fromtimestamp(int(json_data[i]["taken_at_timestamp"])).strftime('%Y-%m-%d %H:%M:%S')
    print(json_data[i]["edge_media_to_caption"]["edges"][0]["node"]["text"])
    print(datetime.datetime.fromtimestamp(int(json_data[i]["taken_at_timestamp"])).strftime('%Y-%m-%d %H:%M:%S'))
