from var_mod import var
import json
import cohere

co = cohere.Client('JovVsEhbD8cauTfCNsPh3CHGo8BhdUKhaF6j0Yln')

class emotionClassificationModel():
    def getECMresp(test_list):
        response = co.classify(
            model='54c4bd39-c594-45a4-a7ea-f8d43f8acdd3-ft',
            inputs=[x for x in test_list if x])

        return response.classifications

class textSummarizationModel():
    def getSummary(s):
        # s = 'As much as my pain is screaming at me to not do anything, I have to clean the house or it will just get worse.'
        response = co.generate(
            model='large',
            prompt=s+"\n--\nPassage: "+s+'\n\nTLDR:',
            max_tokens=50,
            temperature=0.8,
            k=0,
            p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop_sequences=["--"],
            return_likelihoods=None)

        pred = pred+(response.generations[0].text).strip()
        print (pred)
