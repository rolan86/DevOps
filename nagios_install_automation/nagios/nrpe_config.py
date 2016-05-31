#!/usr/bin/python

servers = open('servers.csv','r')
nservers = ['allowed_hosts=127.0.0.1']
for server in servers:
	sg_name, s_name, s_ip, s_type = server.split(',')
	if s_type.strip('\n') == 'server':
		nservers.append(s_ip)
servers.close()
nrpe_o = open('/etc/nagios/nrpe.cfg.bkp','r')
nrpe_a = open('/etc/nagios/nrpe.cfg','w')
for line in nrpe_o:
	if 'allowed_hosts=127.0.0.1' in line:
		sline = ','.join(nservers)
		nrpe_a.write(sline)
		nrpe_a.write('\n')
	else:
		nrpe_a.write(line)
nrpe_a.close()
nrpe_o.close()