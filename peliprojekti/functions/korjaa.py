import time
from functions.lopeta_peli import lopeta_peli

def korjaa(pelaaja):
    esineiden_nimet = [esine.item_name for esine in pelaaja.player_items]
    current_location = pelaaja.player_location

    if current_location.room_name == "Katto":
        if "Jakoavain" in esineiden_nimet and "Aurinkokenno" in esineiden_nimet:
            print("\nKäytät jakoavainta ja asennat uuden aurinkokennon kattotasanteelle.")
            time.sleep(1)
            print("Aurinkopaneelit heräävät henkiin ja alkavat ladata tutkimusaseman akkuja.")
            time.sleep(3)
            print("Lämpötila alkaa nousta ja varovalot sammuvat.")
            print("\nONNEKSI OLKOON! Voitit pelin palauttamalla puhtaan aurinkoenergian!")
            lopeta_peli()
        else:
            print("Aurinkopaneelien korjaamiseen tarvitaan 'Jakoavain' ja 'Aurinkokenno'.")
    elif current_location.room_name == "Tuulikallio":
        if "Kiipeilyvaljaat" in esineiden_nimet and "Voiteluöljy" in esineiden_nimet:
            print("\nPuet kiipeilyvaljaat, kiipeät jäiselle tuulikalliolle ja voitelet tuuliturbiinin akselin!")
            time.sleep(1)
            print("Suuret lavat alkavat pyöriä kovassa tunturituulessa, ja aseman sähköverkko käynnistyy!")
            time.sleep(3)
            print("Lämpö palaa aseman pattereihin!")
            print("\nONNEKSI OLKOON! Voitit pelin käynnistämällä uusiutuvan tuulivoiman!")
            lopeta_peli()
        else:
            print("Tuulivoimalan huoltamiseen tarvitaan 'Kiipeilyvaljaat' ja 'Voiteluöljy'.")
    elif current_location.room_name == "Kellari":
        if "Venttiiliavain" in esineiden_nimet:
            print("\nSaavut maalämpökeskukseen venttiiliavaimen kanssa.")
            koodi = input("Aseta maalämpöpumpun oikea painelukema baareina (vihje: 100-200): ").strip()
            if koodi == "150":
                print("Käännät venttiiliä venttiiliavaimella lukemaan 150 bar!")
                time.sleep(1)
                print("Kuuma geoterminen höyry alkaa kiertää aseman lämmitysputkissa humisten!")
                time.sleep(3)
                print("Tukikohta on pelastettu jäätymiseltä!")
                print("\nONNEKSI OLKOON! Voitit pelin hyödyntämällä geotermistä maalämpöä!")
                lopeta_peli()
            else:
                print("Painelukema oli virheellinen, venttiili ei avaudu turvallisesti.")
        else:
            print("Maalämpöpumpun säätämiseen tarvitaan 'Venttiiliavain'.")
    else:
        print("Tässä huoneessa ei ole korjattavaa energiantuotantojärjestelmää.")
        print("Voit korjata laitteistoa Katolla (aurinko), Tuulikalliolla (tuuli) tai Kellarissa (maalämpö).")
