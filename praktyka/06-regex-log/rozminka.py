import sys

sys.stdout.reconfigure(encoding="utf-8")

with open("data/words.txt", encoding="utf-8") as f:
    for ryadok in f:
        print(ryadok.rstrip().upper())

suma = 0.0
kilkist = 0
with open("data/mbox-short.txt", encoding="utf-8") as f:
    for ryadok in f:
        if ryadok.startswith("X-DSPAM-Confidence:"):
            suma += float(ryadok.split(":")[1])
            kilkist += 1

print()
print(f"Рядків: {kilkist}, середнє: {suma / kilkist}")
