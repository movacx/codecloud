personas = ["Mario", "Isaac", "Alberto","Sasha"]

print(personas)

personas.append("Cindi")

print(personas)

personas.remove("Alberto")

print(personas)

#Lo primero ubicar donde esta???
indice = personas.index("Cindi")

print(indice)

personas[indice] = "Cindy"

print(personas)