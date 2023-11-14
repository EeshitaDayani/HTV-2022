import json
import os
from python_scripts.var_mod import shriya, adver, gac, var
from python_scripts.googleCloudSpeechRec import SpeechRec
from python_scripts.helper import Helper
from python_scripts.models import emotionClassificationModel as ecm 
# from models import textSummarizationModel as tsm
import cohere
co = cohere.Client('JovVsEhbD8cauTfCNsPh3CHGo8BhdUKhaF6j0Yln')

def getSummary(s):
    # s = 'As much as my pain is screaming at me to not do anything, I have to clean the house or it will just get worse.'
    response = co.generate(
        model='1bccf295-9d16-437e-bccf-c182990f5d45-ft',
        prompt=s,
        num_generations=1,
        max_tokens=len(s)//2,
        temperature=0.3,
        k=15,
        p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop_sequences=[],
        return_likelihoods='NONE')

    resp = response.generations[0].text
    split = resp.split('\n')
    print(split[2])

# set google api creds
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = gac

# set the filename of your json object
if (var == 0):
    gcs_uri = "gs://htv2022/audio-files/" + shriya[1]
    filename = shriya[1][0:-4] + "Output.json"
else:
    gcs_uri = "gs://htv2022/audio-files/" + adver[1]
    filename = adver[1][0:-4] + "Output.json"

# makes the results.json file
SpeechRec.transcribe_file(gcs_uri)

# use json_object to send copy to GCS bucket
with open("results.json") as results:
    test_list  = json.load(results)
    responses = ecm.getECMresp(test_list)
    print("Building graph")
    para = " ".join(test_list)
    summary = getSummary(para)
    label_lists = Helper.make_label_lists(responses)
    print("Completed")
    Helper.make_graph(label_lists)

print('Finished!')


