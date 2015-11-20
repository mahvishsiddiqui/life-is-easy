

#!/bin/bash
# Script adb+
# Usage: You can run any adb command on multiple(all) devices connected through usb
# ./adb+ <command> is the equivalent of ./adb -s <serial number> <command>

# Examples: 
# ./adb+ version
# ./adb+ uninstall <packagename>
# ./adb+ install example.apk
# adb+ install -r example.apk
# ./adb+.sh install -r <path/to/your/example.apk>


# To run from your mac, download desired apk to same folder as this script, (For me script and apk both are in  the downloads folder)
# then run following for clean install
# ./adb+.sh uninstall com.example.android
# ./adb+.sh install -r example.apk
# Created by Mahvish Siddiqui on 2015-05-28

adb devices | while read line
do
if [ ! "$line" = "" ] && [ `echo $line | awk '{print $2}'` = "device" ]
then
device=`echo $line | awk '{print $1}'`
echo "$device $@ ..."
adb -s $device $@
fi
done