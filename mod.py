from collections import defaultdict


dict = defaultdict(int)

fq = set()

for i in range(1, 11):
    if i % 3 == 0:
        dict[3] += 1
        fq.add(i)


print(dict)
print(fq)




if __name__ == "__main__": 
    pass
