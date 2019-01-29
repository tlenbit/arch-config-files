#!/usr/bin/python

import json
from subprocess import check_output, call
import sys

ws_data = (json.loads(check_output(['i3-msg','-t','get_workspaces'])))

shift = int(sys.argv[1])
l = len(ws_data)
for (num, x)  in enumerate(ws_data):
  if x['visible'] == True:
    call(['i3-msg','workspace',ws_data[(num+shift)%l]['name']])
    

