#!/usr/bin/python
import param_module as pm
import vagrant_create as vg
import create_vgfile as cvg

HOST = '192.168.56.20'
USER = 'vagrant'
PASSWD = 'vagrant'


if __name__ == "__main__":
	#print vg.command_run("vagrant box add precise32 http://files.vagrantup.com/precise32.box")
	#print vg.command_run("vagrant init precise32")
	#print vg.vagrant_config("192.168.56.20")
	#print vg.command_run("vagrant up")
	
	print cvg.create_file()
	print vg.command_run("vagrant up jenkins")

    
	client = pm.ssh_client() 
	transfer = pm.ptrans(HOST, USER, PASSWD)
	print pm.sftp_put(transfer, 'jenkins_config/jenkinstall.sh', '/home/vagrant/jenkinstall.sh')
	print pm.sftp_put(transfer, 'jenkins_config/config.xml', '/home/vagrant/config.xml')
	inp, out, err = pm.comm_exec(client, HOST, USER, PASSWD, "sudo sh /home/vagrant/jenkinstall.sh")
	jinstall = pm.parse_info(out)
	#for info in jinstall:
	#	print info
	inp, out, err = pm.comm_exec(client, HOST, USER, PASSWD, "sudo service jenkins restart")
	jserver = pm.parse_info(out)
	for info in jserver:
		print info