from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
#九九乘法表
def multiplication_table(m, n):
    print ('\n'.join(['\t'.join(['{}*{}={}'.format(i,j,i*j) for i in range(m,n+1)]) for j in range(1,10)]))

def pyramid(n):
    for i in range(1,n+1):
        s=" "*(n-i)+"*"*(2*i-1)
        print(s)
