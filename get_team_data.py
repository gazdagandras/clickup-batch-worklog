import os
import json
from urllib import request, parse
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

CLICKUP_ACCESS_TOKEN = os.getenv('CLICKUP_ACCESS_TOKEN')
CLICKUP_TEAM_ID = os.getenv('CLICKUP_TEAM_ID')

headers = {
  'Authorization': CLICKUP_ACCESS_TOKEN,
  'Content-Type': 'application/json'
}

req = request.Request('https://api.clickup.com/api/v1/team/' + CLICKUP_TEAM_ID + '/', headers=headers)

response_body = request.urlopen(req).read()
pprint(json.loads(response_body))


