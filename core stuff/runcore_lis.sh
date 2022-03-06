#!/bin/sh
python3 -m http.server
cd /home/ubuntu
nohup tcpdump -w isrunning