# sillyradio

# Instructions
Using python3, generate a docker-compose file

python3 create.py > docker-compose.yaml

# TODO
ansible-galaxy collection install community.docker

# set up fd stuff
echo "1048576000" > /proc/sys/fs/nr_open

# kernel tuning and limits
net.core.rmem_default=419430400
net.core.rmem_max=419430400

net.core.wmem_default=419430400
net.core.wmem_max=419430400

fs.file-max=1000000000

vm.max_map_count=1000000000

# now start docker
docker-compose up -d

