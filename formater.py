# -*- coding: utf-8 -*-

import os
import json
import lib

if __name__ == '__main__':
    perceptrons = []
    data = {}

    for dir in os.listdir('Data/'):
        perceptrons.append(lib.Perceptron(26, dir))
        data[dir] = []

        for file in os.listdir(os.path.join('Data/', dir)):
            text = open(os.path.join('Data/', dir, file), 'r').read()
            data[dir].append(lib.getData(text))

    for i in range(1000):
        for j in range(len(perceptrons)):
            for language in data:
                for arr in data[language]:
                    perceptrons[j].process(arr, language)

    with open("network.json", "w") as json_file:
        for perceptron in perceptrons:
                json.dump(perceptron, json_file, default=lambda x: x.__json__())