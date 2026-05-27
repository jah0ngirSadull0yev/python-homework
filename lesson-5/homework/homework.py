# Task 1 (temperature.py):

def convert_cel_to_far(C):
    return C * 9/5 + 32

def convert_far_to_cel(F):
    return (F - 32) * 5/9

F = float(input("Enter a temperature in degrees F: "))
print(f"{F} degrees F = {convert_far_to_cel(F):.2f} degrees C\n")

C = float(input("Enter a temperature in degrees C: "))
print(f"{C} degrees C = {convert_cel_to_far(C):.2f} degrees F")


#Task 2 (invest.py):

def invest(amount, rate, years):
    st = amount
    for i in range(1, years+1):
        print(f"year {i}: ${(st := st * (1 + rate)):.2f}")

# invest(100, .05, 4)
# year 1: $105.00
# year 2: $110.25
# year 3: $115.76
# year 4: $121.55

amount, rate, years = map(float, input("Enter an initial amount, an annual percentage rate, and a number of years for investment: ").split())
years = int(years)
invest(amount, rate, years)


# Task 3 (factors.py):

n = int(input("Enter a positive integer: "))

for _ in (print(f"{i} is a factor of {n}") for i in range(1, n + 1) if n % i == 0):
    pass


# Task 4:

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(universities):
    return ([uni[1] for uni in universities], [uni[2] for uni in universities])

def mean(l):
    return sum(l) / len(l) if len(l) > 0 else None

def median(l):
    ln = len(l)
    return mean(sorted(l)[(ln - 1)//2:ln//2+1]) if ln > 0 else None

def format_num(n):
    res = f"{n:,.2f}"
    if res.endswith('.00'):
        return res[:-3]
    return res.rstrip('0').rstrip('.') if '.' in res else res

students, tuitions = enrollment_stats(universities)

print("*"*30)
print(f"Total students: {format_num(sum(students))}")
print(f"Total tuition: $ {format_num(sum(tuitions))}\n")
print(f"Student mean: {format_num(mean(students))}")
print(f"Student median: {format_num(median(students))}\n")
print(f"Tuition mean: $ {format_num(mean(tuitions))}")
print(f"Tuition median: $ {format_num(median(tuitions))}")
print("*"*30)


# Task 5:

def is_prime(n):
    return all(n % i != 0 for i in range(2, int(n**0.5) + 1)) if n > 1 else False

# bonus: sieve (better for many checks if the domain is known)
def primes(x): # O(n*log(n)) list generation 
    lst = [True] * (x + 1)
    lst[0] = lst[1] = False
    for t in range(2, int(x**0.5) + 1):
        if lst[t]:
            for i in range(t * t, x + 1, t):
                lst[i] = False
    return lst

n = 1000
p = primes(n)
isprime = lambda x, p: p[x] # O(1) response



