import json
import lib

if __name__ == '__main__':

    perceptrons = []

    with open("network.json", "r") as json_file:
        for line in json_file:
            perceptrons.append(json.loads(line, object_hook=lib.from_json))

    input= input("Podaj zdanie: ")

    for perceptron in perceptrons:
        if perceptron.process(lib.getData(input)):
            print(perceptron.type)
