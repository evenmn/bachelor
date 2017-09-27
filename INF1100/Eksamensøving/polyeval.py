def polyeval(x, p):
    result = 0
    for k in p:
        result += p[k]*x**k
    return result

print polyeval(2,{1:-1, 3:1})
