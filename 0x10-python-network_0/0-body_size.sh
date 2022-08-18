#!/bin/bash
#Shows the body size in bytes
curl -sI "$1" | grep "Content-Length" | cut -f2 -d " "
