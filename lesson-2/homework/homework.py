# number data type 
def round2(num):
    return round(num, 2)

def minmax():
    l = list(map(float, input("sonlar kiriting (probel bilan ajrating): ").split()))
    print(max(l), min(l))

def km_to_m_cm():
    d = float(input("necha kilometer: "))
    cm = d * 100000
    m = cm // 100
    cm %= 100
    print(f"{m}m {cm}cm")

def remainder():
    a, b = map(int, input("sonlarni kiriting: ").split())
    print(a//b, a%b)

def C_to_F(t):
    return 9 * t / 5 + 32

def last_digit(num):
    return num % 10


#string data type
def age():
    input("ismingiz nima?: ")
    birth = int(input("qaysi yil tug'ilgansiz?: "))
    this_year = 2026
    print(f"Siz {this_year - birth} yoki {this_year - 1 - birth} yoshdasiz (tug'ilgan sanangizga bog'liq)")

def car_names():
    txt = "LMaasleitbtui"
    print(txt[0::2], txt[1::2])

def det():
    s = input("matn kiriting: ")
    print(f"uzunlik: {len(s)}\nupper: {s.upper()}\nlower: {s.lower()}")

def is_palindrome(s):
    return s == s[::-1]

def cons_vow():
    s = input("matnni kiriting: ").lower()
    cons = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    vow = ['a', 'e', 'i', 'o', 'u']
    c = v = 0
    for i in s:
        if (i in cons):
            c += 1
        elif (i in vow):
            v += 1
    print(f"consonants: {c}, vowels: {v}")

def contains(a, b):
    return b in a

def replace():
    text = input("matnni kiriting: ")
    target = input("nimani almashtirasiz: ")
    new = input("yangi matnni kiriting: ")
    l = len(new)
    i = 0
    t = text[i:].find(target)
    while (t != -1):
        text = text[:i+t] + new + text[i+t+l:]
        i += t + l
        if (i < len(text)):
            t = text[i:].find(target)
        else:
            break
    print(text)

def pre_end():
    s = input("matn kiriting: ")
    print(f"boshi: {s[0]},\n oxiri: {s[-1]}")

def reverse():
    s = input("matn kiriting: ")
    print(f"teskarisi: {s[::-1]}")

def num_words():
    s = input("gap kiriting: ")
    n = s.count(" ")
    if s == "":
        n = -1
    print(f"gapda {n+1}ta so'z bor")

def contains_digits(s):
    for i in range(0, 10):
        if str(i) in s:
            return True
    return False

def join(words):
    return ", ".join(words)

def acronym():
    s = list(input("matn kiriting: ").split())
    txt = ""
    for i in s:
        txt += i[0]
    print(f"acronym: {txt}")

def remove_all():
    s = input("matn kiriting: ")
    target = input("nimani o'chiramiz?: ")
    print(f"yangi matn: {s.replace(target, '')}")

def hide_vowels():
    import re
    s = input("matn kiriting: ")
    print(f"unlilar yashirlsa: {re.sub(r'[aeiouAEIOU]', '*', s)}")

def start_end(text, first, last):
    l1 = len(first)
    l2 = len(last)
    if len(text) < len(first) or len(text) < len(last):
        return False
    return text[:l1] == first and text[-l2:] == last


# boolean data type
def not_empty(username, password):
    return len(username) > 0 and len(password) > 0

def equal(a, b):
    if (a == b):
        print("equal!")
    return a == b

def pos_even(num):
    return num > 0 and num % 2 == 0

def different(a, b, c):
    return len({a, b, c}) == 3

def same_length(s1, s2):
    return len(s1) == len(s2)

def divisible(num):
    n = 15
    return num % n == 0

def greater(a, b):
    threshold = 50
    return a + b > threshold 

def inside(num):
    l, r = 10, 20
    return l <= num and r >= num


