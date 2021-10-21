##  @file Units.py
#   File containing the ValueWithUnits class and associated framework
#
#   Relies on the UnitConversion.py file for a collection of conversion functions
#
#   @author Jeremy Dunne
#   @date October, 2021
#   @version V0.1.0
#   In progress, use with caution
#   Add functionality (specifically in conversion process) as the need arises

from easyunits import unit_conversion

class UnsuportedUnitError(Exception):
    def __init__(self, unit):
        self.message = 'Unsupported Unit Type: ' + str(unit)
        super().__init__(self.message)

class UnsupportedConverstionError(Exception):
    def __init__(self, base, target):
        self.message = 'Units.py Unsupported Converstion of ' + base + ' to ' + target + '. Please implement!'
        super().__init__(self.message)

class NoUnitError(Exception):
    def __init__(self):
        self.message = 'No unit given, unable to perform converstion'
        super().__init__(self.message)

##  Class to handle float values with unit tags
#
#   Joins a value (float) with a unit tag (str). Attempts to handle conversions
#   as it is capable
class ValueWithUnits():
    supported_units = [
        # distances
        'inches', 'feet', 'yards', 'miles',
        'in', 'ft', 'yds',
        'milimeters', 'centimeters', 'meters', 'kilometers',
        'mm', 'cm', 'm', 'km',
        # weight/mass
        'pounds', 'tons'
        'grams', 'kilograms',
        # pressure
        'psi',
        'pascals', 'kilopascals', 'megapascals'
        'bar'
        #
    ]

    ##  class constructor
    #   Can raise UnsuportedUnitError if unit is not recognized and custom is False
    #
    #   @param self object pointer
    #   @param value (float) optional assigned value
    #   @param unit (str) optional unit tag
    #   @param custom (bool) override for checking that the unit is supported
    def __init__(self, value = None, unit = None, custom = False):
        if value is not None:
            self.value = value
        else:
            self.value = float('NaN')
        if unit is not None:
            self.unit = unit
            if not custom:
                self.checkUnits(self.unit)
        else:
            self.unit = ''
        self.custom = custom



    ##  Checks if the unit is in the supported types
    #   Raises UnsuportedUnitError if the unit is not found
    #   @param self object pointer
    #   @param unit (str) unit tag
    def checkUnits(self, unit):
        # check if the unit is 'officially' supported
        if unit not in self.supported_units:
            raise UnsuportedUnitError(unit)

    ##  Get the value of the object
    #   @param self object pointer
    #   @return (float)
    def getValue(self):
        return self.value, self.unit

    ##  Convert the object value into a target unit
    #   Raises the NoUnitError or the UnsupportedConverstionError
    #   @param self object pointer
    #   @param target_unit (str) target unit tag
    #   @return (float)
    def convert(self, target_unit):
        # this is going to be an interesting method
        if self.custom:
            raise NoUnitError()

        # check if the target unit is supported
        self.checkUnits(target_unit)

        # check the current unit
        value = None
        #### length converstions
        if self.unit == 'inches':
            value = self.convertFromInches(target_unit)


        if value is None:
            raise UnsupportedConverstionError(self.unit, target_unit)
        return value


    ##  Convert to inches
    #
    #   @param self object pointer
    #   @param target_unit (str) target conversion tag
    #   @return (float) or None
    def convertFromInches(self, target_unit):
        #### English to English
        if target_unit == 'feet' or target_unit == 'ft':
            return inchesToFeet(self.value)
        if target_unit == 'yards' or target_unit == 'yd':
            return inchesToYards(self.value)
        if target_unit == 'miles':
            return inchesToMiles(self.value)

        #### English to Metric
        if target_unit == 'milimeters' or target_unit == 'mm':
            return unit_conversion.inchesToMilimeters(self.value)
        if target_unit == 'centimeters' or target_unit == 'cm':
            return inchesToCentimeters(self.value)
        if target_unit == 'meters' or target_unit == 'm':
            return inchesToMeters(self.value)
        if target_unit == 'kilometers' or target_unit == 'km':
            return inchesToKilometers(self.value)

        return None


if __name__ == '__main__':

    """
    # try a blank
    blank = ValueWithUnits()
    blank_value, blank_unit = blank.getValue()
    print("Blank Value: " + str(blank_value) + ' ' + str(blank_unit))
    # try a real unit
    inch = ValueWithUnits(12.3,'inches')
    inch_value, inch_unit = inch.getValue()
    print("Inch Value: " + str(inch_value) + ' ' + str(inch_unit))
    # this should not raise an exception
    furlong = ValueWithUnits(2,'furlongs',True)
    furlong_value, furlong_unit = furlong.getValue()
    print("Furlong Value: " + str(furlong_value) + ' ' + str(furlong_unit))
    # this should raise an exception
    try:
        fortnight = ValueWithUnits(3, 'fortnights')
    except UnsuportedUnitError as error:
        print(error)

    """

    inches = ValueWithUnits(25.3, 'inches')
    mm = inches.convert('mm')
    inches_value, inches_units = inches.getValue()
    print(inches_value, inches_units, ' is ', mm, 'mm')
