#!/bin/sh
docker run --rm sullo/nikto  -h 10.0.0.1 -p 8000
>isvalid.txt