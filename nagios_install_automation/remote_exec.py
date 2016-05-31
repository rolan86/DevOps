#!/usr/bin/python
import param_module as pm
import vagrant_create as vg
import create_vgfile as cvg

HOST = ''
USER = 'vagrant'
PASSWD = 'vagrant'
CONF_PATH = 'nagios'
CONF_FILE = CONF_PATH+'/'+'servers.csv'


if __name__ == "__main__":
	
	print cvg.create_file()
	servers = open(CONF_FILE,'r')
	for server in servers:
		sg_name, s_name, HOST, s_type = server.split(',')
		vgcomm = 'vagrant up %s' %sg_name
		print vg.command_run(vgcomm)
#		print HOST, s_name, HOST, s_type
#		client = pm.ssh_client()
#		if s_type.strip('\n') == 'server':
#			install_file = CONF_PATH+'/'+'ngserver.sh'
#			transfer = pm.ptrans(HOST, USER, PASSWD)
#			print pm.sftp_put(transfer, install_file, '/home/vagrant/ngserver.sh')
#			inp, out, err = pm.comm_exec(client, HOST, USER, PASSWD, "sudo sh /home/vagrant/ngserver.sh")
#			print pm.parse_info(out)
			#inp, out, err = pm.comm_exec(client, HOST, USER, PASSWD, "sudo apt-get install nagios-nrpe-plugin -y")
			#print pm.parse_info(out)
#		else:
#			inp, out, err = pm.comm_exec(client, HOST, USER, PASSWD, "sudo apt-get update")
#			print pm.parse_info(out)
#			inp, out, err = pm.comm_exec(client, HOST, USER, PASSWD, "sudo apt-get install nagios-nrpe-server -y")
#			print pm.parse_info(out)		
	servers.close()