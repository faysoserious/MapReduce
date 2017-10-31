filename = 'eulerGraphs.txt'
with open(filename,'r') as graphs:
    done = 0
    i = 1
    j = 1
    base =''
    eachgraph = 0
    while not done:
        aLine = graphs.readline()
        if (aLine !=''):
            if(j==1):
                j =j+1
            elif((aLine != '\n')&(j!=1)):
                aLine = base+aLine
                with open('graph{}.txt'.format(i),'a+') as output:
                    print(aLine,file=output)
                    j=j+1
            else:
                i=i+1
                j=1
        else:
            done = 1
