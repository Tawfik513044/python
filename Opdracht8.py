fibonacci = int(input("hoeveel sequences wilt u zien?:"))
nummer1, nummer2 = 0, 1
begin = 0

if fibonacci <=0:
    print("voer in hoeveel fibbonaci code je wilt zien")
elif fibonacci == 1:
     print ("fibbonacci code tot ", fibonacci, ":")
     print(nummer1)
else:
   print("Fibonacci sequence:")
   while  begin < fibonacci:
       print(nummer1)
       cijfercombo = nummer1 + nummer2
       nummer1 = nummer2
       nummer2 = cijfercombo
       begin += 1
