dx = 0.001
valuesdf=[]

for i in range(0,10,1):
    f = i**2
    df = ((i+dx)**2-i**2)/(dx)
    valuesdf.append(df)
print(valuesdf)