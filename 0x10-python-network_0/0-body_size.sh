#!/bin/bash
#This script accepts a URL as input,
#initiates a request to the specified URL,
#and presents the size of the response body.
curl -sI "$1" | grep "Content-Length:" | cut -d' ' -f2
