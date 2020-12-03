alfabet = {
    "A": 0,
    "B": 2,
    "C": 3,
    "D": 4
}

x = "ACDC"
tekst = "ABBACDCDACDACDC"
i = 0

def h(ciag):
    suma = 0
    q = 23
    r = len(ciag)
    n = r-1
    for litera in ciag:
        suma += alfabet[litera] * (r**n)
        n -= 1
    wynik = suma % q
    return wynik

h_x = h(x)
r = len(x)
q = 23

while i <= len(tekst) - len(x):
    tmp = ""
    k = 0
    if i > 0:
        while k < 4:
            tmp += tekst[i + k]
            k += 1
            h_tmp = ((h(prev_tmp) - (alfabet[prev_tmp[0]]*(r**(r-1)))) * r + alfabet[tmp[-1]]) % q
        if h_tmp == h_x:
            l = 0
            flag = True
            while l < len(x):
                if tmp[l] == x[l]:
                    l += 1
                else:
                    flag = False
                    break
            if flag:
                print(f"Indeks poczatku wyszukiwanego slowa: {i}")
    else:
        k = 0
        while k < 4:
            tmp += tekst[i + k]
            k += 1
    prev_tmp = tmp
    i += 1
