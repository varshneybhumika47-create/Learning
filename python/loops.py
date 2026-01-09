# loops

for i in range(10):
    print("My Name is Azure")

##

c = 1
for i in range(10):
    print(c)
    c = c + 1


#ques1-

n = 5
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

#ques2-

n = 5
for i in range(1,n+1):
    for j in range(i):
        print("*", end=" ")
    print()

#ques3-

n = 5
for i in range(n,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()

#ques13-

n = 5
for i in range(1,n+1):
    for j in range(i):
        print("*", end=" ")
    print()
for i in range(n-1,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()

#ques30-

n = 5

for i in range(n):
    for j in range(n,0,-1):
        print(j, end=" ")
    print()

