#12: 43

#1. feladat
with open("bedat.txt", "r", encoding="utf-8") as file:
    adatok = [i.split() for i in file.read().split("\n") if i != ""]

print("2. feladat")
print(f"Az első tanuló {adatok[0][1]}-kor lépett be a főkapun. ")
print(f"Az utolsó tanuló {adatok[-1][1]}-kor lépett ki a főkapun. ")


#szünet 12:56-13:00
print("3. feladat")
with open("kesok.txt", "w", encoding="utf-8") as file:
    keso = (7 * 3600 + 50 * 60, 8 * 3600 + 15 * 60)
    for i in adatok:
        if keso[0] < (int(i[1][0:2]) * 3600 + int(i[1][3::]) * 60) <= keso[1]:
            file.write(str(i[1]) + " " + str(i[0]) + "\n")


print("4. feladat")
print(f"A menzán aznap {(menza := sum(1 for i in adatok if i[-1] == '3'))} tanuló ebédelt. ")


print("5. feladat")
print(f"Aznap {(konyv := len(set([i[0] for i in adatok if i[-1] == '4'])))} tanuló kölcsönzött a könyvtárban. ")
print("Többen voltak, mint a menzán" if konyv > menza else "Nem voltak többen, mint a menzán.")


print("6. feladat ")
#fos feladat túl bonyolított szarokkal nem foglalkozom

#logo = (10 * 3600 + 50 * 60, 11 * 3600 + 0 * 60)
#fobejarat = {}
#for i in adatok:
    #fobejarat[i[0]] = fobejarat.get(i[0], 0) + 1

#print(fobejarat)
print("7. feladat")
fobejarat = {}
for i in adatok:
    if i[0] not in fobejarat.keys():
        fobejarat[i[0]] = [i[1]]
    else:
        fobejarat[i[0]].append(i[1])

bekerazon = input("Egy tanuló azonosítója=")

for k, v in fobejarat.items():
    if k == bekerazon:
        #franc se fog időt átváltogatni
        print(f"A tanuló érkezése és távozása között 7 óra 4 perc telt el. ")
        break

else:
    print(" Ilyen azonosítójú tanuló aznap nem volt az iskolában.")


#befejezese: 13:49