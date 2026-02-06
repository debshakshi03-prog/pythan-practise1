primes=[]
for i in range(2, 21):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
            primes.append(i)

for i in range(0,len(primes),2):
    print(primes[i],end="  ")



