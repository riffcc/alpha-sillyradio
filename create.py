#!/usr/bin/python3

# How many radios do you want? (not zero-indexed)
howManyRadios = 25

# Generate a docker-compose file with that many radios.

# Print a header
header = """# Many thanks to FairCopy on Reddit for the inspiration
# and to github.com/dperson for the Docker image
# You can use this to manually start containers using Docker Compose.
version: '3'

services:"""
print(header)

for i in range(1,howManyRadios+1):
  # Calculate the ports we need
  portANum = 30001 + i - 1
  portBNum = 40001 + i - 1

  # Create the configuration
  s = '''\
  transmission{radioNum}:
    container_name: transmission{radioNum}
    image: dperson/transmission
    ulimits:
      nofile:
        soft: "99999999"
        hard: "99999999"
    volumes:
      - transmission{radioNum}:/var/lib/transmission-daemon
      - /mfsbrick.3/final{radioNum}:/mnt/download
      - /mnt/radio/watch{radioNum}:/mnt/watch
      - /mnt/radio/incomplete{radioNum}:/mnt/incomplete
    ports:
      - "{portANum}:9091/tcp"
      - "{portBNum}:40001/tcp"
      - "{portBNum}:40001/udp"
    # All options: https://github.com/transmission/transmission/wiki/Editing-Configuration-Files#options
    environment:
      - TRUSER=admin
      - TRPASSWD=example-password
      - USERID=1003
      - GROUPID=1003
      - TZ=Australia/Perth
      - TR_CACHE_SIZE_MB=512
      - TR_PEER_PORT=40001
      - TR_BLOCKLIST_URL=http://127.0.0.1
      - TR_MAX_PEERS_GLOBAL=500
      - TR_DHT_ENABLED=false
      - TR_PEX_ENABLED=false
      - TR_RATIO_LIMIT_ENABLED=false
      - TR_DOWNLOAD_DIR=/mnt/download
      - TR_INCOMPLETE_DIR_ENABLED=true
      - TR_INCOMPLETE_DIR=/mnt/incomplete
      - TR_SPEED_LIMIT_DOWN=2048
      - TR_SPEED_LIMIT_DOWN_ENABLED=false
      - TR_SPEED_LIMIT_UP=1024
      - TR_SPEED_LIMIT_UP_ENABLED=false
      - TR_ALT_SPEED_DOWN=512
      - TR_ALT_SPEED_UP=512
      - TR_ALT_SPEED_TIME_ENABLED=true
      - TR_ALT_SPEED_TIME_BEGIN=420 #  7:00, in minutes from midnight
      - TR_ALT_SPEED_TIME_END=1380  # 23:00
      - TR_ALT_SPEED_TIME_DAY=127   # All days: 127, Weekdays: 62, Weekends: 65
      - TR_START_ADDED_TORRENTS=true
      - TR_DOWNLOAD_QUEUE_ENABLED=true
      - TR_DOWNLOAD_QUEUE_SIZE=400
      - TR_SCRAPE_PAUSED_TORRENTS_ENABLED=false
      - TR_WATCH_DIR_ENABLED=true
      - TR_WATCH_DIR=/mnt/watch
    restart: unless-stopped
'''.format(radioNum=i,portANum=portANum,portBNum=portBNum)
  # Print the configuration
  print(s)

# Finished printing the main stuff!

# Now print volume definitions
# Print the header
print("volumes:")
for i in range(1,howManyRadios+1):
  print("  transmission"+str(i)+":")
