import boto3
def create_ec2():
    try:
        resource_ec2 = boto3.client("ec2")
        resource_ec2.run_instances(
            ImageId="ami-04db49c0fb2215364",
            MinCount=1,
            MaxCount=1,
            InstanceType="t2.micro",
            KeyName="mumbaiEC2"
        )
    except Exception as e:
        print(e)
def terminate_ec2():
    try:
        resource_ec2=boto3.client("ec2")
        resource_ec2.terminate_instances(InstanceIds=['i-0f61b70eadf45f8c3'])
    except Exception as e:
        print(e)
#create_ec2()
terminate_ec2()