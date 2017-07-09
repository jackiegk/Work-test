#!/bin/sh
#for i in `seq 0 3`; do
	my_current_date=`date +%Y_%m_%d`
	my_current_time=`date +%H_%M_%S`
	if [ ! -d  /mnt/sda3/mjpg/pic/$my_current_date ]
	then
		mkdir /mnt/sda3/mjpg/pic/$my_current_date
	fi
	wget  "http://192.168.123.100:8080/?action=snapshot" -O /mnt/sda3/mjpg/pic/$my_current_date/$my_current_time.jpg
	echo $i
	sleep 12
exit
