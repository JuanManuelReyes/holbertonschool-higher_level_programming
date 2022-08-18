#!/bin/bash
#Shows the body size in bytes
curl -sI 0.0.0.0:5000 | grep "Content-Length" | cut -f2 -d " "
