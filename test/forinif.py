
its = [i for i in range(10) if i%2==0]
for k in its:
    print(k)

count = sum(1 for k in its)
print(f'count: {count}')