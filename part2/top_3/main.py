# Вам нужно написать функцию top3, 
# которая на вход принимает строку и 
# возвращает 3 наиболее повторяющихся элемента из входной строки. 
from collections import Counter

"""def top3(input_str):
    s = [x for x in input_str]
    s1 = sorted(list(map(lambda x: [x, s.count(x)], set(s))), reverse=True, key=lambda x: x[1])
    return sorted([x[0] for x in s1][:3])"""
"""def top3(input_str):
    s = [[x, input_str.count(x)] for y, x in enumerate(input_str) if input_str.index(x) == y]
    d = sorted(s, key=lambda x: x[1], reverse=True)
    return [v[0] for v in d][:3]"""

def top3(input_str):
    c = Counter(input_str)
    return sorted([x[0] for x in c][:3])


if __name__ == "__main__":
    print(top3('11111111222222223333333344444444555555'))
