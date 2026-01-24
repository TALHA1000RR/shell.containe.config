print( "\033c\033[40;37m\give the file .dat script to show ? ")
a=input()
f1=open(a,"r")
b=f1.read()
f1.close()
aa=b.encode()
c=str(aa)
c=c[2:]
c=c[:-1]
a=a.replace(".dat",".txt")
f1=open(a,"w")
f1.write(c)
f1.close()
