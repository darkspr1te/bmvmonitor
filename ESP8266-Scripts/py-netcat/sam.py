from netcat import Netcat

# start a new Netcat() instance
nc = Netcat('192.168.10.211', 23)

nc.read_until('Checksum')
output = nc.read()
print output

