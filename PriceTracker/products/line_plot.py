# import matplotlib
import matplotlib.pyplot as plt
# import numpy as np
import json
import os


def plot(username):
    direc = os.getcwd()
    filepath = direc + str("/json_files/" + username)

    f = open(filepath)
    data = json.load(f)

    websites = data["website"]
    prices = list()
    for website in websites.keys():
        for value in websites[website]:
            prices.append(value)

    time = data["datetime"]
    timee = [str(i)[5:10] + " " + str(i)[11:16] for i in time]
    fig, ax = plt.subplots()
    ax.plot(timee, prices)

    ax.set(xlabel='time', ylabel='Price is Rs',
           title='Price Comparison')
    ax.grid()

    fig.savefig(dir + "/plots/" + "test.png")
