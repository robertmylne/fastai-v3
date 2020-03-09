import math
from decimal import *


def num_converter(num):
    decimals = 4
    multiplier = 10 ** decimals

    probability = math.floor(num * multiplier) / multiplier
    percentage = round(probability * 10 * 10, 2)

    return {
        'probability': '{:.2f}'.format(probability),
        'percentage': '{:.2%}'.format(percentage)
    }


def results(classes, classesDict, probabilities, remove_zeros=True, sort=True):

    results = [{
        'name': c, 
        'original': p.item(),
        'probability': num_converter(p.item())['probability'],
        'percentage': num_converter(p.item())['percentage']
        } for (c, p) in zip(classes, probabilities)]

    if remove_zeros:
        results = [result for result in results if not result['probability'] == 0.0]
    if sort:
        results = sorted(results, key=lambda result: result['probability'], reverse=True)

    return results