import json
import matplotlib.pyplot as plt
import numpy as np
from python_scripts.var_mod import emotions

class Helper():
    def make_resp_json(results):
        temp_rows=[]
        for res in results:
            temp_rows.append(res.alternatives[0].transcript.split('.'))
        
        rows = sum(temp_rows, [])
        with open("results.json", "w+") as file:
            json.dump(rows, file)
        
        print("Completed")

    def make_output_json(data, filename):
        with open(filename, "w+") as file:
            json.dump(data, file)

    def make_label_lists(responses):
        zeroList, oneList, twoList, threeList, fourList, fiveList = [], [], [], [], [], []
        for res in responses:
            zeroList.append(res.labels['0'].confidence)
            oneList.append(res.labels['1'].confidence)
            twoList.append(res.labels['2'].confidence)
            threeList.append(res.labels['3'].confidence)
            fourList.append(res.labels['4'].confidence)
            fiveList.append(res.labels['5'].confidence)

        return [np.array(zeroList), np.array(oneList), np.array(twoList), np.array(threeList), np.array(fourList), np.array(fiveList)]
    
    def make_graph(ll):
        x = np.arange(0, len(ll[0]))
        plt.plot(x, ll[0])
        plt.plot(x, ll[1])
        plt.plot(x, ll[2])
        plt.plot(x, ll[3])
        plt.plot(x, ll[4])
        plt.plot(x, ll[5])

        plt.legend(emotions, bbox_to_anchor=(0, 0), loc='upper right')
        plt.show()