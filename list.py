x=int(input("banyaknya bilangan : "))
bilangan=[]
genap=[]
ganjil=[]
def bil(x):
    for i in range (x):
        y=int(input("masukan bilangan ke- {0} =".format(i)))
        bilangan.append(y)
    a=bilangan
    return a
def bilgen(bilangan):
    for i in range (len(bilangan)):
        if bilangan[i]%2==0:
            genap.append(bilangan[i])
    return genap
def bilgan(bilangan):
    for i in range (len(bilangan)):
        if bilangan[i]%2==1:
            ganjil.append(bilangan[i])
    return ganjil

print ("bilangan = ",bil(x))
print ("genap = ", bilgan(bilangan))
print ("ganjil = ", bilgan(bilangan))
