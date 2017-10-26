#!/usr/bin/python

import sys
from subprocess import check_output, call

max_brightness = int(check_output(['cat', '/sys/class/backlight/intel_backlight/max_brightness']))
step = int(sys.argv[1])
current_brightness = int(check_output(['cat', '/sys/class/backlight/intel_backlight/brightness']))
#call(['echo', str(current_brightness + step), '>', '/sys/class/backlight/intel_backlight/brightness'])
f = open('/sys/class/backlight/intel_backlight/brightness', 'w')
change = current_brightness + step


if change > max_brightness:
  f.write(str(max_brightness))
else:
  if change < 0:
    f.write('1')
  else:
    f.write(str(change))

f.close()
