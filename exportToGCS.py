from google.cloud import storage
import json
import os
import var_mod

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/perudayani/Downloads/steam-glass-365615-d823e4ed9dfc.json"

# credentials to get access google cloud storage
# write your key path in place of gcloud_private_key.json
storage_client = storage.Client()

# write your bucket name in place of bucket1go
bucket_name = 'htv2022'
BUCKET = storage_client.get_bucket(bucket_name)

def create_json(json_object, filename):
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

# set the filename of your json object
if (var_mod.var == 0):
    filename = "audio-output/" + var_mod.rant[1][0:-4] + "Output.json"
else:
    filename = "audio-output/" + var_mod.adver[1][0:-4] + "Output.json"

# run the function and pass the json_object
with open("results.json") as json_file:
    data = json.load(json_file)
    print(create_json(data, filename))