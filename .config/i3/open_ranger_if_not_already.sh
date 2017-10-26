#!/bin/bash
if [[ ! $(xlsclients | grep "ranger") ]]; then urxvt -e ranger;  fi
