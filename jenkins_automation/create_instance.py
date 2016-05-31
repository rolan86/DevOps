import boto.ec2
from boto.ec2 import EC2Connection

ACCESS_KEY = 'AKIAJSTSRLGGLFT3PALQ'
SECRET_KEY = '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'
region = "us-west-2"
#ec2conn = ec2.connection.EC2Connection(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
conn = boto.connect_ec2( ACCESS_KEY, SECRET_KEY, region=region )
#conn = boto.ec2.connect_to_region("us-west-2")
reservation = conn.run_instances(
						'ami-9abea4fb',
						key_name='key-test',
						instance_type='t2.micro',
						security_groups=['all_traffic']
				)