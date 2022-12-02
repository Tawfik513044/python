def add(x, y): 
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Select operation.")
print("1.optellen")
print("2.aftrekken")
print("3.vermeenigvuldigen")
print("4.delen")

while True:
   
    choice = input("maak een keuze(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("voer het eerste getal in: "))
        num2 = float(input("voer het tweede getal in: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
       
        next_calculation = input("zullen we de volgende berekening maken (ja/nee): ")
        if next_calculation == "nee":
          break
    else:
        print("syntax error")

# b.v.b bij het woord apple zijn 5 letters, als 2:5: zou gegeven worden pakt die allen alle letters tussen de tweede en de vijfde,
# als een getal aan het einde staat (-1 in dit geval), dan pakt hij alleen de letters volgens die volgorde.