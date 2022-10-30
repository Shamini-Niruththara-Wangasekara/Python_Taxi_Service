import datetime
import json


def main():
    time = datetime.datetime.now()
    print("""     
                   _______                         
                  //  ||\ \\
            _____//___||_\ \___
            )  _          _    \\
            |_/ \________/ \___|
           ___\_/________\_/______
                   _______
                  //  ||\ \\
            _____//___||_\ \___
            )  _          _    \\
            |_/ \________/ \___|
           ___\_/________\_/______
       """)

    print("\n\tWELCOME TO SN CAB SERVICE\n")
    print(f"\tCurrent date and time: {time}")

    while True:
        print("""
        ********  SN cab service ********
        1. Admin
        2. Unregistered Customer
        3. Registered Customer
        4. Exit 
        """)

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number!")
            continue

        if choice == 1:
            admin()

        elif choice == 2:
            unregistered_function()

        elif choice == 3:
            registered_function()

        elif choice == 4:
            break

        else:
            print("Please Enter a choice between 1-4 only!")


def login(user, password, elevated):
    print(user, password)
    with open("Admin.json" if not elevated else "Admin.json", "r") as text:
        userData = json.load(text)
        userData = userData["admins"]
        print(userData)
        print("%s Login ********" % ("******** Admin" if elevated else "******** User"))
        text.close()
        for record in userData:
            print(record)
            userName = record['userName']
            paswrd = record['password']
            if userName == user and password == paswrd:
                print("Welcome, %s" % user)
                return True
        print("Error! Wrong username or password")
        return False


def admin():
    nValue = input("Enter username: ")
    pValue = input("Enter password: ")
    if login(nValue, pValue, True):
        admin_function()


def admin_function():
    while True:
        print("""
            ******** Access System ********
            1. Add cabs with Details
            2. Remove cabs Details
            3. Display All records of
                a. Cabs available for Rent
                b. Customer Payment 
            4. Search Specific record of
                a. Cab Booking
                b. Customer Payment
            5. Return a Rented cab
            6. Exit to main menu
            """)

        try:
            choice = int(input("Enter a number: "))
        except ValueError:
            print("Please Enter a number!")
            continue

        if choice == 1:
            add_cabs()

        elif choice == 2:
            remove_cabs()

        elif choice == 3:
            option = input("option a or b? ")
            if option == 'a':
                display_cabs()
            else:
                print("Customers Payment for a specific time duration")  # customers_payment function goes here

        elif choice == 4:
            option = input("option a or b?")
            if option == 'a':
                assign_cabs()
            else:
                print("Customer Payment")

        elif choice == 5:
            return_cabs()

        elif choice == 6:
            break

        else:
            print("Please enter a number between 1-6 only!")


def get_new_users():
    admins = []
    with open("user.json", "r") as fp:
        admins = json.load(fp)
        admins = admins["admins"]
        fp.close()
        while True:
            name = input("Enter name to register: ")
            password = input("Enter password: ")
            adminRecord = {"userName": name, "password": password}
            admins = admins.append(adminRecord)
            with open("user.json", "w") as fp:
                json.dump({"admins": admins}, fp, indent=4)
                fp.close()
            break


def existing_users():
    nValue = input("Username: ")
    pValue = input("Password: ")
    return login(nValue, pValue, False)


def display_cabs():
    with open("displaycabs.json", "r") as data:
        print(data)
        cabData = json.load(data)
        print(cabData)
        cab_type = input("Type: ")
        if cab_type.lower() == "car":
            print("""car: maximum number of passengers - 3 and 4
                      AC/Non AC
                 """)
        elif cab_type.lower() == "van":
            print("""van: maximum number of passengers - 6 and 8
                     AC/Non AC
                 """)
        elif cab_type.lower() == "threewheel":
            print("""threewheel: maximum number of passengers - 3
                """)
        elif cab_type.lower() == "truck":
            print("""Size - 7ft and 12ft
                            """)
        else:
            print("""Max load and size - 2500kg and 3500kg
                                        """)


def add_cabs():
    with open("cabs.json", "r") as data:
        print(data)
        cabData = json.load(data)
        print(cabData)
        car_type = input("Type: ")
        brand = input("Brand: ")
        color = input("Color: ")
        year = input("Year: ")
        condition = input("Status: ")

        if car_type.lower() == "car":
            cabArr = cabData["cars"]
            cabArr.append({"car_type": car_type, "brand": brand, "color": color, "year": year, "con": condition})
            cabData["cars"] = cabArr
        else:
            cabArr = cabData["van"]
            cabArr.append({"car_type": car_type, "brand": brand, "color": color, "year": year, "con": condition})
            cabData["van"] = cabArr
    with open("cabs.json", "w") as cab:
        json.dump(cabData, cab, indent=4)
        data.close()

    cabArr.append({})
    print("Added succesfully!")


def remove_cabs():
    with open("displaycabs.json", "r") as data:
        cabData = json.load(data)
        # cabs = cabData[vehtype]
        # data.close()
        # print(cabs)
        for i in range(len(cabData)):
            if cabData[i]["idnumber"] == "003v":
                cabData.pop(i)
                break
        with open("displaycabs.json", "w") as data:
            cabData = json.dump(cabData, data, indent=4)
            data.close()


# if c["id"] == id:
# cabs.remove(c)

# print(cabs)
# cabData[vehtype] = cabs
# print(cabData)

def unregistered_function():
    while True:
        print("""
        ******** All Customers ********
        1. View all cabs available for rent
        2. Register to System
        3. Exit to main menu
        """)
        try:
            choice = int(input("Enter a number: "))
        except ValueError:
            print("Please enter a number!")
            continue

        if choice == 1:
            display_cabs()

        elif choice == 2:
            get_new_users()
            # break

        elif choice == 3:
            break

        else:
            print("Please enter a choice between 1-3 only!")


def registered_function():
    if existing_users() is True:
        while True:
            print("""
            ******** Registered Customer ********
            1. Personal Rental History
            2. Display Cabs
            3. Booking Cabs 
            4. Payment and Confirmation of Booking
            5. Exit to main menu
            """)
            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Please enter a number!")
                continue

            if choice == 1:
                print("personal history")  # personal_rental_history function goes here

            elif choice == 2:
                display_cabs()

            elif choice == 3:
                assign_cabs()

            elif choice == 4:
                print("payment and confirmation")  # payment function goes here

            elif choice == 5:
                break

            else:
                print("Please enter a choice between 1-5 only!")
    else:
        print("1. Please re-enter login details")
        print("2. Exit to main menu")
        choice = int(input("Enter choice: "))
        if choice == 1:
            existing_users()
        else:
            return


def assign_cabs():
    print(" 1. Car\n 2. Van\n 3. Threewheel\n 4. Truck\n 5. Lorry")
    hireDetails = []
    with open("assigncabs.json", "r") as data:
        print(data)
        cabData = json.load(data)
        print(cabData)
        car_type = input("Type: ")
        idno = input("Enter vehicle idno: ")
        if car_type.lower() == "car":
            cabArr = cabData["cars"]
            cabArr.append({"car_type": car_type, "ID number": idno, })
            cabData["cars"] = cabArr
        else:
            cabArr = cabData["van"]
            cabArr.append({"car_type": car_type, "ID number": idno, })
            cabData["van"] = cabArr
    with open("assigncabs.json", "w") as cab:
        json.dump(cabData, cab, indent=4)
        data.close()

    # while True:

    # hiredRecord = {"cab_type": type, "idnumber": idno}
    # hireDetails = hireDetails.append(hiredRecord)
    #    json.dump({"hireDetails": hireDetails}, fp, indent=4)
    #    fp.close()
    #    break


def return_cabs():
    # get inputs remove hired detail
    inputHiedId = input("Enter Hired Vehicle Id :")

    with open("assigncabs.json", "r") as data:
        cabData = json.load(data)
        cabs = cabData[type]
        data.close()
        print(cabs)
        for c in cabs:
            if c["id"] == id:
                cabs.remove(c)

        print(cabs)
        cabData[type] = cabs
        print(cabData)
        with open("assigncabs.json", "w") as fp:
            json.dump(cabData, fp, indent=4)
            fp.close()

    print("Hired Removed Successfully")


def checkDataFile():
    try:
        with open("cabs.json", "r") as data:
            try:
                vehicle_data = json.load(data)
            except json.decoder.JSONDecodeError:
                print("Decode error file will reset")


    except IOError:
        print('File not found, will create a new one.')
        vehicle_data = {
            "cars": [],
            "van": [],

        }
    with open("cabs.json", 'w') as fp:
        json.dump(vehicle_data, fp, indent=4)
        fp.close()
    return vehicle_data


if __name__ == "__main__":
    checkDataFile()
    main()
