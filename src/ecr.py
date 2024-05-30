import boto3

# creating an AWS ECR repository
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#ECR.Client.create_repository

ecr_client = boto3.client('ecr', region_name='us-west-2')
repository_name = "my-devops-repo"
response = ecr_client.create_repository(repositoryName=repository_name)
repository_uri = response['repository']['repositoryUri']
print(f'Repository URI: {repository_uri}')
