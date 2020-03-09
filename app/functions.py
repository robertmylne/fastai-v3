import math


def round_down(n, decimals=0):
    multiplier = 10 ** decimals

    return math.floor(n * multiplier) / multiplier


def to_percentage(decimal_number):

  return f"{decimal_number * 10 * 10}%"


def results(classes, classesDict, probabilities, remove_zeros=True, sort=True):

    results = [{
        'name': c, 
        'probability': round_down(p.item(), 4),
        'percentage': to_percentage(round_down(p.item(), 4))
        } for (c, p) in zip(classes, probabilities)]

    if remove_zeros:
        results = [result for result in results if not result['probability'] == 0.0]
    if sort:
        results = sorted(results, key=lambda result: result['probability'], reverse=True)

    return results