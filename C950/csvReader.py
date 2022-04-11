import csv
from hashTable import HashMap

# Read CSV files
with open("./data/inputData.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")

    hashMap = HashMap()

    # Lists for trucks
    firstDelivery = []
    secondDelivery = []
    thirdDelivery = []

    # O(n) Complexity
    # Insert data from csv file into key: value pairs
    for row in reader:
        deliveryStart = ""
        addressLocation = ""
        deliveryStatus = "At hub"
        id = row[0]
        address = row[1]
        city = row[2]
        state = row[3]
        zip = row[4]
        delivery = row[5]
        size = row[6]
        note = row[7]

        value = [
            id, 
            addressLocation, 
            address, 
            city, 
            state, 
            zip, 
            delivery, 
            size, 
            note, 
            deliveryStart, 
            deliveryStatus
        ]

        # O(1) Complexity
        # Packages for the 1st delivery
        def getFirstDelivery():
            return firstDelivery

        # O(1) Complexity
        # Packages for 2nd delivery
        def getSecondDelivery():
            return secondDelivery

        # O(1) Complexity
        # Packages for the 3rd delivery
        def getFinalDelivery():
            return thirdDelivery

        # O(1) Complexity
        # All packages
        def getHashMap():
            return hashMap

        # Branching statments that determine which truck a package is meant to be on
        # packages are appened to a list for quick indexing

        # Package with wrong details is fixed
        if "84104" in value[5] and "10:30" not in value[6]:
            thirdDelivery.append(value)

        # 1st tucks starting delivery
        if value[6] != "EOD":
            if "Must" in value[8] or "None" in value[8]:
                firstDelivery.append(value)

        # 2nd trucks delivery
        if "Can only be" in value[8] or "Delayed" in value[8]:
            secondDelivery.append(value)
        
        # Check remaining packages
        if value not in firstDelivery and value not in secondDelivery and value not in thirdDelivery:
            secondDelivery.append(value) if len(secondDelivery) < len(thirdDelivery) else thirdDelivery.append(value)

        # Inserting packages into the hash table
        hashMap.insert(id, value)
