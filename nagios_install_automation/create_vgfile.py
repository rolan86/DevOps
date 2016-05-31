#!/usr/bin/python
def create_file():
	sconf = open("nagios/servers.csv", "r")
	vfile = open("Vagrantfile", "w")
	vfile.write('Vagrant.configure("2") do |config|\n')
	vfile.write('  config.vm.provision "shell", inline: "echo Hello"\n')
	for line in sconf:
		sg_name, s_name, s_ip, s_type = line.split(',')
		vmdefine = '  config.vm.define "%s" do |%s|\n'%(sg_name.strip(),sg_name.strip())
		vmbox = '    %s.vm.box = "%s"\n'%(sg_name.strip(),s_name.strip())	#You need to add the type of os that you load
		vmip = '    %s.vm.network "private_network", ip: "%s"\n'%(sg_name.strip(),s_ip.strip())
		vfile.write(vmdefine)
		vfile.write(vmbox)
		vfile.write(vmip)
		vfile.write('  end\n')
	vfile.write('end')
	vfile.close()
	sconf.close()
	return "Vagrantfile created"