#!/bin/bash
# Takes in a URL as an argument, sends a GET request
# and displays the body of the URL
curl -sH "X-School-User-Id: 98" "$1"
