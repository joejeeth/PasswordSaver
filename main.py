global site_name
global pass_word
global f_pass

print("1. Find Password \n2. Save password \n0. To exit")
choice = int(input("Enter your choice: "))
f_pass = 0

while choice != 0:

    if choice == 2:
        file = open("text.txt", "a")
        site_name = input("Enter Website: ")
        pass_word = input("Enter Password: ")
        file.write(f"\n{site_name}, {pass_word}")
        file.close()

    else:
        site_name = input("Enter Website name to find: ")
        with open("text.txt", "r") as file:
            for word in file:
                l_w = word.split()
                if l_w[0].replace(",", "") == site_name:
                    f_pass = l_w[1]
                    break
            if f_pass:
                print(f"\n ********** &&&&&&&& ********** \nSite name: {site_name} \nPassword is: {f_pass} \n ********** "
                      f"&&&&&&&& ********** \n")
            else:
                print("Could not find the site.")

    print("1. Find Password \n2. Save password \n0. To exit")
    choice = int(input("Enter your choice: "))
