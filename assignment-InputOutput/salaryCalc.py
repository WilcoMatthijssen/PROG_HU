def printSalary(hoursWorked, hourlyWage):
    """Print out hours worked, hourly wage and salary."""
    try:
        print("You earn {} per hour.".format(hourlyWage))
        print("You worked {} hour(s).".format(hoursWorked))
        salary=hoursWorked*hourlyWage
        print("{} hour(s) work results into a salary of {}".format(hoursWorked, salary))
    except:
        print("Your input was not valid, try using int or floats.")


