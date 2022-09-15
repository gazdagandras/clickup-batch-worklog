import os
import csv
import time
import datetime
from urllib import request, parse
from dotenv import load_dotenv

load_dotenv()

CLICKUP_USER_ID = os.getenv('CLICKUP_USER_ID')
CLICKUP_ACCESS_TOKEN = os.getenv('CLICKUP_ACCESS_TOKEN')

with open("./times.csv", 'r') as file:
  csvreader = csv.reader(file, delimiter=';')
  for row in csvreader:
    taskId = row[0]
    dateTime = row[1]
    durationInMin = row[2]
    desc = row[3]

    duration = int(durationInMin) * 60 * 1000

    date_time = datetime.datetime.strptime(dateTime, "%Y-%m-%d %H:%M:%S")
    unixTime = time.mktime(date_time.timetuple())

    print(taskId, dateTime, durationInMin, desc)

    values = {
        "description": desc,
        "start": 1655881788000,
        "billable": true,
        "duration": duration,
        "assignee": int(CLICKUP_USER_ID),
        "tid": taskId
      }

    headers = {
      'Authorization': CLICKUP_ACCESS_TOKEN,
      'Content-Type': 'application/json'
    }

    print(values)

    postData = parse.urlencode(values).encode()

    req = request.Request('https://api.clickup.com/api/v2/team/2545761/time_entries/?custom_task_ids=&team_id=', data=postData, headers=headers)

    response_body = request.urlopen(req).read()
    print(response_body)


