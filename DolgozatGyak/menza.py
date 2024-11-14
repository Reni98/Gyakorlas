lista = []

with open("menza.txt", "r", encoding="UTF8") as fajl:
    sorok = fajl.readlines()

    for sor in sorok[1:]:
        sor = sor.strip()
        sor = sor.split(";")

        osztaly = sor[0]
        oszletszam=int(sor[1])
        honap = sor[2]
        ar = int(sor[3])
        kedvezmenyes= int(sor[4])

        lista.append([osztaly, oszletszam,honap,ar,kedvezmenyes])
befizetes_atlag = []
legtobbetfizeto_osztaly_osszege= 0
legtobbetfizeto_osztaly = None
idoszak = None
with open("befizetes.txt", "w", encoding="UTF8") as file:

    for item in lista:
    #print(f"{item[0]},{item[1]},{item[2]},{item[3]},{item[4]}")
    # osszeg = ((item[1]-item[4])*item[3] + (item[3]-(item[3]*0.3))*item[4])
    # print(f"{item[0]}, {round(osszeg)} Ft")
        teljesar= (item[1]-item[4])*item[3]
        kedvezmenyes = (item[3]-(item[3]*0.3))*item[4]
        if teljesar + kedvezmenyes> legtobbetfizeto_osztaly_osszege:
            legtobbetfizeto_osztaly_osszege= teljesar+kedvezmenyes
            legtobbetfizeto_osztaly = item[0]
            idoszak = item[2]
        befizetes_atlag.append(round(teljesar+kedvezmenyes))

        file.write(f"\nOsztály: {item[0]}, Teles áras befizetések: {round(teljesar)}, Kedvezményes befizetések: {round(kedvezmenyes)}, Összeg: {round(teljesar+kedvezmenyes)}")
    print(f"A legtöbbet fizető osztály: {legtobbetfizeto_osztaly}, {round(legtobbetfizeto_osztaly_osszege)} Ft, {idoszak}")

print(f"A befizetés átlaga: {round(sum(befizetes_atlag)/len(befizetes_atlag))} Ft")
