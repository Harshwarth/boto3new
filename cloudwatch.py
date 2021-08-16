import boto3
from datetime import datetime, timedelta
client = boto3.client('cloudwatch')
response = client.get_metric_statistics(
    Namespace='AWS/EC2',
    MetricName='CPUUtilization',
    Dimensions=[{'Name': 'InstanceId','Value': 'i-036105dc9f567f625'}],
    StartTime=datetime.utcnow() - timedelta(minutes=10),
    EndTime=datetime.utcnow(),
    Period=60,
    Statistics=['Average'],
    Unit='Percent'
    )
for cpu in response['Datapoints']:
    print(cpu)