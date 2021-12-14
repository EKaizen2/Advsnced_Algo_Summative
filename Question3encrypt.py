text = 'Plain text'
key = int(input("Enter your key here: "))


# initialising an encryption function that takes two arguments: the text and the key
def encryption(text, key):
    # initializing a variable to store the encrypted message
    encrypted_message = ""

    # Creating a variable to assist determine where to begin and stop based on the key
    start = 0

    # Her we try to cycle over the key and then through the text in the gaps of the key.
    # If the key is 2, for example, we loop through the text in 2 step increments
    # And add the characters to the result variable.
    while start < key:
        for j in range(start, len(text), key):
            # Formulating our result with characters gotten in steps of our key.
            encrypted_message += text[j]
        # Incrementing our start variable
        start += 1

    # Returning our result
    return encrypted_message

encrypted = encryption(text, key)
