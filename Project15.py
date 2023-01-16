"""
Project 15
"""
#Create a Standard SQS Queue using Python

import boto3

# Obtain the service resource
sqs = boto3.resource('sqs')

# Queue will be created & output will returns an SQS Queue instance
queue = sqs.create_queue(QueueName='Lex')

print(queue.url)

