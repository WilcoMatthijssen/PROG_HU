from trainPriceCalc import *
print("The standard fare for a 100 KM is: {}".format(standardFare(100)))
print("The fare with discounts for someone that is 42 years old travelling 100 KM in the weekend is: {}".format(trainFare(42, True, 100)))
testTrainFareFunction()