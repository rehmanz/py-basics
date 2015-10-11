# 1 -> "one"
# 10 -> "ten"
# 100 -> "one hundred"
# 1001 -> "one thousand and one"
# 100111 -> "one hundred thousand one hundred and eleven"

def lookup_string():
    pass

def int_to_words(number):
    l = len(str(number))
    s = ''
    if l == 1:
        s = 'one'
        mod = 1
    elif l == 2:
        s = 'ten'
        mod = 10
    elif l == 3:
        s = 'one hundred'
        mod = 100

    # d = {
    #     1   :   'one',
    #     10  :   'ten',
    #     100 :   'one hundred'
    # }
    print(s)
    remainder_s = number % mod
    print("%s %s" %(s, remainder_s))


int_to_words(10)

