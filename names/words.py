import uuid
import random

def removeWhitespace(string: str) -> str:
    return string.strip().capitalize()

def GetName() -> str:
    try:
        adjectives = open("names\\adjectivses.txt", 'r')
        nouns = open("names\\words.txt", 'r')

        adjectiveList = adjectives.readlines()
        adjectiveList = list(map(removeWhitespace, adjectiveList))

        nounList = nouns.readlines()
        nounList = list(map(removeWhitespace, nounList))

        adjective = random.choice(adjectiveList)
        nouns =  random.sample(nounList, 3)

        return adjective+nouns[0]+nouns[1]+nouns[2]
    except FileNotFoundError:
        print("No se encontraron los archivos con nombres, se utilizarán GUIDs")
        return str(uuid.uuid4())


