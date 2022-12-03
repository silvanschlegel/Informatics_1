#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from car import Car


class CombustionCar(Car):

    def __init__(self, gas_capacity, gas_per_100km):
        if not isinstance(gas_capacity, float) or not isinstance(gas_per_100km, float):
            self.__gas_curr = 0
            raise Warning("Warning: Parameters must be floats")
        if gas_capacity < 0 or gas_per_100km < 0:
            self.__gas_curr = 0
            raise Warning("Warning: Parameters must be positive!")
        self.__gas_max = gas_capacity  # float
        self.__gas_per_100km = gas_per_100km  # float
        self.__gas_curr = self.__gas_max  # float

    def fuel(self, f):
        if not isinstance(f, float):
            self.__gas_curr = 0
            raise Warning("Parameter must be float")
        if f < 0:
            self.__gas_curr = 0
            raise Warning("Parameter must be positive")
        if self.__gas_curr + f > self.__gas_max:
            self.__gas_curr = 0
            raise Warning("Warning: Too much fuel for this tank!")
        self.__gas_curr += f

    def get_gas_tank_status(self):
        return (self.__gas_curr, self.__gas_max)

    def get_remaining_range(self):
        remaining_range = self.__gas_curr / (self.__gas_per_100km / 100)
        return remaining_range

    def drive(self, dist):
        if not isinstance(dist, float):
            self.__gas_curr = 0
            raise Warning("Parameter must be of type float")
        if dist < 0.0:
            self.__gas_curr = 0
            raise Warning("Warning: driving distance must be positive")
        if dist * (self.__gas_per_100km / 100) > self.__gas_curr:
            self.__gas_curr = 0
            raise Warning("Warning: Distance too large, fuel tank depleted!")
        self.__gas_curr -= dist * (self.__gas_per_100km / 100)
        if self.__gas_curr == 0.0:
            self.__gas_curr = int(0)
