import datetime
import distance
import csvReader

# Create Empty Lists for each list of data needed
firstDelivery = []
secondDelivery = []
thirdDelivery = []
firstTruckDistances = []
secondTruckDistances = []
thirdTruckDistances = []

# Each dispatch time for trucks
firstLeaveTimes = ["8:00:00"]
secondLeaveTimes = ["9:10:00"]
thirdLeaveTimes = ["11:00:00"]

# O(n) Complexity
# deliveryStart = firstLeaveTime for all packages on 1st truck
for index, value in enumerate(csvReader.getFirstDelivery()):
    csvReader.getFirstDelivery()[index][9] = firstLeaveTimes[0]
    firstDelivery.append(csvReader.getFirstDelivery()[index])
    
# O(n^2) Complexity
# Compares current address for 1st truck to neighboring addresses
for index, outer in enumerate(firstDelivery):
    for inner in distance.getAddress():
        if outer[2] == inner[2]:
            firstTruckDistances.append(outer[0])
            firstDelivery[index][1] = inner[0]

# Sorts packages on to 1st truck
distance.getShortestRoute(firstDelivery, 1, 0)
totalDistanceOne = 0

# O(n) Complexity
# Total distance for 1st truck and packages
for index in range(len(distance.firstTruckIndex())):
    try:
        totalDistanceOne = distance.getDistance(int(distance.firstTruckIndex()[index]), int(distance.firstTruckIndex()[index + 1]), totalDistanceOne)
        
        deliverPackage = distance.getTime(distance.getCurrentDistance(int(distance.firstTruckIndex()[index]), int(distance.firstTruckIndex()[index + 1])), firstLeaveTimes)
        distance.firstTruckList()[index][10] = (str(deliverPackage))
        csvReader.getHashMap().update(int(distance.firstTruckList()[index][0]), firstDelivery)
    except IndexError:
        pass

# O(n) Complexity
# Set deliveryStart = secondLeaveTime for all 2nd truck packages
for index, value in enumerate(csvReader.getSecondDelivery()):
    csvReader.getSecondDelivery()[index][9] = secondLeaveTimes[0]
    secondDelivery.append(csvReader.getSecondDelivery()[index])

# O(n^2) Complexity
# Compare 2nd truck addresses to address neighboring
for index, outer in enumerate(secondDelivery):
    for inner in distance.getAddress():
        if outer[2] == inner[2]:
            secondTruckDistances.append(outer[0])
            secondDelivery[index][1] = inner[0]

# Sorts packages for 2nd truck
distance.getShortestRoute(secondDelivery, 2, 0)
totalDistanceTwo = 0

# O(n) Complexity
# Total distance for 2nd truck and packages
for index in range(len(distance.secondTruckIndex())):
    try:
        totalDistanceT = distance.getDistance(int(distance.secondTruckIndex()[index]), int(distance.secondTruckIndex()[index + 1]), totalDistanceTwo)
        
        deliveryPackage = distance.getTime(distance.getCurrentDistance(int(distance.secondTruckIndex()[index]), int(distance.secondTruckIndex()[index + 1])), secondLeaveTimes)
        distance.secondTruckList()[index][10] = (str(deliveryPackage))
        csvReader.getHashMap().update(int(distance.secondTruckList()[index][0]), secondDelivery)
    except IndexError:
        pass

# O(n) Complexity
# Set deliveryStart = thirdLeaveTime for 3rd tuck packages
for index, value in enumerate(csvReader.getFinalDelivery()):
    csvReader.getFinalDelivery()[index][9] = thirdLeaveTimes[0]
    thirdDelivery.append(csvReader.getFinalDelivery()[index])

# O(n^2) Complexity
# Compare 3rd truck address to all neighboring addresses
for index, outer in enumerate(thirdDelivery):
    for inner in distance.getAddress():
        if outer[2] == inner[2]:
            thirdTruckDistances.append(outer[0])
            thirdDelivery[index][1] = inner[0]

# Sort all packages for 3rd truck
distance.getShortestRoute(thirdDelivery, 3, 0)
totalDistanceThree = 0

# O(n) Complexity
# Total distance for 3rd truck and packages
for index in range(len(distance.thirdTruckIndex())):
    try:
        totalDistanceThree = distance.getDistance(int(distance.thirdTruckIndex()[index]), int(distance.thirdTruckIndex()[index + 1]), totalDistanceThree)
        
        deliverPackage = distance.getTime(distance.getCurrentDistance(int(distance.thirdTruckIndex()[index]), int(distance.thirdTruckIndex()[index + 1])), thirdLeaveTimes)
        distance.thirdTruckList()[index][10] = (str(deliverPackage))
        csvReader.getHashMap().update(int(distance.thirdTruckList()[index][0]), thirdDelivery)
    except IndexError:
        pass

# O(1) Complexity
# Sum of package distances
def totalDistance():
    return totalDistanceOne + totalDistanceTwo + totalDistanceThree
