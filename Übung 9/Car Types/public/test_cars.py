#!/usr/bin/env python3

from unittest import TestCase
from combustion_car import CombustionCar
from electric_car import ElectricCar
from hybrid_car import HybridCar


class TestCars(TestCase):

    def test_comb_remaining_range_1(self):
        c = CombustionCar(40.0, 8.0)
        self.assertAlmostEqual(500.0, c.get_remaining_range(), delta=0.001)

    def test_comb_remaining_range_2(self):
        c = CombustionCar(40.0, 8.0)
        c.drive(500.0)
        self.assertAlmostEqual(0.0, c.get_remaining_range(), delta=0.001)

    def test_comb_drive(self):
        c = CombustionCar(40.0, 8.0)
        c.drive(25.0)
        self.assertAlmostEqual(38.0, c.get_gas_tank_status()[0], delta=0.001)

    def test_comb_fuel(self):
        c = CombustionCar(40.0, 8.0)
        c.drive(500.0)
        c.fuel(40.0)
        self.assertAlmostEqual(500.0, c.get_remaining_range())

    def test_comb_drive_int(self):
        c = CombustionCar(40.0, 8.0)
        self.assertRaises(Warning,c.drive,500)

    def test_comb_fuel_int(self):
        c = CombustionCar(40.0, 8.0)
        self.assertRaises(Warning,c.fuel,500)

    def test_el_drive_int(self):
        c = ElectricCar(40.0, 500.0)
        self.assertRaises(Warning,c.drive,500)

    def test_el_charge_int(self):
        c = ElectricCar(40.0, 500.0)
        self.assertRaises(Warning,c.charge,500)

    def test_comb_fuel_too_much(self):
        c = CombustionCar(40.0, 8.0)
        c.drive(500.0)
        self.assertRaises(Warning, c.fuel, 40.0001)

    def test_comb_drive_too_far(self):
        c = CombustionCar(40.0, 8.0)
        self.assertRaises(Warning, c.drive, 500.001)

    def test_el_remaining_range_1(self):
        c = ElectricCar(100.0, 200.0)
        self.assertAlmostEqual(200, c.get_remaining_range(), delta=0.001)

    def test_el_remaining_range_2(self):
        c = ElectricCar(40.0, 80.0)
        c.drive(80.0)
        a = c.get_remaining_range()
        self.assertAlmostEqual(0.0, c.get_remaining_range(), delta=0.001)

    def test_el_drive(self):
        c = ElectricCar(40.0, 50.0)
        c.drive(25.0)
        self.assertAlmostEqual(25.0, c.get_remaining_range(), delta=0.001)

    def test_el_charge(self):
        c = ElectricCar(40.0, 500.0)
        c.drive(500.0)
        c.charge(40.0)
        self.assertAlmostEqual(500.0, c.get_remaining_range())

    def test_el_charge_too_much(self):
        c = ElectricCar(40.0, 500.0)
        c.drive(500.0)
        self.assertRaises(Warning, c.charge, 40.0001)

    def test_el_drive_too_far(self):
        c = ElectricCar(40.0, 500.0)
        self.assertRaises(Warning, c.drive, 500.001)

    def test_hybrid_basic(self):
        h = HybridCar(40.0, 8.0, 25.0, 500.0)
        h.switch_to_combustion()
        h.drive(600.0)  # depletes fuel, auto-switch
        self.assertAlmostEqual(20.0, h.get_battery_status()[0])

    def test_hybrid_basic_2(self):
        h = HybridCar(40.0, 8.0, 25.0, 500.0)
        h.drive(600.0)
        self.assertAlmostEqual(32.0, h.get_gas_tank_status()[0])

    def test_hybrid_drive_too_far(self):
        h = HybridCar(40.0, 8.0, 25.0, 500.0)
        self.assertRaises(Warning, h.drive, 200000)

    def test_hybrid_wrong_parameters_1(self):
        self.assertRaises(Warning, HybridCar, "Car", "Car", "Car", "car")

    def test_hybrid_wrong_parameters_2(self):
        self.assertRaises(Warning, HybridCar, -40.0, 8.0, 25.0, 500.0)

    def test_hybrid_drive_int(self):
        c = HybridCar(40.0, 8.0, 25.0, 500.0)
        self.assertRaises(Warning,c.drive,500)

    # This current test suite only contains very basic test cases. By now,
    # you have some experience in writing test cases. We strongly encourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test&Run' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.
