# python3

def parallel_processing(n, m, data):
    output = []
    ft=[0]*n
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    for i in range(m):
        t=0
        for j in range(n):
            if ft[j]< ft[t]:
                t=j
        output.append((t,ft[t]))
        ft[t]= data[i]+ft[t]
        

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n,m = map(int, input().split())
    #print(n)
    #print(m)

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int,input().split()))
    #print(data)

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for i,j in result:
        print(i,j)



if __name__ == "__main__":
    main()
