import os
import random

def removeWhitespace(string: str) -> str:
    return string.strip().capitalize()

def GetName() -> str:
        adjectives = open("names\\adjectives.txt", 'r')
        nouns = open("names\\words.txt", 'r')

        adjectiveList = adjectives.readlines()
        adjectiveList = list(map(removeWhitespace, adjectiveList))

        nounList = nouns.readlines()
        nounList = list(map(removeWhitespace, nounList))

        adjective = random.choice(adjectiveList)
        nouns =  random.sample(nounList, 3)

        return adjective+nouns[0]+nouns[1]+nouns[2]

