from typing import Dict

# def add(elem1, elem2):
#     return elem1 + elem2


# val1 = add(1, 3)
# val2 = add(2.34, 12.35)
# val3 = add('hello', 'world')

# print(val1)  # 4
# print(val2)  # 14.69
# print(val3)  # helloworld

# def add(elem1: int, elem2: float) -> float:
#     return elem1 + elem2


# val1 = add(1, 3)
# val2 = add(2.34, 12.35)
# val3 = add('hello', 'world')

# print(val1)  # 4
# print(val2)  # 14.69
# print(val3)  # helloworld

# int, float, str, bool
# Dict, List, Tuple

def add(elem1: int, elem2: float) -> Dict:
    response = elem1 + elem2
    return {"sum": response}


val1 = add(2, 4.67)

print(val1)  # 6.67
