import botocore
import boto3
import datetime

def lambda_handler(event, context):
    print("Starting Lambda function...")

    try:
        client = boto3.client('ec2')
        snaps = client.describe_snapshots(OwnerIds=['self'])['Snapshots']
    except botocore.exceptions.ClientError as error:
        print(f"ERROR: {error.response['Error']['Code']} - {error.response['Error']['Message']}")
        raise error

    print(f"Found {len(snaps)} snapshots")   
    for snap in snaps:
        snap_id = snap['SnapshotId']
        snap_date = snap['StartTime']
        now = datetime.datetime.now()
        age = (now - snap_date).days
        if age > 365:
            # delete the snapshot
            print(f"Deleting snapshot {snap_id}...")
            try:
                client.delete_snapshot(SnapshotId=snap_id)
            except botocore.exceptions.ClientError as error:
                print(f"ERROR: {error.response['Error']['Code']} - {error.response['Error']['Message']}")
                raise error

    print("Lambda function completed.")
    return {
        'statusCode': 200,
        'body': 'Lambda function completed.'
    }