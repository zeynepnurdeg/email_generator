path = "C:\\Users\\zeyne\\OneDrive\\Masaüstü\\workerNames.txt"

try:
    inp = open(path,"r")

    for name in inp.readlines():
        pos = name.find(" ")
        first_name = name[:pos].capitalize()
        last_name = name[pos + 1:].lower()
        email = last_name.strip() + first_name[0] + "@abc.com"
        print(email)
except FileNotFoundError:
    print("File Not Found!!!")
except TypeError:
    print("There is a type error")