import math


def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier


def to_percentage(decimal_number):
  return f"{decimal_number * 10 * 10}%"


def result(classesDict, prediction):
    return {
        'id': str(prediction),
        'name': classesDict[str(prediction)]
    }


def probabilites(classes, classesDict, probs, remove_zeros=True, sort=True, to_dict=False):
    probs = [(c, round_down(p.item(), 4)) for (c, p) in zip(classes, probs)]
    if remove_zeros:
        probs = [(name, value) for (name, value) in probs if not value == 0.0]
        print(probs)
    if sort:
        probs = sorted(probs, key=lambda x: x[1], reverse=True)
        print(probs)
    if to_dict:
        probs = [{'id': name, 'name': classesDict[name], 'value': value} for (name, value) in probs]

    return probs


def percentages(classes, classesDict, probs, to_dict=False):
    probs = probabilites(classes, classesDict, probs)
    percentages = [(name, to_percentage(probability)) for (name, probability) in probs]
    if to_dict:
        percentages = [{'id': name, 'name': classesDict[name], 'value': value} for (name, value) in percentages]

    return percentages


