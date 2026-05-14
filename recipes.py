import math

def cakes(recipe, available):
    checked_ing = [available[ing] / recipe[ing] if ing in available else 0 for ing in recipe]
    cakes = min(checked_ing)
    return math.floor(cakes)


if __name__ == '__main__':
    recipe = {
        "flour": 500,
        "sugar": 200,
        "eggs": 1
    }
    available = {
        "flour": 1200,
        "sugar": 1200,
        "eggs": 5,
        "milk": 200
    }
    print(cakes(recipe, available))
