scrmb = input()
with open('Database.txt','w') as lst:
    for word in lst.split():
        if len(scrmb) == len(word) and set(scrmb) == set(word):
            print(word)
