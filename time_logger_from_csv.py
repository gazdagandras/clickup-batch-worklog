import os
import csv
import time
import datetime
import json
from urllib import request, parse
from dotenv import load_dotenv

load_dotenv()

CLICKUP_USER_ID = os.getenv('CLICKUP_USER_ID')
CLICKUP_TEAM_ID = os.getenv('CLICKUP_TEAM_ID')
CLICKUP_ACCESS_TOKEN = os.getenv('CLICKUP_ACCESS_TOKEN')

with open("./times.csv", 'r') as file:
  csvreader = csv.reader(file, delimiter=';')
  for row in csvreader:
    dateTime = row[0]
    durationInMin = row[1]
    desc = row[2]
    taskId = row[3]

    duration = int(durationInMin) * 60 * 1000

    date_time = datetime.datetime.strptime(dateTime, "%Y-%m-%d %H:%M:%S")
    unixTime = int(time.mktime(date_time.timetuple()) * 1000)

    print(taskId, dateTime, durationInMin, desc)

    values = {
        "description": desc,
        "start": unixTime,
        "billable": "true",
        "duration": duration,
        "assignee": int(CLICKUP_USER_ID),
        "tid": taskId
      }

    headers = {
      'Authorization': CLICKUP_ACCESS_TOKEN,
      'Content-Type': 'application/json'
    }

    print(values)

    postData = json.dumps(values).encode('utf8')

    req = request.Request('https://api.clickup.com/api/v2/team/' + CLICKUP_TEAM_ID + '/time_entries/', data=postData, headers=headers)

    response_body = request.urlopen(req).read()
    print(response_body)


