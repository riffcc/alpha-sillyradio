#!/usr/bin/python3

# How many radios do you want? (not zero-indexed)
howManyRadios = 25

# Generate a docker-compose file with that many radios.

for i in range(1,howManyRadios+1):
  # Calculate the ports we need
  portANum = 30001 + i - 1
  portBNum = 40001 + i - 1

  # Create the configuration
  s = '''\
[Connection.bobby-{radioNum}]
Host=10.1.1.30
UseSSL=0
CertFile=
CertPass=
Autoreconnect=1
Port={portANum}
UserName=admin
Password=ZXhhbXBsZS1wYXNzd29yZA==
UseProxy=0
UseSockProxy=0
ProxyHost=
ProxyPort=8080
ProxyUser=
ProxyPass=
PathMap=
DownSpeeds=0,10,25,50,100,250,500,750,1000,2500,5000,7000
UpSpeeds=0,10,25,50,100,250,500,750,1000,2500,5000,7000
'''.format(radioNum=i,portANum=portANum,portBNum=portBNum)
  # Print the configuration
  print(s)

# Finished printing the main stuff!

