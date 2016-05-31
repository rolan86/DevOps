sudo apt-get install wget apache2 apache2-utils php5 libapache2-mod-php5 build-essential libgd2-xpm-dev -y --force-yes
sudo service apache2 start
sudo useradd nagios
sudo echo -e "nagios\nnagios" | (sudo passwd nagios)
sudo groupadd nagcmd
sudo usermod -a -G nagcmd nagios
sudo usermod -a -G nagcmd www-data
sudo usermod -a -G nagios nagios
sudo usermod -a -G nagios www-data

cd /opt/
sudo wget https://assets.nagios.com/downloads/nagioscore/releases/nagios-4.1.1.tar.gz
sudo tar xzf nagios-4.1.1.tar.gz
cd nagios-4.1.1
sudo ./configure --with-command-group=nagcmd
sudo make all
sudo make install
sudo make install-init
sudo make install-config
sudo make install-commandmode

sudo cp ~/nagios.conf /etc/apache2/sites-available/
sudo ln -s /etc/apache2/sites-available/nagios.conf /etc/apache2/sites-enabled/
sudo cp ~/nagios.conf /etc/apache2/conf.d/
#sudo htpasswd -b -c /etc/nagios3/htpasswd.users nagiosadmin admin
#sudo htpasswd -b -c /etc/nagios3/htpasswd.users vagrant vagrant
sudo htpasswd -b -c /usr/local/nagios/etc/htpasswd.users nagiosadmin admin
#sudo htpasswd -b -c /usr/local/nagios/etc/htpasswd.users vagrant vagrant

sudo a2enconf nagios
sudo a2enmod cgi
sudo service apache2 restart

cd /opt
sudo wget http://www.nagios-plugins.org/download/nagios-plugins-2.1.1.tar.gz
sudo tar xzf nagios-plugins-2.1.1.tar.gz
cd nagios-plugins-2.1.1

sudo ./configure --with-nagios-user=nagios --with-nagios-group=nagios
sudo make
sudo make install

sudo mkdir -p /usr/local/nagios/var/spool/checkresults
sudo chmod 777 /usr/local/nagios/var/spool/checkresults
sudo /usr/local/nagios/bin/nagios -v /usr/local/nagios/etc/nagios.cfg
sudo service nagios start

sudo chmod 666 /usr/local/nagios/etc/nagios.cfg
sudo echo cfg_dir=/usr/local/nagios/etc/servers >> /usr/local/nagios/etc/nagios.cfg

sudo mkdir -p /usr/local/nagios/etc/servers

sudo a2enmod rewrite
sudo a2enmod cgi

sudo service nagios restart
sudo service apache2 restart