from random import randint

def factorial(number):
    a=1
    for n in range(number):
        a=a*(n+1)
    return float(a)

def prob_six(n):
    N = 10000
    res = 0
    for i in range(N):
        number = 0
        for j in range(n):
            outcome = randint(1,6)
            if outcome == 6:
                if number == 0:
                    res += 1
                number += 1
    return float(res)/N

def exact_prob_six(n):
    return 1-(5./6)**n

Number_of_draws = 50

print exact_prob_six(Number_of_draws)
print prob_six(Number_of_draws)
