#!/usr/bin/python
from paramiko import SSHClient

import paramiko
import time


def ssh_client():
    """
        Create ssh client
    """
    client = SSHClient()
    return client

def comm_exec(client, host, user, passwd, comm):
    """
        Add host keys, connect via ssh, execute commands
    """

    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.load_system_host_keys()
    client.connect(host, username=user, password=passwd)
    stdin, stdout, stderr = client.exec_command(comm)
    return stdin, stdout, stderr

def parse_info(data):
    """
        Parse the information from command executed,
        Perform operations on parsed info.
    """
    return data.readlines()

def ptrans(host, user, passwd):
    """
        This module is used to perform SFTP
    """
    t = paramiko.Transport((host,22))
    t.connect(username=user, password=passwd)
    sftp = paramiko.SFTPClient.from_transport(t)
    return sftp

def sftp_put(sftp, src, dest):
    """
        This will put you data on remote server
    """
    sftp.put(src, dest)
    return "Transfer Complete"

def ssh_close(client):
	client.close()
	return 0
	
def sftp_close(sftp):
	sftp.close()
	return 0