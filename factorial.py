# Generate n factorial
def rec_fact(n):
    if n == 0:
        return 1
    else:
        return (n * rec_fact(n-1))

print rec_fact(4)
