#!/bin/bash

dir=~/.config/i3/wallpapers_for_conky

array=($(ls $dir))

random_int=$(shuf -i 1-${#array[@]} -n 1)

feh --bg-center $dir/${array[random_int]}
