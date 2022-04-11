import csv
import datetime

# Read CSV files
with open("./data/distanceData.csv") as csvfileOne:
    distanceCsv = list(csv.reader(csvfileOne, delimiter=","))
with open("./data/distanceNameData.csv") as csvfileSecond:
    distanceNameCsv = list(csv.reader(csvfileSecond, delimiter=","))

    # O(n) Complexity
    # Getting packages address data
    def getAddress():
        return distanceNameCsv

    # O(1) Complexity
    # Finding the totaled distance values for row and column data
    def getDistance(row, col, total):
        distance = distanceCsv[row][col]
        if distance == "":
            distance = distanceCsv[col][row]

        return total + float(distance)

    # O(1) Complexity
    # Finding the current distance values for row and column data
    def getCurrentDistance(row, col):
        distance = distanceCsv[row][col]
        if distance == "":
            distance = distanceCsv[col][row]

        return float(distance)

    # O(n) Complexity
    # Finding the totaled distance values for a truck
    def getTime(distance, truckList):
        newTime = distance / 18
        distanceInMinutes = "{0:02.0f}:{1:02.0f}".format(
            *divmod(newTime * 60, 60))
        finalTime = distanceInMinutes + ":00"
        truckList.append(finalTime)
        total = datetime.timedelta()
        for i in truckList:
            (hrs, mins, secs) = i.split(":")
            total += datetime.timedelta(hours=int(hrs),
                                        minutes=int(mins), seconds=int(secs))
        return total

    # Lists that show the sorted trucks
    # Trucks are arranged in from most effient to least
    firstTruck = []
    firstTruckIndices = []
    secondTruck = []
    secondTruckIndices = []
    thirdTruck = []
    thirdTruckIndices = []

    # Below is the "Greedy algorithm", it uses a recursive technique to repeat
    # until it finds the locaiton with the lowest distance value.
    
    # The algorithm uses 3 paremters to achieve the pathfinding
    # 1. List of all packages
    # 2. The truck number
    # 3. The current location of the truck

    # There are 2 loops, the first loop is for finding the shortest distance
    # from current location to next location, it plugs in the lowest value found
    # then replaces it with the next smallest found, until there are none left
    
    # The second loop decides what to do once the smallest distance is found
    # Branching statments are used to check which truck the package is in.
    # A location based on package with the shortest distance is then applied to the truck.
    # This loop continues until the base case is called and end the function while returning the empty list

    # Base Case: Length of the list is False, or zero. 

    # O(n^2) Space-Time Complexity

    def getShortestRoute(_list, num, currLocation):
        if not len(_list):
            return _list

        lowestValue = 50.0
        location = 0

        for i in _list:
            value = int(i[1])
            if getCurrentDistance(currLocation, value) <= lowestValue:
                lowestValue = getCurrentDistance(
                    currLocation, value)
                location = value

        for i in _list:
            if getCurrentDistance(currLocation, int(i[1])) == lowestValue:
                if num == 1:
                    firstTruck.append(i)
                    firstTruckIndices.append(i[1])
                    _list.pop(_list.index(i))
                    currLocation = location
                    getShortestRoute(_list, 1, currLocation)
                elif num == 2:
                    secondTruck.append(i)
                    secondTruckIndices.append(i[1])
                    _list.pop(_list.index(i))
                    currLocation = location
                    getShortestRoute(_list, 2, currLocation)
                elif num == 3:
                    thirdTruck.append(i)
                    thirdTruckIndices.append(i[1])
                    _list.pop(_list.index(i))
                    currLocation = location
                    getShortestRoute(_list, 3, currLocation)

    # Insert 0 for the first index of each index list
    firstTruckIndices.insert(0, "0")
    secondTruckIndices.insert(0, "0")
    thirdTruckIndices.insert(0, "0")

    # O(1) Complexity
    # The following are all helper functions to return a desired value
    def firstTruckIndex():
        return firstTruckIndices

    def firstTruckList():
        return firstTruck

    def secondTruckIndex():
        return secondTruckIndices

    def secondTruckList():
        return secondTruck

    def thirdTruckIndex():
        return thirdTruckIndices

    def thirdTruckList():
        return thirdTruck
