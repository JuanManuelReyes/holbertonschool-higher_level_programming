#!/bin/bash
#asd
curl -sI "$1" | grep "Allow:" | cut -f2,3,4 -d " "
