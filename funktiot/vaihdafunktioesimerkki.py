def vaihda():
    kaupunki = "Vantaa"
    print("Funktiossa lopuksi: " + kaupunki)
    return

kaupunki = "Helsinki"
print("Pääohjelmassa aluksi: " + kaupunki)
vaihda()
print("Pääohjelmassa lopuksi: " + kaupunki)

# Tämä ei tee mitään koska kaupunki variable on paikallinen vaihda 
# funktion sisällä ja muuttuu vaan vaihda funktion sisällä, ei globaalisesti