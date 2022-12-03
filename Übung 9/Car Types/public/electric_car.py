#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from car import Car

class ElectricCar(Car):

    def __init__(self, battery_size, battery_range_km):
        if not isinstance(battery_size,float) or not isinstance(battery_range_km, float):
            self.__battery_curr = 0
            raise Warning("Warning: Parameters must be floats")
        if battery_size<0 or battery_range_km<0:
            self.__battery_curr = 0
            raise Warning("Warning: Parameters must be positive!")
        self.__battery_size = battery_size
        self.__battery_range_km = battery_range_km
        self.__battery_curr = self.__battery_size
        self.__kwh_per_km = self.__battery_size/self.__battery_range_km

    def charge(self, kwh):
        if not isinstance(kwh, float):
            self.__battery_curr = 0
            raise Warning("Parameter must be float")
        if kwh < 0:
            self.__battery_curr = 0
            raise Warning("Parameter must be positive")
        if self.__battery_curr + kwh > self.__battery_size:
            self.__battery_curr = 0
            raise Warning("Warning: Charge is too big.")
        self.__battery_curr += kwh

    def get_battery_status(self):
        return (self.__battery_curr, self.__battery_size)

    def get_remaining_range(self):
        remaining_range = self.__battery_curr/self.__kwh_per_km
        return remaining_range

    def drive(self, dist):
        if not isinstance(dist,float):
            self.__battery_curr = 0
            raise Warning
        if dist < 0:
            self.__battery_curr = 0
            raise Warning
        if dist > self.__battery_curr/self.__kwh_per_km:
            self.__battery_curr = 0
            raise Warning(f"Warning: Distance is too far for current battery status. Remaining range with current charge is {self.__battery_curr*(self.__battery_range_km/100)}.")
        self.__battery_curr -= dist*self.__kwh_per_km
        if self.__battery_curr == 0.0:
            self.__battery_curr = int(0)