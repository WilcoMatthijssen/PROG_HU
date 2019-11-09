def standardFare(distanceInKM):
    """Return the standard fare for a train ride with distance in KM."""
    if distanceInKM <0:
        myError = ValueError('distanceInKM should be a positive')
        raise myError
    if distanceInKM > 50:
         price= 15 + distanceInKM * 0.6
    else:
        price= distanceInKM * 0.8
    return price
  

def trainFare(age, weekendRide, distanceInKM):
    print("WIP")