#Creater: Caleb Hathaway ID: 005470217

from csvReader import getHashMap
from packages import totalDistance
import datetime
from styles import bcolor

class Main:

    print(bcolor.GREEN + "------------------------------" + bcolor.END)
    print(bcolor.GREEN + "WGUPS Routing System." + bcolor.END)
    print(bcolor.GREEN + "------------------------------\n" + bcolor.END)
    print(bcolor.GREEN + f"Total Miles {totalDistance():.2f} miles.\n" + bcolor.END)

    userInput = input(bcolor.CYAN + """
    Select one of the following:
    1: Get info for all packages at a particular time
    2: Get info for a single package at a particular time
    3: Exit

    Choice: """ + bcolor.END)

    while userInput != "3":
        # O(n) Complexity.
        # Finds all packages in specified time
        if userInput == "1":
            try:
                inputTime = input(bcolor.CYAN + "\nEnter a time in the following format: (HH:MM:SS): " + bcolor.END)
                (hrs, mins, secs) = inputTime.split(":")
                convertUserTime = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))

                # O(n^2) Complexity
                for count in range(1,41):
                    try:
                        firstTime = getHashMap().getValue(str(count))[9]
                        secondTime = getHashMap().getValue(str(count))[10]
                        (hrs, mins, secs) = firstTime.split(":")
                        convertFirstTime = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                        (hrs, mins, secs) = secondTime.split(":")
                        convertSecondTime = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                    except:
                        print(bcolor.RED + "Invalid entry" + bcolor.END)

                        # Finds the packages that have left hub
                    if convertFirstTime >= convertUserTime:
                        getHashMap().getValue(str(count))[10] = bcolor.BLUE + "At Hub " + bcolor.END
                        getHashMap().getValue(str(count))[9] = bcolor.BLUE + "Leaves at " + bcolor.END + bcolor.PURPLE + firstTime + bcolor.END

                        # Print package data
                        print(bcolor.GREEN + "Package ID: " + bcolor.END, end ="") 
                        print(bcolor.BLUE + f"{getHashMap().getValue(str(count))[0]}, " + bcolor.END, end ="")
                        print(bcolor.GREEN + "Delivery status: " + bcolor.END, end ="")
                        print(bcolor.BLUE + f"{getHashMap().getValue(str(count))[10]}\n" + bcolor.END)

                    # Finds packages still in transit
                    elif convertFirstTime <= convertUserTime:
                        if convertUserTime < convertSecondTime:
                            getHashMap().getValue(str(count))[10] = bcolor.BLUE + "In transit" + bcolor.END
                            getHashMap().getValue(str(count))[9] = bcolor.BLUE + "Left at " + bcolor.END + bcolor.PURPLE + firstTime + bcolor.END

                            # Prints package data
                            print(bcolor.GREEN + "Package ID: " + bcolor.END, end = "")
                            print(bcolor.BLUE + f"{getHashMap().getValue(str(count))[0]}, " + bcolor.END, end = "")
                            print(bcolor.GREEN + "Delivery status: " + bcolor.END, end = "")
                            print(bcolor.BLUE + f"{getHashMap().getValue(str(count))[10]}\n" + bcolor.END)

                        # Finds delivered packages
                        else:
                            getHashMap().getValue(str(count))[10] = bcolor.BLUE + "Delivered at: " + bcolor.END + bcolor.PURPLE + secondTime + bcolor.END
                            getHashMap().getValue(str(count))[9] = bcolor.BLUE + "Left at " + bcolor.END + bcolor.PURPLE + firstTime + bcolor.END

                            # Prints package data
                            print(bcolor.GREEN + "Package ID: " + bcolor.END, end = "")
                            print(bcolor.BLUE + f"{getHashMap().getValue(str(count))[0]}, " + bcolor.END, end = "")
                            print(bcolor.GREEN + "Delivery status: " + bcolor.END, end = "")
                            print(bcolor.BLUE + f"{getHashMap().getValue(str(count))[10]}\n" + bcolor.END)

            except:
                print(bcolor.RED + "Invalid entry" + bcolor.END)

        # O(n) Complexity.
        # Finds package in specified time
        elif userInput == "2":
            try:
                count = input(bcolor.CYAN + "Enter a valid package ID: " + bcolor.END)
                firstTime = getHashMap().getValue(str(count))[9]
                secondTime = getHashMap().getValue(str(count))[10]
                inputTime = input(bcolor.CYAN + "Enter a time (HH:MM:SS): " + bcolor.END)
                (hrs, mins, secs) = inputTime.split(",")
                convertUserTime = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                (hrs, mins, secs) = firstTime.split(",")
                convertFirstTime = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                (hrs, mins, secs) = secondTime.split(",")
                convertSecondTime = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))

                # Finds the packages that have left hub
                if convertFirstTime >= convertUserTime:

                    getHashMap().getValue(str(count))[10] = bcolor.GREEN + "At Hub" + bcolor.END
                    getHashMap().getValue(str(count))[9] = bcolor.BLUE + "Leaves at " + bcolor.END + bcolor.PURPLE + firstTime + bcolor.END
                    
                    # Prints package data
                    print(bcolor.GREEN + "Package ID: " + bcolor.END, end = "")
                    print(bcolor.BLUE + f"{getHashMap().getValue(str(count))[0]}" + bcolor.END)
                    print(bcolor.GREEN + "Street address: " + bcolor.END, end = "")
                    print(bcolor.BLUE + f"{getHashMap().getValue(str(count))[2]}" + bcolor.END)
                    print(bcolor.GREEN + "Required delivery time: " + bcolor.END, end = "")
                    print(bcolor.BLUE + f"{getHashMap().getValue(str(count))[6]}" + bcolor.END)
                    print(bcolor.GREEN + "Package weight: " + bcolor.END, end = "")
                    print(bcolor.BLUE + f"{getHashMap().getValue(str(count))[7]}" + bcolor.END)
                    print(bcolor.GREEN + "Truck status: " + bcolor.END, end = "")
                    print(bcolor.BLUE + f"{getHashMap().getValue(str(count))[9]}" + bcolor.END)
                    print(bcolor.GREEN + "Delivery status: " + bcolor.END, end = "")
                    print(bcolor.BLUE + f"{getHashMap().getValue(str(count))[10]}\n" + bcolor.END)

                # Finds packages still in transit
                elif convertFirstTime <= convertUserTime:
                    if convertUserTime < convertSecondTime:
                        getHashMap().getValue(str(count))[10] = bcolor.BLUE + "In transit" + bcolor.END
                        getHashMap().getValue(str(count))[9] = bcolor.BLUE + "Left at " + bcolor.end + bcolor.PURPLE + firstTime + bcolor.END

                        # Prints package data
                        print(bcolor.GREEN + "Package ID: " + bcolor.END, end = "")
                        print(bcolor.BLUE + f"{getHashMap().getValue(str(count))[0]}" + bcolor.END)
                        print(bcolor.GREEN + "Street address: " + bcolor.END, end = "")
                        print(bcolor.BLUE + f"{getHashMap().getValue(str(count))[2]}" + bcolor.END)
                        print(bcolor.GREEN + "Required delivery time: " + bcolor.END, end = "")
                        print(bcolor.BLUE + f"{getHashMap().getValue(str(count))[6]}" + bcolor.END)
                        print(bcolor.GREEN + "Package weight: " + bcolor.END, end = "")
                        print(bcolor.BLUE + f"{getHashMap().getValue(str(count))[7]}" + bcolor.END)
                        print(bcolor.GREEN + "Truck status: " + bcolor.END, end = "")
                        print(bcolor.BLUE + f"{getHashMap().getValue(str(count))[9]}" + bcolor.END)
                        print(bcolor.GREEN + "Delivery status: " + bcolor.END, end = "")
                        print(bcolor.BLUE + f"{getHashMap().getValue(str(count))[10]}\n" + bcolor.END)

                    # Finds delivered packages
                    else:
                        getHashMap().getValue(str(count))[10] = bcolor.BLUE + "Delivered at: " + bcolor.END + bcolor.PURPLE + secondTime + bcolor.END
                        getHashMap().getValue(str(count))[9] = bcolor.BLUE + "Left at " + bcolor.END + bcolor.PURPLE + firstTime + bcolor.END

                        # Prints package data
                        print(bcolor.GREEN + "Package ID: " + bcolor.END, end = "")
                        print(bcolor.BLUE + f"{getHashMap().getValue(str(count))[0]}" + bcolor.END)
                        print(bcolor.GREEN + "Street address: " + bcolor.END, end = "")
                        print(bcolor.BLUE + f"{getHashMap().getValue(str(count))[2]}" + bcolor.END)
                        print(bcolor.GREEN + "Required delivery time: " + bcolor.END, end = "")
                        print(bcolor.BLUE + f"{getHashMap().getValue(str(count))[6]}" + bcolor.END)
                        print(bcolor.GREEN + "Package weight: " + bcolor.END, end = "")
                        print(bcolor.BLUE + f"{getHashMap().getValue(str(count))[7]}" + bcolor.END)
                        print(bcolor.GREEN + "Truck status: " + bcolor.END, end = "")
                        print(bcolor.BLUE + f"{getHashMap().getValue(str(count))[9]}" + bcolor.END)
                        print(bcolor.GREEN + "Delivery status: " + bcolor.END, end = "")
                        print(bcolor.BLUE + f"{getHashMap().getValue(str(count))[10]}\n" + bcolor.END)

            except ValueError:
                print(bcolor.RED + "Invalid entry" + bcolor.END)

        # This exits the program
        elif userInput == "3":
            exit()