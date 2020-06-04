def standard_fare_calc(distance_in_km: float) -> float:
    """
    Calculate the standard fare for a train ride with distance in KM.

    :param distance_in_km: Distance of the train ride in km as a float.
    :return fare: Standard fare for the train ride as a float.
    """
    if distance_in_km > 50:
        fare = 15 + distance_in_km * 0.6
    if distance_in_km > 0:
        fare = distance_in_km * 0.8
    else:
        raise ValueError("distance_in_km should be positive")

    return fare


def train_fare_calc(age: int, weekend_ride: bool, distance_in_km: float) -> float:
    """
    Calculate the train fare for a train ride including discounts.

    :param age: Age of the person going on the train ride as an int.
    :param weekend_ride: If the train ride is in the weekend as a bool.
    :param distance_in_km: Distance of the train ride in km as a float.
    :return fare: Train fare for the train ride as a float.
    """
    if weekend_ride:
        if 12 <= age <= 65:
            price_multiplier = 0.60
        else:
            price_multiplier = 0.70
    else:
        if 12 <= age <= 65:
            price_multiplier = 1
        else:
            price_multiplier = 0.65

    try:
        fare = standard_fare_calc(distance_in_km)
    except ValueError:
        fare = 0
    else:
        fare *= price_multiplier

    return fare



