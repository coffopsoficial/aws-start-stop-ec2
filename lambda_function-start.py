import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    ec2.start_instances(InstanceIds=['YOUR-INSTANCE-ID'])
