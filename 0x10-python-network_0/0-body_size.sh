#!/bin/bash
# presents the size of the response body.
curl -sI "$1" | grep "Content-Length:" | cut -d' ' -f2
