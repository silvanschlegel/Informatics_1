#!/usr/bin/env python3

# The purpose of this file is illustrating the class usages. This script
# is irrelevant for the grading and you can freely change its contents.

from combustion_car import CombustionCar
from electric_car import ElectricCar
from hybrid_car import HybridCar

h = HybridCar(40.0, 8.0, 25.0, 500.0)
h.drive(1000.0)
print(h.get_gas_tank_status())
print(h.get_battery_status())