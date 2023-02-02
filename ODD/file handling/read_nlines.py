
n = int(input('Enter the number of lines'))


f = open('sample.txt', 'r')
for i in range(n):
    data = f.readline()
    print(data)
f.close()


with open('sample.txt') as f:
    for i in range(n):
        print(f.readline())


# writing file using with
with open('info.txt', 'w') as f:
    f.write('Hello World')

f.closed 