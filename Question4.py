def generateSuperDigit(n, k):
    # Initializing our p variable the concatenation (n times k)
    # We also convert it to integer
    p = int(n * k)

    # Initializing a variable to help us calculate our super digit.
    superDigit = 0

    # While p is more than zero and total is less than 9, we perform a while loop.
    while (superDigit > 9 or p > 0):
        # If p equals 0, we are done adding the current digit, so let's exchange our
        # Current p with the total we've acquired so far to keep looking for the super value.
        if (p == 0):
            p, superDigit = superDigit, p

        # Else add the modulo of p to the total variable and divide it by 10 to remove the last digit.
        else:
            superDigit += p % 10
            p //= 10
    return superDigit

# Testing our code.
n = '9875'
k = 4
print("n = " + str(n))
print("k = " + str(k))
print("Super Digit = " + str(generateSuperDigit(n, k)))

n = '148'
k = 3
print("n = " + str(n))
print("k = " + str(k))
print("Super Digit = " + str(generateSuperDigit(n, k)))
