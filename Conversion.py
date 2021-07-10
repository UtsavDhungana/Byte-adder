def intToBinaryConv(a,b):
    d = ""
    e = ""
    for i in range(8):
        d = str(a%2) + d
        a = int(a/2)
        e = str(b%2) + e
        b = int(b/2)

    return d,e
    
def binaryToIntConv(a):
    b = 1
    c = 0

    for i in range(len(a)-1,-1,-1):
        c = int(c + (int(a[i]))*b)
        b = b*2
    
    return (c)


