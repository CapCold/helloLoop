count = 1

print("Are you sure")
sure = input()

if sure == "yes" or sure == "Yes" or sure == "YES":
    while count > 0:
        print("yikes big mistake")
else:
    quit()
