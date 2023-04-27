#!/bin/bash
# Script that sends a JSON POST
curl -s -H "Content-Type: application/json" -d @"$2" -X POST "$1"
