# -*- coding: utf-8 -*-
class Perceptron:
    def __init__(self, l, t):
        self.type = t
        self.o = 1.0
        self.w = [0.0]*(l-1)

    def __json__(self):
        return {'type':self.type, 'o':self.o, 'w':self.w}

    def process(self, arr, expected = None):
        sum = 0.0
        for i in range(0,len(arr)-1):
            sum += float(arr[i])*self.w[i]
        y = sum > self.o
        if expected:
            d = (expected == self.type)
            for i in range(0,len(self.w)):
                self.w[i] = self.w[i] + (d - y)*float(arr[i])*0.01
            self.o -= (d - y)*0.01
        return y

def from_json(jObject):
    if "type" in jObject and "o" in jObject and 'w' in jObject:
        perceptron = Perceptron(26, jObject["type"])
        perceptron.o = float(jObject["o"])
        for i in range(len(jObject["w"])):
            perceptron.w[i]=float(jObject["w"][i])
        return perceptron
    return jObject

def getData(text):
    text = text.lower()
    text = str(text).replace('ą', 'a')
    text = str(text).replace('å', 'a')
    text = str(text).replace('ä', 'a')
    text = str(text).replace('â', 'a')
    text = str(text).replace('î', 'i')
    text = str(text).replace('ę', 'e')
    text = str(text).replace('é', 'e')
    text = str(text).replace('ó', 'o')
    text = str(text).replace('ö', 'o')
    text = str(text).replace('ć', 'c')
    text = str(text).replace('ś', 's')
    text = str(text).replace('ż', 'z')
    text = str(text).replace('ź', 'z')
    text = str(text).replace('ł', 'l')
    data = [0]*26
    text = str(text).upper()
    for i in range(0,26):
        data[i] = str(text).count(chr(65+i))/len(text)
    return data