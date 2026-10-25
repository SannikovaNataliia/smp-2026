# Розбір журналу сервера data/access.log іменованими групами.
# Запуск з кореня репозиторію: python praktyka/06-regex-log/log-parser.py
import re
import sys
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")

shablon = re.compile(
    r'^(?P<ip>\d{1,3}(?:\.\d{1,3}){3}) '            # IP на початку рядка
    r'.*?\[(?P<chas>[^\]]+)\] '                      # час у квадратних дужках
    r'"(?P<metod>[A-Z]+) (?P<shliakh>\S+)[^"]*" '    # метод і шлях; протокол пропускаємо
    r'(?P<kod>\d{3}) '                               # код відповіді — рівно три цифри
)

rozibrano = 0
propushcheno = 0
ip = Counter()
kody = Counter()
pomylky_5xx = []

with open("data/access.log", encoding="utf-8") as f:
    for ryadok in f:
        m = shablon.search(ryadok)
        if not m:
            propushcheno += 1
            continue
        rozibrano += 1
        ip[m["ip"]] += 1
        kody[m["kod"]] += 1
        if m["kod"].startswith("5"):
            pomylky_5xx.append((m["chas"], m["shliakh"]))

print(f"1. Розібрано: {rozibrano}, пропущено: {propushcheno}")

print("\n2. Топ-5 IP-адрес:")
for adresa, kilkist in ip.most_common(5):
    print(f"   {kilkist:3}  {adresa}")

print(f"\n3. Коди відповіді ({len(kody)} різних):")
for kod, kilkist in sorted(kody.items()):
    print(f"   {kod}: {kilkist}")

print(f"\n4. Запити з помилкою 5xx ({len(pomylky_5xx)}):")
for chas, shliakh in pomylky_5xx:
    print(f"   {chas}  {shliakh}")
