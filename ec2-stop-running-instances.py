import _json

import pprint
import json
import boto3
from aws_access import aws_account

from pprint import pprint

access_key = aws_account["access_key_id"]
secret_key = aws_account["secret_access_key"]
pprint("access key : " + access_key)
pprint("secret key : " + secret_key)
region = 'us-east-1'
ec2 = boto3.client('ec2', aws_secret_access_key=secret_key, aws_access_key_id=access_key, region_name=region)

instances = ec2.describe_instance_status(
    Filters=[
        {'Name': 'instance-state-name', 'Values': ['running']},
        {
            'Name': 'vpc-id',
            'Values': ['vpc-62ec191b']
        }
    ])
pprint("instances id is  : " + str(instances['InstanceStatuses'][0]))


for instance in instances['InstanceStatuses']:
    pprint("print instance : " + str(instance['InstanceId']))
    '''print("Instance information :" + str(instances['InstanceStatuses'][i]['InstanceId']))'''


"""
for instance in instances:
    print("Instance information :" + str(instance['Reservations'][0]))

"""
'''
# following should be valid instance id
instances = ['i-0750283d8daa4874c']

status = ec2.describe_instances(InstanceIds=instances)
pprint("Current status of Instance is : " + str(status['Reservations'][0]['Instances'][0]['State']['Name']))
pprint("Instance Name is  : " + str(status['Reservations'][0]['Instances'][0]['Tags'][0]['Value']))


#check whether instance is running, if running shut down
if status['Reservations'][0]['Instances'][0]['State']['Name'] == "running":
    ec2.stop_instances(InstanceIds=instances)
    pprint("Instance " + status['Reservations'][0]['Instances'][0]['Tags'][0]['Value'] + " is shutting down")

elif status['Reservations'][0]['Instances'][0]['State']['Name'] == "stopped":
    ec2.start_instances(InstanceIds=instances)
    pprint("Instance " + status['Reservations'][0]['Instances'][0]['Tags'][0]['Value'] + " is starting")
else:
    pprint("Instance is terminated/pending")


'''