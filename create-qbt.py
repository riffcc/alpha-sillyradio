#!/usr/bin/python3

# How many radios do you want? (not zero-indexed)
howManyRadios = 25

# Generate a docker-compose file with that many radios.

# Print a header
header = """# Many thanks to FairCopy on Reddit for the inspiration
# and to the linuxserver.io project
# You can use this to manually start containers using Docker Compose.
version: '3'

services:"""
print(header)

for i in range(1,howManyRadios+1):
  # Calculate the ports we need
  portANum = 21130 + i - 1
  portBNum = 40001 + i - 1

  # Create the configuration
  s = '''\
  qbittorrent{radioNum}:
    container_name: qbt{radioNum}
    image: ghcr.io/linuxserver/qbittorrent
    ulimits:
      nofile:
        soft: "99999999"
        hard: "99999999"
    volumes:
      - /mfsbrick.3/final{radioNum}:/downloads
      - /mnt/radio/watch{radioNum}:/mnt/watch
      - /mnt/radio/incomplete{radioNum}:/mnt/incomplete
    ports:
      - "{portANum}:9091/tcp"
      - "{portBNum}:40001/tcp"
      - "{portBNum}:40001/udp"
    environment:
      - PUID=1003
      - PGID=1003
      - TZ=Australia/Perth
      - WEBUI_PORT={portANum}
    restart: unless-stopped
'''.format(radioNum=i,portANum=portANum,portBNum=portBNum)
  # Print the configuration
  print(s)

# Finished printing the main stuff!
