import random
dp=list(map(int, input("Enter the values").split()))
k=int(input("Enter no of cluster "))
mean=[(random.randint(0, max(dp))) for _ in range(k)]

while True:
    near=list()
    cluster=[list() for _ in range(k)]
    for m in mean:
        near.append([abs(point-m) for point in dp])
    for i in range(len(dp)):
        calc=[near[j][i] for j in range(k)]
        belongs=calc.index(min(calc))
        cluster[belongs].append(dp[i])

    nm=list()
    for cl in cluster:
        try:
            nm.append(sum(cl)/len(cl))
        except:
            nm.append(0) 
    if nm==mean:
        break
    mean=nm                   
print("Required Cluster are: ")
for i in range(k):
    print(f"Cluster {i+1}: ",end="")
    print(*cluster[i])    