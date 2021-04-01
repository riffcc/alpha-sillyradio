# sillyradio

# Instructions
Follow the TODO first.

Using python3, generate a docker-compose file

python3 create.py > docker-compose.yaml

Then run docker-compose up -d

Done! Your farm will start on port 30001, incrementing by 1 for each instance.

Username admin and password default-password are the default credentials but feel free to change them as needed.

# TODO
## set up fd stuff
echo "1048576000" > /proc/sys/fs/nr_open

## set kernel tuning and limits
net.core.rmem_default=419430400
net.core.rmem_max=419430400

net.core.wmem_default=419430400
net.core.wmem_max=419430400

fs.file-max=1000000000

vm.max_map_count=1000000000

