sudo apt-get install wget apache2 apache2-utils php5 libapache2-mod-php5 build-essential libgd2-xpm-dev curl -y --force-yes
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
sudo ./configure --with-nagios-group=nagios --with-command-group=nagcmd 
sudo make all
sudo make install
sudo make install-commandmode
sudo make install-init
sudo make install-config
sudo /usr/bin/install -c -m 644 sample-config/httpd.conf /etc/apache2/sites-available/nagios.conf
sudo ln -s /etc/apache2/sites-available/nagios.conf /etc/apache2/sites-enabled/

sudo htpasswd -b -c /usr/local/nagios/etc/htpasswd.users nagiosadmin admin

sudo a2enconf nagios
sudo a2enmod cgi
sudo service apache2 restart

cd /opt
sudo wget http://www.nagios-plugins.org/download/nagios-plugins-2.1.1.tar.gz
sudo tar xzf nagios-plugins-2.1.1.tar.gz
cd nagios-plugins-2.1.1

sudo ./configure --with-nagios-user=nagios --with-nagios-group=nagios --with-openssl
sudo make
sudo make install

sudo mkdir -p /usr/local/nagios/var/spool/checkresults
sudo chmod 777 /usr/local/nagios/var/spool/checkresults
#sudo /usr/local/nagios/bin/nagios -v /usr/local/nagios/etc/nagios.cfg
#sudo service nagios start

sudo chmod 666 /usr/local/nagios/etc/nagios.cfg
sudo echo cfg_dir=/usr/local/nagios/etc/servers >> /usr/local/nagios/etc/nagios.cfg

sudo mkdir -p /usr/local/nagios/etc/servers

cd ~
sudo curl -L -O http://downloads.sourceforge.net/project/nagios/nrpe-2.x/nrpe-2.15/nrpe-2.15.tar.gz
sudo tar xvf nrpe-*.tar.gz
cd nrpe-*
sudo ./configure --enable-command-args --with-nagios-user=nagios --with-nagios-group=nagios --with-ssl=/usr/bin/openssl --with-ssl-lib=/usr/lib/x86_64-linux-gnu
sudo make all
sudo make install
sudo make install-xinetd
sudo make install-daemon-config
sudo service xinetd restart
sudo ln -s /etc/init.d/nagios /etc/rcS.d/S99nagios

sudo a2enmod rewrite
sudo a2enmod cgi

sudo service nagios restart
sudo service apache2 restart