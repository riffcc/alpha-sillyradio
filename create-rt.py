#!/usr/bin/python3

# How many radios do you want? (not zero-indexed)
howManyRadios = 3

# Generate a docker-compose file with that many radios.

# Print a header
header = """# Many thanks to FairCopy on Reddit for the inspiration.
# Thanks to https://github.com/crazy-max/docker-rtorrent-rutorrent/ for the Docker image.
# You can use this to manually start containers using Docker Compose.
version: '3.2'

services:"""
print(header)

for i in range(1,howManyRadios+1):
  # Calculate the ports we need
  portANum = 21130 + i - 1
  portBNum = 6881 + i - 1

  # Create the configuration
  s = '''\
  geoip{radioNum}:
    image: crazymax/geoip-updater:latest
    volumes:
      - "/opt/radio/{radioNum}/data/geoip:/data"
    env_file:
      - "/opt/radio/{radioNum}/geoip-updater.env"
    restart: always

  rtorrent{radioNum}:
    image: crazymax/rtorrent-rutorrent:latest
    expose:
      - "${RT_DHT_PORT}/udp"
      - "${XMLRPC_PORT}"
      - "${RUTORRENT_PORT}"
      - "${WEBDAV_PORT}"
      - "${RT_INC_PORT}"
    ports:
      - target: ${RT_DHT_PORT}
        published: ${RT_DHT_PORT}
        protocol: udp
      - target: ${RUTORRENT_PORT}
        published: ${RUTORRENT_PORT}
        protocol: tcp
      - target: ${WEBDAV_PORT}
        published: ${WEBDAV_PORT}
        protocol: tcp
      - target: ${RT_INC_PORT}
        published: ${RT_INC_PORT}
        protocol: tcp
    env_file:
      - "/opt/radio/{radioNum}/rtorrent-rutorrent.env"
      - ".env"
    volumes:
      - "./data:/data"
      - "./downloads:/downloads"
      - "./passwd:/passwd"
    ulimits:
      nproc: 65535
      nofile:
        soft: 32000
        hard: 40000
    restart: always

  rtorrent-logs:
    image: bash
    command: bash -c 'tail -f /log/*.log'
    depends_on:
      - rtorrent-rutorrent
    volumes:
      - "./data/rtorrent/log:/log"
    restart: always
'''.format(radioNum=i,portANum=portANum,portBNum=portBNum)
  # Print the configuration
  print(s)

# Finished printing the main stuff!
