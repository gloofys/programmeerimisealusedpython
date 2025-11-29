# On antud sõne s = 'Python is a programming language that lets you work quickly and integrate Systems more effectively'
# Printige:
#  sõne s esimesed 10 sümbolit
#  sõne s viimased 10 sümbolit
#  sõne s iga 3. sümbol alates sõne algusest
#  sõne s vastupidises järjekorras
#  sõne, millest on eemaldatud esimene ja viimane sümbol

s = 'Python is a programming language that lets you work quickly and integrate Systems more effectively'
print (s[0:10])
print (s[-10:])
print (s[0:len((s)):3])
print(s[::-1])
print(s[1:len(s)-1])

# Kirjuta programm, mis võtab etteantud sõne ja jagab selle kaheks võimalikult võrdseks osaks ja paigutab need ümber.
# Kui sõne pikkus on paarisarv, peavad mõlemad pooled olema sama pikad. if  kasutada ei tohi.

# Kui sõne pikkus on paaritu, peab esimene pool olema ühe sümboli võrra pikem kui teine.

# Programmis peab kasutama täisarvulist jagamist (//), et määrata sõne poolitamise koht.

# Näiteks:
# Sisend: "Pallindromm"
# Väljund: ndrommPallin

# def split_word_equally_and_replace():
#     word=input("sisesta sona: ")
#     print(len(word))
#     first = word[:(len(word)+1) // 2]
#     second = word[(len(word) +1) // 2:]
#     print(len(first), len(second))
#     print(second + first)

# split_word_equally_and_replace()


# Kasutaja sisestab sõnet. Kirjutage programm, mis kuvab:
# •    sõne elemendid veerus vastupidises järjekorras
# •    sõne elemendid ühes reas vastupidises järjekorras (tühikuga)

def display_elements_reverse():
    sone = input("sisesta sone: ")
    for char in sone[::-1]:

        print(char, end="\n")
display_elements_reverse()