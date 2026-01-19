# for row in range(1,6):
#     for col in range(5,0,-1):
#         if (row<col):
#             print(' ', end=" ")
#         else:
#             print('*', end=" ")
#     print()

for row in range(1,6):
    for col in range(1,6):
        if (row>col):
           print(' ', end=" ")
        else:
           print('*', end=" ")
    print()

