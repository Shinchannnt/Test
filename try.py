import inflect
p=inflect.engine()
lst=[]
while True:
    try:
        x=input("Input Name:")
        lst.append(x)
        res=p.join(lst)
        
    except EOFError:
        break
print("Me likes "+ res)


    
