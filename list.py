
def total_length(words):
    total = 0
    for word in words:
        length = len(word)
        total = length + total
    return total


print(total_length(['list','words']))



password = ''
while password != 'fizzbuzz':
    password = input('please enter password: ')

s = "Tenochtitlan"
index = 0
while index < len(s):
    index += 1
    print(s[:index])
