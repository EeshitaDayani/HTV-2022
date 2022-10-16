import json
import os
from var_mod import rant, adver, gac, var
from googleCloudSpeechRec import SpeechRec
from helper import Helper
from models import emotionClassificationModel as ecm 
# from models import textSummarizationModel as tsm
import cohere
co = cohere.Client('JovVsEhbD8cauTfCNsPh3CHGo8BhdUKhaF6j0Yln')

def getSummary(s):
        # s = 'As much as my pain is screaming at me to not do anything, I have to clean the house or it will just get worse.'
        response = co.generate(
            model='1bccf295-9d16-437e-bccf-c182990f5d45-ft',
            prompt=s,
            max_tokens=len(s)//2,
            temperature=0.3,
            k=15,
            p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop_sequences=[],
            return_likelihoods=None)

        resp = response.generations[0].text
        split = resp.split('\n')
        print("summary:")
        print (split[1])

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
    responses = ecm.getECMresp(test_list)
    label_lists = Helper.make_label_lists(responses)
    para = " ".join(test_list)
    summary = getSummary(para)
    Helper.make_graph(label_lists)

print('Finished!')


