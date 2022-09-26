#!/bin/bash

#OPTION=$(nordvpn countries | sed 's/\t/\n/g' | sed '/^[[:space:]]*$/d' | sed -e "s/\r//g" | sed -e 's/-  -  //g' | awk '{print tolower($0)}' | sed '1i disconnect' | sed '1i cancel' | dmenu -l 30)


COUNTRIES_LIST=$HOME/.config/polybar/scripts/nordvpn_countries.txt
OPTION=$(cat $COUNTRIES_LIST | awk '{print tolower($0)}' | sed '1i disconnect' | sed '1i cancel' | dmenu -l 30)

if [[ "$OPTION" == "disconnect" ]]
then
    nordvpn disconnect
elif [[ "$OPTION" == "cancel" ]]
then
    exit 1
elif $(grep -Fxqi "$OPTION" $COUNTRIES_LIST)
then
    echo "Connecting to $OPTION"
    nordvpn connect $OPTION
else
    exit 1
fi
