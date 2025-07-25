#!/usr/bin/env bash

apt-get update
apt-get install -y wget gnupg ca-certificates fonts-liberation libappindicator3-1 libasound2 libatk-bridge2.0-0 libatk1.0-0 libcups2 libdbus-1-3 \
libgdk-pixbuf2.0-0 libnspr4 libnss3 libx11-xcb1 libxcomposite1 libxdamage1 libxrandr2 libxss1 libxtst6 lsb-release xdg-utils libgbm1 libxshmfence1 libxkbcommon0

playwright install

uvicorn main:app --host 0.0.0.0 --port 10000
