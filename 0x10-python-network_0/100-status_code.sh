#!/bin/bash
# Sends a request to url, display status code only
curl -s -o /dev/null -w "%{http_code}" "$1"
