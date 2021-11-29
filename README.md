# measurement_uncertainty

from agilent import Agilent

agilent = Agilent()

print(f"volt_direct(20): {agilent.volt_direct(20)}") input

print(f"volt_alternating(25, 50): {agilent.volt_alternating(25, 50)}") input, hz

print(f"ohm(100): {agilent.ohm(100)}") input

print(f"current_direct(1): {agilent.current_direct(1)}") input

print(f"current_alternating(1.343, 50): {agilent.current_alternating(1.343, 50)}") input, hz

print(f"voltage_ac_dc(1.343, 50): {agilent.voltage_ac_dc(1.343, 50)}") input, hz

print(f"current_ac_dc(1.343, 50): {agilent.current_ac_dc(1.343, 50)}") input, hz