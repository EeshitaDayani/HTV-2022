from var_mod import var
import json
import cohere

co = cohere.Client('JovVsEhbD8cauTfCNsPh3CHGo8BhdUKhaF6j0Yln')

class emotionClassificationModel():
    def getECMresp(test_list):
        response = co.classify(
            model='54c4bd39-c594-45a4-a7ea-f8d43f8acdd3-ft',
            inputs=test_list[:100])

        return response.classifications

class textSummarizationModel():
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
        print (split[1])
