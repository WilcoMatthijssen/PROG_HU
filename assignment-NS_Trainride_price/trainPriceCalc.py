def standardFare(distanceInKM):
    """Return the standard fare for a train ride with distance in KM."""
    if distanceInKM <0:
        raise ValueError("distanceInKM should be a positive")
    if distanceInKM > 50:
         price= 15 + distanceInKM * 0.6
    else:
        price= distanceInKM * 0.8
    return price
  

def trainFare(age, weekendRide, distanceInKM):
    """ Returns the train fare """
    if weekendRide:
        if age <= 12  or age >= 65:
            priceMultiplier=0.70
        else:
            priceMultiplier=0.60
    else:
        if age <= 12  or age >= 65:
            priceMultiplier=0.65
        else:
            priceMultiplier=1.00
    return standardFare(distanceInKM)*priceMultiplier

def testTrainFareFunction():
    """ Way too simple for a test but it tests if the priceMultiplier or age if statements are changed. """
    for i in range(8, 64, 2):
        if i <= 12  or i >= 65:
            if trainFare(i, True, 10) != standardFare(10) * 0.70:
                raise ValueError("trainFare function gave false return value with age: {}, weekendRide: True, distanceInKM: 10".format(i))
        else:
            if trainFare(i, True, 10) != standardFare(10) * 0.60:
                raise ValueError("trainFare function gave false return value with age: {}, weekendRide: True, distanceInKM: 10".format(i))
    print("test was succesfull!")


