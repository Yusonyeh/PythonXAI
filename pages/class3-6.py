D1 = {}
D2 = {"A": 90, "B": 80, "C": 70, "D": 60}
print(D1)
print(D2)
print(D2["A"])
print(D2["C"])

print("-" * 30)

D3 = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
for key in D3:
    print(key)

print(D3.keys())
for key in D3.keys():
    print(key)

print(D3.values())
for value in D3.values():
    print(value)

print(D3.items())
for key, value in D3.items():
    print(f"key: {key}, value: {value}")

D3 = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
D3["f"] = 6
print(D3)
D3["a"] = 10
print(D3)

print("-" * 30)

D3 = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
D3.pop("c")
print(D3)
popValue = D3.pop("f", "error: key not found")
print(popValue)
print(D3)

print("-" * 30)

print(len({}))
print(len({"apple": "蘋果"}))
print(len({"a": 1, "b": 2, "c": 3}))

print("-" * 30)
D3 = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
print("d" in D3)
print("f" in D3)
print(2 in D3)

print("-" * 30)

L1 = [1, 2, 3, 4, 5]
print(4 in L1)
print(6 in L1)

print("-" * 30)

import random

scores = {"國文": [], "英文": [], "數學": [], "自然": [], "社會": []}
for key in scores:
    for i in range(10):
        scores[key].append(random.randint(0, 100))
print("計算各科平均分數:")
for key in scores:
    total = 0
    for score in scores[key]:
        total += score
    avg = total / 10
    print(f"{key} 平均分數: {avg}")
