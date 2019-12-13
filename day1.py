module_masses_and_expected_fuel = [ 
	(12, 2), 
	(14, 2), 
	(1969, 654), 
	(100756, 33583),
	(2, 0)
]

total_expected_fuel_for_moduels_with_masses = [
	(14, 2),
	(1969, 966),
	(100756, 50346)
]


def required_fuel_for_mass(mass):
	required_fuel = mass // 3 - 2
	if required_fuel > 0:
		return required_fuel
	else:
		return 0

def required_fuel_for_module(mass):
	required_fuel = 0
	fuel_to_add = required_fuel_for_mass(mass)
	while fuel_to_add > 0:
		required_fuel += fuel_to_add
		fuel_to_add = required_fuel_for_mass(fuel_to_add)
	return required_fuel 

def test_required_fuel_for_mass():
	for mass, expected in module_masses_and_expected_fuel:
		calculated_fuel = required_fuel_for_mass(mass)
		if calculated_fuel == expected:
			print("PASS: Required fuel for mass {} is {}".format(mass, expected))
		else:
			print("FAIL: Required fuel for mass {} is {}, calculated fuel was {}".format(mass, expected, calculated_fuel))

def test_required_fuel_for_module():
	for mass, expected in total_expected_fuel_for_moduels_with_masses:
		calculated_fuel = required_fuel_for_module(mass)
		if calculated_fuel == expected:
			print("PASS: Required fuel for module with mass {} is {}".format(mass, expected))
		else:
			print("FAIL: Required fuel for module with mass {} is {}, calculated fuel was {}".format(mass, expected, calculated_fuel))

def sum_fuel_for_moduels(module_masses):
	sum = 0
	for mass in module_masses:
		sum += required_fuel_for_mass(mass)
	return sum

def test_fuel_for_moduels():
	expected_sum = 0
	masses = []
	for mass, expected in module_masses_and_expected_fuel:
		expected_sum += expected
		masses.append(mass)
	sum_fuel = sum_fuel_for_moduels(masses)
	if sum_fuel == expected_sum:
		print("PASS: The sum of the fuel for the provided masses is {}".format(expected_sum))
	else:
		print("FAIL: The expected sum is {}, but the calculated sum was {}.".format(expected_sum, sum_fuel))

def sum_total_fuel_for_modules(module_masses):
	sum = 0
	for mass in module_masses:
		sum += required_fuel_for_module(mass)
	return sum

print("Day 1: 1")
test_required_fuel_for_mass()
test_fuel_for_moduels()

input = open('input-files/input_day1_1.txt', 'r')
masses = []
for line in input:
	masses.append(int(line))

print("----\n The sum is {}.\n ----".format(sum_fuel_for_moduels(masses)))
print("Day 1: 2")
test_required_fuel_for_module()
print("----\n The sum is {}.\n ----".format(sum_total_fuel_for_modules(masses)))

