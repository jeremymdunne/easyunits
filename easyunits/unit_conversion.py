##  @file UnitConversion.py
#   File containing functions to handle unit conversions
#
#   This is used as a verified repository of conversion functions
#
#   @author Jeremy Dunne
#   @date October, 2021
#   @version V0.1.0
#   In progress, not complete by any means
#   Add functions as needed to ease upfront development time


########## Distance Conversions ##########

#### English to english ### why?

##  Convert inches to feet
#   @param inches (float)
#   @return (float)
def inchesToFeet(inches = 1):
    return inches / 12

##  Convert inches to yards
#   @param inches (float)
#   @return (float)
def inchesToYards(inches = 1):
    return inches / 36

##  Convert inches to miles
#   @param inches (float)
#   @return (float)
def inchesToMiles(inches = 1):
    return inches / 63360



#### English to metric

##  Convert inches to milimeters
#   This is a base function, used by others
#   @param inch (float)
#   @return (float) calculated milimeters
def inchesToMilimeters(inches = 1):
    return inches * 25.4

##  Convert inches to centimeters
#
#   @param inch (float)
#   @return (float) calculated centimeters
def inchesToCentimeters(inches = 1):
    return inches * 2.54

##  Convert inches to meters
#   @param inch (float)
#   @return (float) calculated meters
def inchesToMeters(inches = 1):
    return inches * .0254

##  Convert inches to kilometers
#   @param inch (float)
#   @return (float) calculated kilometers
def inchesToKilometers(inches = 1):
    return inches * .0000254

##  Convert feet to milimeters
#   @param feet (float)
#   @return (float) calculated milimeters
def feetToMilimeterss(feet = 1):
    return feet * 304.8

##  Convert feet to centimeters
#   @param feet (float)
#   @return (float) calculated centimeters
def feetToCentimeters(feet = 1):
    return feet * 30.48

##  Convert feet to meters
#   @param feet (float)
#   @param (float) calculated meters
def feetToMeters(feet = 1):
    return feet * 0.3048

## Convert feet to kilometers
#   @param feet (float)
#   @return (float) calculated kilometers
def feetToKilometers(feet = 1):
    return feet * 0.0003048

##  Convert yard to milimeters
#   @param yards (float)
#   @return (float) calculated milimeters
def yardsToMilimeters(yards = 1):
    return yards * 914.4

##  Convert yard to centimeters
#   @param yards (float)
#   @return (float) calculated milimeters
def yardsToCentimeters(yards = 1):
    return yards * 91.44

##  Convert yard to meters
#   @param yards (float)
#   @return (float) calculated meters
def yardsToMeters(yards = 1):
    return yards * 0.9144

##  Convert yard to kilometers
#   @param yards (float)
#   @return (float) calculated kilometers
def yardsToKilometers(yards = 1):
    return yards * 0.0009144

##  Convert miles to milimeters
#   @param miles (float)
#   @return (float) calculated milimeters
def milesToMilimters(miles = 1):
    return miles * 1609344

##  Convert miles to centimeters
#   @param miles (float)
#   @return (float) calculated centimeters
def milesToCentimeters(miles = 1):
    return miles * 160934.4

##  Convert miles to meters
#   @param miles (float)
#   @return (float) calculated meters
def milesToMeters(miles = 1):
    return miles * 1609.344

##  Convert miles to kilometers
#   @param miles (float)
#   @return (float) calculated kilometers
def milesToKilometers(miles = 1):
    return miles * 1.609344

#### Metric to English

##  Convert milimeters to inches
#   This is a basic function
#   @param milimeters (float)
#   @return (float)
def milimetersToInches(milimeters = 1):
    return milimeters / 25.4

##  Convert centimeters to inches
#   @param centimeters (float)
#   @return (float)
def centimetersToInches(centimeters = 1):
    return centimeters / 2.54

##  Convert meters to inches
#   @param meters (float)
#   @return (float)
def metersToInches(meters = 1):
    return meters / .0254

## Convert kilometers to inches
#   @param kilometers (float)
#   @return (float)
def kilometersToInches(kilometers = 1):
     return kilometers / .000254

##  Convert milimeters to feet
#   @param milimeters (float)
#   @return (float)
def milimetersToFeet(milimeters = 1):
    return milimeters / 304.8

##  Convert centimeters to feet
#   @param centimeters (float)
#   @return (float)
def centimetersToFeet(centimeters = 1):
    return centimeters / 30.48

##  Convert meters to feet
#   @param meters (float)
#   @return (float)
def metersToFeet(meters = 1):
    return meters / 0.3048

## Convert kilometers to feet
#   @param kilometers (float)
#   @return (float)
def kilometersToFeet(kilometers = 1):
     return kilometers / 0.0003048

##  Convert milimeters to yards
#   @param milimeters (float)
#   @return (float)
def milimetersToYards(milimeters = 1):
    return milimeters / 914.4

##  Convert centimeters to yards
#   @param centimeters (float)
#   @return (float)
def centimetersToYards(centimeters = 1):
    return centimeters / 91.44

##  Convert meters to yards
#   @param meters (float)
#   @return (float)
def metersToYards(meters = 1):
    return meters / 0.9144

## Convert kilometers to yards
#   @param kilometers (float)
#   @return (float)
def kilometersToYards(kilometers = 1):
     return kilometers / .0009144

##  Convert milimeters to miles
#   @param milimeters (float)
#   @return (float)
def milimetersToMiles(milimeters = 1):
    return milimeters / 1609344

##  Convert centimeters to miles
#   @param centimeters (float)
#   @return (float)
def centimetersToMiles(centimeters = 1):
    return centimeters / 160934.4

##  Convert meters to miles
#   @param meters (float)
#   @return (float)
def metersToMiles(meters = 1):
    return meters / 1609.344

## Convert kilometers to yards
#   @param kilometers (float)
#   @return (float)
def kilometersToYards(kilometers = 1):
     return kilometers / 1.609344


########## Pressure Conversion ##########

#### English to ___

##  Convert psi to pascal
#   @param psi (float)
#   @return (float)
def psiToPascals(psi = 1):
    return psi * 6894.7572931783

##  Convert psi to kilopascals
#   @param psi (float)
#   @return (float)
def psiToKilopascals(psi = 1):
    return psi * 6.8947572931783

##  Convert psi to megapascals
#   @param psi (float)
#   @return (float)
def psiToKilopascals(psi = 1):
    return psi * 0.0068947572931783

##  Convert psi to bar
#   @param psi (float)
#   @return (float)
def psiToBar(psi = 1):
    return psi * 0.068947572931783


#### Metric to ___

## Convert pascals to psi
#   @param pascals (float)
#   @return (float)
def pascalsToPsi(pascals):
    return psi / 6894.7572931783

##  Convert megapascals to psi
#   @param psi (float)
#   @return (float)
def megapascalsToPsi(megapascals = 1):
    return megapascals / 6.8947572931783

##  Convert kilopascals to psi
#   @param psi (float)
#   @return (float)
def kilopascalsToPsi(kilopascals = 1):
    return kilopascals / 0.0068947572931783


########## Mass Conversions ##########

#### English to Metric



#### Metric to English


########## Force Conversions ##########

#### English to Metric

#### Metric to English


if __name__ == '__main__':
    print("12 Miles is ", milesToMilimters(12), " milimeters")
    print("Betyadidntknowthat")
