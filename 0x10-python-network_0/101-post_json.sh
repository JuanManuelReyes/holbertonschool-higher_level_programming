#!/bin/bash
#coment
curl -s --request POST "$1" -H 'Content-Type: application/json' -d @"$2"
