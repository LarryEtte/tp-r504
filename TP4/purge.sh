#!/bin/bash
docker stop $(docker ps -aq) 1>/dev/null 2>/dev/null
docker rm $(docker ps -aq) 1>/dev/null 2>/dev/null
docker system prune -a --volumes -f 1>/dev/null 2>/dev/null
