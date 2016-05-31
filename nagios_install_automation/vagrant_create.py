import subprocess

def command_run(command):
	process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)
	for line in iter(process.stdout.readline, b''):
		print line,
	output = process.communicate()
	process.stdout.close()
	return output[0]

def vagrant_config(ipadd):
	"""
	This will refer to a config file, and add in the below line to allow a private ip
	"""
	vcfile = open("vagrant_config","r")
	vfile = open("Vagrantfile","w")
	found = 0
	for line in vcfile:
		if "config.vm.network" in line and found==0:
			ipconfig = '  config.vm.network "private_network", ip: "%s"\n'%ipadd
			vfile.write(ipconfig)
			found = 1
		vfile.write(line)
	vfile.close()
	vcfile.close()
	return "Vagrantfile written"

"""	
if __name__ == "__main__":
	#print command_run("vagrant box add precise32 http://files.vagrantup.com/precise32.box")
	#print command_run("vagrant init precise32")
	#print vagrant_config("192.168.56.30")
	print command_run("vagrant up jenkins")
"""	