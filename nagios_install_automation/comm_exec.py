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
	
	servers = open(CONF_FILE,'r')
	nslist = []
	for server in servers:
		sg_name, s_name, HOST, s_type = server.split(',')
		print HOST, s_name, HOST, s_type
#		client = pm.ssh_client()
		if s_type.strip('\n') == 'server':
			client = pm.ssh_client()
			install_file = CONF_PATH+'/'+'nserver.sh'
			nagios_conf = CONF_PATH + '/' + 'nagios.conf'
			transfer = pm.ptrans(HOST, USER, PASSWD)
			print pm.sftp_put(transfer, install_file, '/home/vagrant/ngserver.sh')
			print pm.sftp_put(transfer, nagios_conf, '/home/vagrant/nagios.conf')
			inp, out, err = pm.comm_exec(client, HOST, USER, PASSWD, "sudo apt-get update")
			print pm.parse_info(out)
			inp, out, err = pm.comm_exec(client, HOST, USER, PASSWD, "sudo sh /home/vagrant/ngserver.sh")
			print pm.parse_info(out)
			nslist.append(HOST)
			pm.sftp_close(transfer)
			pm.ssh_close(client)
		else:
			client = pm.ssh_client()
			sfile = CONF_PATH + '/' + 'servers.csv'
			cscript = CONF_PATH + '/' + 'nrpe_config.py'
			transfer = pm.ptrans(HOST, USER, PASSWD)
			print pm.sftp_put(transfer, sfile, '/home/vagrant/servers.csv')
			print pm.sftp_put(transfer, cscript, '/home/vagrant/nrpe_config.py')
			inp, out, err = pm.comm_exec(client, HOST, USER, PASSWD, "sudo apt-get update")
			print pm.parse_info(out)	
			inp, out, err = pm.comm_exec(client, HOST, USER, PASSWD, "sudo apt-get install nagios-nrpe-server nagios-plugins -y")
			print pm.parse_info(out)
			inp, out, err = pm.comm_exec(client, HOST, USER, PASSWD, "sudo mv /etc/nagios/nrpe.cfg /etc/nagios/nrpe.cfg.bkp")
			print pm.parse_info(out)
			inp, out, err = pm.comm_exec(client, HOST, USER, PASSWD, "sudo python nrpe_config.py")
			print pm.parse_info(out)
			pm.sftp_close(transfer)
			pm.ssh_close(client)
	servers.close()