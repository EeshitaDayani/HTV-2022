import json
import os
from var_mod import bucket_name, rant, adver, gac, var, emotions
from googleCloudSpeechRec import SpeechRec
from helper import Helper
from model import emotionClassificationModel as ecm 

# set google api creds
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = gac

# set the filename of your json object
if (var == 0):
    gcs_uri = "gs://htv2022/audio-files/" + rant[1]
    filename = rant[1][0:-4] + "Output.json"
else:
    gcs_uri = "gs://htv2022/audio-files/" + adver[1]
    filename = adver[1][0:-4] + "Output.json"

# makes the results.json file
SpeechRec.transcribe_file(gcs_uri)

# use json_object to send copy to GCS bucket
with open("results.json") as results:
    test_list  = json.load(results)
    responses = ecm.makeCSVs(test_list)
    label_lists = Helper.make_label_lists(responses)
    Helper.make_graph(label_lists)

print('Finished!')


