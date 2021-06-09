#!/usr/bin/python3
from pathlib import Path
import os

# How many radios do you want? (not zero-indexed)
howManyRadios = 3

os.makedirs("/opt/radio/", exist_ok=True)

# Start our docker-compose.yml file
compose = """
# Many thanks to FairCopy on Reddit for the inspiration.
# Thanks to https://github.com/crazy-max/docker-rtorrent-rutorrent/ for the Docker image.
# You can use this to manually start containers using Docker Compose.
version: '3.2'

services:"""

# Generate a docker-compose fragment for each radio.
for i in range(1, howManyRadios+1):
    # Set up ports
    dhtPort = 21002
    xmlRPCPort = 22002
    rutorrentPort = 23002
    webDAVPort = 24002
    rtIncPort = 25002
    # Calculate the ports we need
    dhtPortSet = 21002 + i - 1
    xmlRPCPortSet = 22002 + i - 1
    rutorrentPortSet = 23002 + i - 1
    webDAVPortSet = 24002 + i - 1
    rtIncPortSet = 25002 + i - 1

    # Create the configuration
    dc = '''
  geoip{i}:
    image: crazymax/geoip-updater:latest
    volumes:
      - "/opt/radio/{i}/config/geoip:/data"
    env_file:
      - "config/geoip.env"
    restart: always

  rtorrent{i}:
    image: crazymax/rtorrent-rutorrent:latest
    expose:
      - "{dhtPortSet}/udp"
      - "{xmlRPCPortSet}"
      - "{rutorrentPortSet}"
      - "{webDAVPortSet}"
      - "{rtIncPortSet}"
    ports:
      - target: {dhtPortSet}
        published: {dhtPortSet}
        protocol: udp
      - target: {rutorrentPortSet}
        published: {rutorrentPortSet}
        protocol: tcp
      - target: {webDAVPortSet}
        published: {webDAVPortSet}
        protocol: tcp
      - target: {rtIncPortSet}
        published: {rtIncPortSet}
        protocol: tcp
    env_file:
      - "config/rtorrent.env"
    volumes:
      - "/opt/radio/{i}/data:/data"
      - "/opt/radio/{i}/completed:/downloads"
      - "/opt/radio/{i}/config/passwd"
    ulimits:
      nproc: 65535
      nofile:
        soft: 123456789
        hard: 419430400
    restart: always

  rtorrent-logs{i}:
    image: bash
    command: bash -c 'tail -f /log/*.log'
    depends_on:
      - rtorrent{i}
    volumes:
      - "/opt/radio/{i}/logs:/log"
    restart: always
'''.format(i=i,
           dhtPortSet=dhtPortSet,
           xmlRPCPortSet=xmlRPCPortSet,
           rutorrentPortSet=rutorrentPortSet,
           webDAVPortSet=webDAVPortSet,
           rtIncPortSet=rtIncPortSet
           )
    # Write the configuration
    print(dc)
    compose = compose + dc
    os.makedirs("/opt/radio/"+ str(i), exist_ok=True)
    os.makedirs("/opt/radio/"+ str(i) +"/data", exist_ok=True)
    os.makedirs("/opt/radio/"+ str(i) +"/completed", exist_ok=True)
    os.makedirs("/opt/radio/"+ str(i) +"/logs", exist_ok=True)
    os.makedirs("/opt/radio/"+ str(i) +"/config", exist_ok=True)

f = open(Path.home() + "/docker-compose.yml", "w")
f.write(compose)
f.close()

# Generate the final file
