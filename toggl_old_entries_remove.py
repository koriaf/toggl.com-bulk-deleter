#!/usr/bin/env python3
import datetime
import time
import requests

API_USERNAME = 'your@toggl.com.email'
API_PASSWORD = 'your secure password'
API_URL = 'https://www.toggl.com/api/v8/'
# we don't care about timezone when deleting for several years
DATE_FORMAT = '%Y-%m-%dT%H:%M:%S+00:00'

start_date = datetime.date(2001, 1, 1)
end_date = datetime.date.today() - datetime.timedelta(days=365)
# you can specify custom datespan. Note now it isn't inclusive for end_date
# start_date = datetime.date(2013, 1, 1)
# end_date = datetime.date(2016, 1, 1)


def do_request(method, url, params={}):
    global API_PASSWORD, API_USERNAME
    full_url = '{}{}'.format(API_URL, url)
    print('Request', method, full_url)
    return method(
        full_url,
        params=params,
        auth=requests.auth.HTTPBasicAuth(API_USERNAME, API_PASSWORD)
    )


def fetch_1000_records(start_date, end_date):
    params = {
        'start_date': start_date.strftime(DATE_FORMAT),
        'end_date': end_date.strftime(DATE_FORMAT),
    }
    resp = do_request(requests.get, 'time_entries', params)
    assert resp.status_code == 200, resp
    return resp.json()


def delete_record(record):
    # print("Deleting ", record)
    resp = do_request(requests.delete, 'time_entries/{id}'.format(**record))
    assert resp.status_code == 200, resp.status_code
    return 1


def delete_records(records):
    deleted = 0
    for record in records:
        deleted += delete_record(record)
    return deleted

while delete_records(fetch_1000_records(start_date, end_date)):
    print("Next step...")
    time.sleep(0.5)
