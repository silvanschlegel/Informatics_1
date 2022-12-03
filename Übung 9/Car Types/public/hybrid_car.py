#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from combustion_car import CombustionCar
from electric_car import ElectricCar


class HybridCar(CombustionCar, ElectricCar):

    def __init__(self, gas_capacity, gas_per_100km, battery_size, battery_range_km):
        CombustionCar.__init__(self, gas_capacity, gas_per_100km)
        ElectricCar.__init__(self, battery_size, battery_range_km)
        self.__electric_mode = True  # if false, car drives with fuel

    def switch_to_combustion(self):
        self.__electric_mode = False

    def switch_to_electric(self):
        self.__electric_mode = True

    def get_remaining_range(self):
        return ElectricCar.get_remaining_range(self) + CombustionCar.get_remaining_range(self)

    def drive(self, dist):
        if not isinstance(dist, float):
            raise Warning

        if ElectricCar.get_remaining_range(self) + CombustionCar.get_remaining_range(self) < dist:
            raise Warning("Warning: Distance too large.")

        if self.__electric_mode:
            if dist > ElectricCar.get_remaining_range(self):
                rest = ElectricCar.get_remaining_range(self)
                ElectricCar.drive(self, rest)
                ElectricCar.__battery_curr = 0
                self.__electric_mode = False
                CombustionCar.drive(self, (dist - rest))
                if CombustionCar.get_gas_tank_status(self) == 0.0:
                    CombustionCar.__gas_curr = 0
            else:
                ElectricCar.drive(self, dist)

        else:  # use gas
            if dist > CombustionCar.get_remaining_range(self):
                rest = CombustionCar.get_remaining_range(self)
                CombustionCar.drive(self, rest)
                CombustionCar.__gas_curr = 0
                self.__electric_mode = True
                ElectricCar.drive(self, (dist - rest))
                if ElectricCar.get_battery_status(self) == 0.0:
                    ElectricCar.__battery_curr = 0
            else:
                CombustionCar.drive(self, dist)

