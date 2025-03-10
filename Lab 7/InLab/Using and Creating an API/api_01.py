import numpy as np
import pandas as pd
import requests
import json

url = "https://wind-bow.glitch.me/twitch-api/channels/freecodecamp"
JSONContent = requests.get(url).json()
content = json.dumps(JSONContent, indent = 4, sort_keys=True)
# print(content)

# List of channels we want to access
channels = ["ESL_SC2", "OgamingSC2", "cretetion", "freecodecamp", "storbeck", "habathcx", "RobotCaleb", "noobs2ninjas",
            "ninja", "shroud", "Dakotaz", "esltv_cs", "pokimane", "tsm_bjergsen", "boxbox", "wtcn", "a_seagull",
           "kinggothalion", "amazhs", "jahrein", "thenadeshot", "sivhd", "kingrichard"]

channels_list = []
# For each channel, we access its information through its API
for channel in channels:
    JSONContent = requests.get("https://wind-bow.glitch.me/twitch-api/channels/" + channel).json()
    if 'error' not in JSONContent:
        channels_list.append([JSONContent['_id'], JSONContent['display_name'], JSONContent['status'],
                             JSONContent['followers'], JSONContent['views']])
                         
dataset = pd.DataFrame(channels_list)
print(dataset.sample(5))
