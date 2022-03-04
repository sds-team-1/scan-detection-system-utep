#!/bin/sh
python3 -m http.server
nohup tcpdump -w running
