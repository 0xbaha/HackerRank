if __name__ == '__main__':
    a = [] # List for input
    for _ in range(int(input())):
        name = input()
        score = float(input())
        a.append([score, name])

    # Sort the input list
    a.sort()

    # Remove lowest
    b = [i for i in a if i[0] != a[0][0]] 
    
    # Only take the second lowest
    c = [j for j in b if j[0] == b[0][0]] 

    # Sort by name
    c.sort(key=lambda x: x[1]) 
    
    # Print output
    for i in range(len(c)):
        print(c[i][1]) 
    