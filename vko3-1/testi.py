numbers = ['123456789.123456789', '123453459.128967678']

with open(path + '\\numbers.txt', 'w') as out:
    for n in numbers:
        out.write(n + '\n')