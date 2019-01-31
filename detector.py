import pickle as c
import os
from collections import Counter


def crear_log():
    f=open("registro.txt", "a+")
    return(f)
    

def load(clf_file):
    with open(clf_file, 'rb') as fp:
        clf = c.load(fp)
    return clf


def make_dict():
    direc = "emails/"
    files = os.listdir(direc)
    emails = [direc + email for email in files]
    words = []
    c = len(emails)

    for email in emails:
        f = open(email, encoding="latin-1")
        blob = f.read()
        words += blob.split(" ")
        print(c)
        c -= 1

    for i in range(len(words)):
        if not words[i].isalpha():
            words[i] = ""

    dictionary = Counter(words)
    del dictionary[""]
    return dictionary.most_common(3000)


clf = load("text-classifier.pkl")
d = make_dict()

f = crear_log()

while True:
    features = []
    inp = input(">")
    if inp is not "exit":
        f.write(inp+"\n\n")
    
    inp = inp.split()
    if inp[0] == "exit":
        f.close()
        break
    for word in d:
        features.append(inp.count(word[0]))
    res = clf.predict([features])
    f.write(["correo legitimo\n", "Correo basura!\n"][res[0]])
    print(["correo legitimo", "Correo basura!"][res[0]])
    f.write("\n")
    

    