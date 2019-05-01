import requests
import json
import os
import time

states = [
    '01',  '02',  '03',  '04',  '05',  '06',  '07',  '08',
    '09',  '10',
    "AL",  "AK",  "AS",  "AZ",  "AR",  "CA",  "CO",  "CT",
    "DE",  "DC",  "FM",  "FL",  "GA",  "GU",  "HI",  "ID",
    "IL",  "IN",  "IA",  "KS",  "KY",  "LA",  "ME",  "MH",
    "MD",  "MA",  "MI",  "MN",  "MS",  "MO",  "MT",  "NE",
    "NV",  "NH",  "NJ",  "NM",  "NY",  "NC",  "ND",  "MP",
    "OH",  "OK",  "OR",  "PW",  "PA",  "PR",  "RI",  "SC",
    "SD",  "TN",  "TX",  "UT",  "VT",  "VI",  "VA",  "WA",
    "WV",  "WI",  "WY"
]


def get_state_data(state):
    requestUrl = 'https://ofmpub.epa.gov/echo/sdw_rest_services.get_systems?output=JSON&p_st=%s&p_act=Y' % state
    data = get_json_data(requestUrl)
    qID = data['Results']['QueryID']
    if qID:
        print('%s qid=%s' % (state, qID))
        get_facility_data(state, qID)
        # yeah, sleeping 10 seconds sux but they have strict rate limits. should be able to make it through state
        time.sleep(2)


def get_facility_data(state, query_id):
    proceed = True
    page_number = 0
    while proceed is True:
        page_number += 1  # page 0 doesn't include data
        url = 'https://ofmpub.epa.gov/echo/sdw_rest_services.get_qid?output=JSON&qid=%s&pageno=%s' % (
            query_id, page_number)
        target_file = os.path.join(
            os.getcwd(), 'epaData/stateJson/%spage%s.json' % (state, page_number))
        # should try/except here to handle timeouts, over hitting API
        data = get_json_data(url)
        # returns an empty array when past last page of data
        if not data["Results"]["WaterSystems"]:
            proceed = False
            break
        save_json_data_to_file(data, target_file)


def get_json_data(url):
    raw_json = requests.get(url)
    if raw_json.status_code == 200:
        data = json.loads(raw_json.content)
    else:
        raise ValueError('Invalid response: %s %s' %
                         (raw_json.status_code, raw_json.content))
    return data


def save_json_data_to_file(json_data, target_file):
    with open(target_file, 'w') as f:
        f.write(json.dumps(json_data))


if __name__ == "__main__":
    for state in states:
        print('Getting data for %s' % state)
        get_state_data(state)
