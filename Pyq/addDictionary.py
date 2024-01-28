d1 = {'a': 10, 'b': 20, 'c': 20}
d2 = {'a': 30, 'b': 20, 'c': 40}
d3 = {}  # for the result

for keyd1, valued1 in d1.items():
    for keyd2, valued2 in d2.items():
        if keyd1 == keyd2:
            d3[keyd1] = valued1 + valued2

print(d3)

            
