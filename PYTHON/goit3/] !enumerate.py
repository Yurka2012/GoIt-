#
# c, n, m = 1, 2, 3

# x = 'Hello World'
# for index, line in enumerate(x):
#     print(index, line)

    # index, line = (0, 'H')
a = [1, 2, 3, 4, 5]
b = [5,6,7,8,9,10]

# result = []
# for c, d in zip(a, b):
    # result.append(c * d)
# print(line)
# print(result)

# test = [
#     # 'test', 1,2,3, True
#     x for x in range(10)
#         ]
# print(test)
#
# m = a + b
# print(m)

# for l in a:
#     print()
#     for k in b:
#         print(f'l={l}, k={k}', end=" ")
    # break # будет одна строчка

f = []

for line in range(100):
    if line % 2 == 0:
        f.append(line)
        continue
    print('!!!!!!!!')

print(f)
