for i in range(1, 10):
    for j in range (1, i+1):
        k = i * j
        print ('%d x %d = %d' %(j,i,k), end="  ")
    print()