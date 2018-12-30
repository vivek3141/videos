#!/usr/bin/env bash

sudo apt-get update -y
sudo apt-get install -y --no-install-recommends apt-utils
sudo apt-get install -y build-essential libsqlite3-dev sqlite3 bzip2 \
                         libbz2-dev zlib1g-dev libssl-dev openssl libgdbm-dev \
                         libgdbm-compat-dev liblzma-dev libreadline-dev \
                         libncursesw5-dev libffi-dev uuid-dev
sudo apt-get install -y wget
sudo apt-get install -y libcairo2-dev libjpeg-dev libgif-dev
sudo python3 -m pip install -r requirements.txt
sudo apt-get install -y ffmpeg
sudo apt-get install -y apt-transport-https
sudo apt-get install -y texlive-latex-base 
sudo apt-get install -y texlive-full
sudo apt-get install -y texlive-fonts-extra
sudo apt-get install -y sox
sudo apt-get install -y git


