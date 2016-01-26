from afinn import Afinn

afinn = Afinn()

def score(text):
    return afinn.score(text)

def comparative(text):
    tokens = afinn.split(text)
    return score(text) / len(tokens)
