#!/bin/bash
# Sends a DELETE request to the URL passed & displays the body of the response.
curl -s "$1" -X DELETE
