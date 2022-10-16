from datasets import load_dataset
import cohere
from cohere.classify import Example
import json

class emotionClassificationModel():
    dataset = load_dataset('emotion','binary')
    emotions = ["sadness", "joy", "love", "anger", "fear", "surprise"]
    emotion_test = load_dataset('emotion', 'binary', split='test')
    # Access GC file
    # Read JSON - check if list appears as is, else parse
    def getTestList(emotion_test):
        with open("rantOutput.json", "r") as j:  
            test_list = json.loads(j.read())
        for row in emotion_test:
            test_list.append(row['text'])

    def makeCSVs(test_list, dataset):
        co = cohere.Client('JovVsEhbD8cauTfCNsPh3CHGo8BhdUKhaF6j0Yln')
        response = co.classify(
        model='54c4bd39-c594-45a4-a7ea-f8d43f8acdd3-ft',
        inputs=test_list[:100])
        #print('The confidence levels of the labels are: {}'.format(response.classifications))

        for split, data in dataset.items():
            data.to_csv(f"my-dataset-{split}.csv", index = None)