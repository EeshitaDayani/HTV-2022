from var_mod import var
import json
import cohere

class emotionClassificationModel():
    def makeCSVs(test_list):
        co = cohere.Client('JovVsEhbD8cauTfCNsPh3CHGo8BhdUKhaF6j0Yln')
        response = co.classify(
            model='54c4bd39-c594-45a4-a7ea-f8d43f8acdd3-ft',
            inputs=test_list[:100])

        return response.classifications