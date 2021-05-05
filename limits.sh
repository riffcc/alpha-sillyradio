#!/bin/bash
# Reset limits on macOS
sudo sysctl kern.maxfiles=512753664 kern.maxfilesperproc=1108197376
sudo launchctl limit maxfiles 512753664 1108197376
