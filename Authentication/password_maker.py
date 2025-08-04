for i in range(150):
    if i % 3:
        print("carlos")
    else:
        print("wiener")

with open('passwords', 'r') as f:
    lines = f.readlines()
print("###############################################")
i = 0
for pwd in lines:
    if i % 3:
        print(pwd.strip('\n'))
    else:
        print('peter')
        print(pwd.strip('\n'))
        i = i+1
    i=i+1
