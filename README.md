The Silly Radio
===============
Silly Radio allows you to create a farm of BitTorrent clients used for hosting massive amounts of files with few resources. It is intended to be capable of hosting one million torrents on a single machine.

Requirements
============
* A modern Linux, details are up to you. (WSL unsupported but may work.)
* Git
* Ansible 2.9+
* Enough RAM and CPU to handle the number of torrents you want to host
* Plenty of disk space!
* Docker Engine and docker-compose installed and working
* (Optional) Docker access for the user you wish to work with

Getting started
===============
Check out this repository using Git.

`git clone https://github.com/riffcc/sillyradio.git`

Edit the inventory file to include your machine.

Use Ansible to bring up your machine.

`ansible-playbook site.yml`

Use Python to generate a docker-compose file.

`python3 create.py > docker-compose.yaml`

Then use docker-compose to bring up your farm.

`docker-compose up`

Done! Your farm will start on port 21130, incrementing by 1 for each instance.

Username admin and password default-password are the default credentials but feel free to change them as needed.
