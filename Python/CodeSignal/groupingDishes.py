# input: [[dish1, ingredient1, ingredient2, ...]]
# dict: {ingredient1: [dish1, dish2, ...]}
# output: [[ingredient1, dish1, dish2, ...]]

def solution(dishes):
    d = dict() 
    for el in dishes:
        dish, ingredients = el[0], el[1:]
        for ing in ingredients:
            if ing in d.keys():
                d[ing].append(dish)
            else:
                d[ing]=[dish]
    recipe = []
    for key, vals in d.items():
        sorted_vals = sorted(vals)
        if len(vals) >= 2:
            recipe.append([key] + sorted_vals)
    recipe = sorted(recipe, key = lambda dish : dish[0])
    return recipe

"""
dishes = [["Salad", "Tomato", "Cucumber", "Salad", "Sauce"],
            ["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
            ["Quesadilla", "Chicken", "Cheese", "Sauce"],
            ["Sandwich", "Salad", "Bread", "Tomato", "Cheese"]]

solution(dishes) = [["Cheese", "Quesadilla", "Sandwich"],
                      ["Salad", "Salad", "Sandwich"],
                      ["Sauce", "Pizza", "Quesadilla", "Salad"],
                      ["Tomato", "Pizza", "Salad", "Sandwich"]]
"""    