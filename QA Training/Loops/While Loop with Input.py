names = []

while True:
    name = input("Please enter a name...or type 'stop' to finish: ")
    if name.lower() == 'stop':
        break
    names.append(name)

for n in names:
    print(n + " is cool")
