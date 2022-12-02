woord = input("Geef een Woord:")
omdraaien = woord [::-1]
# b.v.b bij het woord apple zijn 5 letters, als 2:5: zou gegeven worden pakt die allen alle letters tussen de tweede en de vijfde,
# als een getal aan het einde staat (-1 in dit geval), dan pakt hij alleen de letters volgens die volgorde.
if woord == omdraaien: 
   print("Dit is een palindroom")
else:
   print("Dit woord is geen palindroom")

# Goed



# apple
# 12345
# (-) 54321
# 531 -2