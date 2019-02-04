import boto3

__client__ = None

def s3_client(conf):
    global __client__
    if __client__ is None:
        session = boto3.session.Session()
        __client__ = session.client('s3',
                                region_name=conf['region_name'],
                                endpoint_url=conf['endpoint_url'],
                                aws_access_key_id=conf['aws_access_key_id'],
                                aws_secret_access_key=conf['aws_secret_access_key'])
    return __client__
