#!/bin/bash
# Displays only the status code of the response.
curl -so /dev/null "${1}" -w "%{http_code}"
