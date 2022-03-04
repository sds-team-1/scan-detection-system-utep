#!/bin/sh
python3 -m http.server
cd /home/ubuntu
tcpdump -w isrunning