function cs() {
  cd "$@" && ls
  }
alias lumos="tee /sys/class/backlight/intel_backlight/brightness <<<"
alias ll="ls -la --block-size=MB"
alias ls='ls --color=auto'
alias wget='wget --inet4-only'
alias qutebrowser='qutebrowser --backend webengine'

# eye candy
alias cava2='urxvt --transparent true -e cava & disown & exit'
alias matrix='urxvt --transparent true -e cmatrix -b -a -u 1 & disown & exit'

if [ "$EUID" != "0" ] 
then
  PS1='\[\e[0;34m\] \w $ \[\e[0m\]'
else
  PS1='\[\e[0;31m\] \w # \[\e[0m\]'
fi  

HISTSIZE=1000

# neofetch --config /home/cristo/.config/neofetch/config
#--ascii_colors 6 6 1 8 8 6
neofetch --ascii ~/.config/neofetch/ascii_logos/12

# added by Anaconda3 4.4.0 installer
export PATH="/home/cristo/anaconda3/bin:$PATH"
