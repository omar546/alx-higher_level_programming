#!/bin/bash
# sends a JSON POST request to a URL passed as the first argument, and displays the body
# send a POST request with the contents of a file, passed with the filename as the second argument,
#in the body of the request.
curl -s "$1" -X POST -H "Content-Type: application/json" -d "$(cat "$2")"
