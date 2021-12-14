def decryption(encrypted, key):
    # initializing variables needed for the program
    a = 0
    decrypted_message = ''

    # The case when the length of our text is even but the key is not even.
    if len(encrypted) % 2 == 0 and key % 2 != 0:
        # dividing the length of the word by the key to know which partitions to start from
        b = len(encrypted) // key

        # we loop with a is less that the length of our partition
        while a < b:
            b += 1
            # adding the characters to our result variable
            decrypted_message += encrypted[a]
            # loop through the length of the word starting at a
            for i in range(a, len(encrypted)):
                # getting the next index to add to the answer
                c = i + b
                decrypted_message += encrypted[c]
                # getting the next index to add to the answer
                decrypted_message += encrypted[c + key]
                # breaking out of the loop
                break

            # reset the b to the partition
            b = len(encrypted) // key
            # increment incrementing a to start at the next index and take b steps every time
            a += 1
            # add the last character of b to the answer
        decrypted_message += encrypted[b]

    # checking for cases when the length of the text is even and the key is even
    if len(encrypted) % 2 == 0 and key % 2 == 0:
        # dividing the length of the word by the key to know which partitions to start from
        b = len(encrypted) // key

        # while a in less than the partition
        while a < b:
            # loop through the length of the word starting at a and take b steps every time
            for i in range(a, len(encrypted), b):
                # adding the characters to our result variable
                decrypted_message += encrypted[i]
            # incrementing a to start at the next index and take b steps every time
            a += 1

            # checking for edges cases when the length of the
    return decrypted_message


# calling the function
decrypted = decryption(encrypted, key)

print("The plain text is: " + text)
print("The text after encryption is: " + encrypted)
print("The text after decryption is: " + decrypted)
