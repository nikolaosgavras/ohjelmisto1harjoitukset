username = "python"
password = "rules"

counter = 0

while True:
    usernameInput = input("Syötä käyttäjänimi: ")
    passwordInput = input("Syötä salasana: ")
    if usernameInput != username or passwordInput != password:
        print("Väärä käyttäjänimi tai salasana")
        counter += 1
        if counter == 5:
            print("Pääsy evätty")
            break
        continue
    if usernameInput == username or passwordInput == password:
        print('Tervetuloa takaisin "' + usernameInput + '"' + "!")
        break
