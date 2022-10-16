from google.cloud import storage
import json
import os
from var_mod import bucket_name, gac

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = gac

class exportGCS():
    def create_json(json_object, filename):
        # credentials to get access google cloud storage
        # write your key path in place of gcloud_private_key.json
        storage_client = storage.Client()

        # write your bucket name in place of bucket1go
    
        BUCKET = storage_client.get_bucket(bucket_name)
        '''
        this function will create json object in
        google cloud storage
        '''
        # create a blob
        blob = BUCKET.blob(filename)
        # upload the blob 
        blob.upload_from_string(
            data=json.dumps(json_object),
            content_type='application/json'
            )

        result = filename + ' upload complete'
        return {'response' : result}

