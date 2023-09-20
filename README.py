"""
Caesar Cipher.

:author: SFS
"""


def shift(letter: str, shift_amount: int) -> str:
    """
    Perform a letter shift.
    
    :param letter: starting letter
    :param shift_amount: letter shift amount
    
    :return: new shifted letter
    """
    
    letter_code = ord(letter)
    # uses ASCII table to get character code number
    
    letter_location = letter_code - 97
    # since "a" has code 97, "b" has code 98, and so on...
    # we subtract 97 to get the "letter location" such that
    # "a" is 0, "b" is 1, "c" is 2, etc.
    
    new_letter_location = letter_location + shift_amount
    # we add the shift to get the location of the new letter
    
    new_letter_location = new_letter_location % 26
    # but what happens when our new letter code is bigger than our largest
    # letter code??? -- for example, a shift of "y" by 4 yields a code of 24+4
    # = 28... we have to do a "wraparound"
    
    # the "%" operator finds the remainder value when a number is divided by 26,
    # and for codes 0-25, the remainder is the same number, but for anything bigger,
    # it performs this wraparound operation that we want!
    
    # shortcut: new_letter_location %= 26
    
    new_letter_code = new_letter_location + 97
    # add 97 back to the new letter location to get the ASCII code
    
    return chr(new_letter_code)
    # turn the "new_letter_code" value back into a character (or letter)
    # AND then "return" this value
    
    
def encode() -> None:
    """
    Encode a message.
    """

    message = input("Enter the word: ")
    # get word to encode
    
    shift_amount = int(input("Enter the shift: "))
    # get Caesar shift amount
    
    for letter in message:
    # loop through each letter in the message --
    # so for the word "hello" it will set "letter" to "h" then run the code
    # within the loop, then it will set "letter" to "e" and run the code,
    # then "l" "l" "o"
    
        print(shift(letter, shift_amount), end="")
        # for each letter in the word, run the "shift" function on the letter;
        # the result of this (the shifted letter) will then be printed --
        # the 'end=""' block specifies that an "ENTER" is not displayed after
        # the letter is displayed, so all letters are placed on the screen next
        # to each other
        
    print()
    # "makes it look better" --
    # because of the 'end=""' an "ENTER" is never printed after the final
    # shifted word, so this empty print does that


def decode() -> None:
    """
    Decode a message.
    """
    
    message = input("Enter the encoded word: ")
    # get word to decode
    
    shift_amount = int(input("Enter the shift: "))
    # get original Caesar shift amount used to encode the word
    
    for letter in message:
    # loop through letters just like in "encode"
    
        print(shift(letter, -shift_amount), end="")
        # perform and print the shift like in "encode" -- BUT
        # this time we shift by the negative of the shift amount;
        # so if a word was encoded with shift=4, shifting by -4
        # puts it back to the original value
        
    print()
    # print for formatting


if __name__ == "__main__":
# the program starts here!
     
    encode()
    # encode a word
    
    print("\n" + "=" * 50 + "\n")
    # formatting print
    
    decode()
    # decode a word