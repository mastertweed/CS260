# Input the zip code, convert to string then to list of characters, change characters to ints
user = input('Enter your Zip Code: ')
user_s = list(str(user))

user_split_int = [int(k) for k in user_s]


# define all number 0-9 in barcode
def print_digit(num):
    frames = ['!!...', '...!!', '..!.!', '..!!.', '.!..!',
              '.!.!.', '.!!..', '!...!', '!..!.', '!.!..']

    return frames[num]


def print_barcode(digits):
    # Start barcode with !
    barcode = '!'
    count = 1
    for i in digits:
        # Add add barcode number to barcode string
        barcode = barcode + (print_digit(i))
        # If iteration of list less then 5 add a space otherwise finish barcode with !
        if count < 5:
            barcode = barcode + ' '
        count = count + 1
    barcode = barcode + '!'

    return barcode

# Print barcode
print(print_barcode(user_split_int))
# Create/Access file adt55_barcode.txt, write initial zip code, newline, write zip code as barcode
f = open("adt55_barcode.txt", "w+")
f.write(user)
f.write('\n')
f.write(print_barcode(user_split_int))
