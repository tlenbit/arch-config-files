#!/bin/bash

if [ $(setxkbmap -query | grep layout | cut -d ':' -f 2 | sed "s/ //g") == 'us' ]
then
  setxkbmap ru
else
  setxkbmap us
fi
