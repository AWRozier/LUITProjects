
#Import boto3
import boto3
from time import sleep

#List of EC2 instance IDs
Ids=['i-02a84095bc7d5b130','i-02a3ead29f60f1e98','i-0d5874bcb675e66bf']

#Resource variable setting
ec2 = boto3.resource("ec2")

#Instance termination
x = ec2.instances.filter(InstanceIds=Ids).stop()

#Display in terminal
print("Stopping Instances.Congrats!...")
sleep(10)
print(x)