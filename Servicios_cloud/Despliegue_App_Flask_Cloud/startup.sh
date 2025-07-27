#!/bin/bash
sudo apt update
sudo apt install -y python3-pip
pip3 install Flask==2.2.5 gunicorn==20.1.0
cd /home/angel/app
nohup gunicorn -w 2 -b 0.0.0.0:8080 app:app &
