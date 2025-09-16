#!/bin/bash
docker run -d --rm  \
  -p 5000:5000  \
  -v $(pwd)/srv:/srv  \
  --name tp4-app-2  \
  --network net-tp4  \
  im-tp4-2  \
  1>/dev/null 2>/dev/null
