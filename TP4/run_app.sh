#!/bin/bash
docker run --rm  \
  -p 5000:5000  \
  --mount type=bind,src=/TP4/srv,dst=/srv  \
  --name tp4-app  \
  --network net-tp4  \
  im-tp4-2  \
