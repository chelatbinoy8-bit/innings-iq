import requests
from bs4 import BeautifulSoup
import json
import os

def get_live_data():
    # Placeholder for scraping logic - we'll target a public scorecard
    # For now, let's structure the JSON format your site will expect
    data = {
        "match_info": {
            "teams": "IND vs AUS",
            "score": "145/3 (18.2)",
            "batter": "Virat Kohli",
            "bowler": "Mitchell Starc",
            "last_12_balls": ["1", "4", "0", "wd", "1", "6", "W", "0", "1", "1", "2", "4"]
        },
        "oracle_insight": "Starc is targeting the blockhole. Kohli's strike rate against left-arm pace at this length is 112%. Expect a flick towards mid-wicket.",
        "win_probability": "68%",
        "negative_tracker": [
            {"event": "Dropped Catch (12.4 ov)", "tax": "+14 runs"},
            {"event": "Misfield (15.1 ov)", "tax": "+4 runs"}
        ]
    }
    return data

def save_to_json(data):
    path = os.path.join('data', 'live_data.json')
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    live_info = get_live_data()
    save_to_json(live_info)
    print("Brain refreshed successfully.")
