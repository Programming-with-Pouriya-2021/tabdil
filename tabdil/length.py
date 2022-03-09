


# this function converts sort of length units (kilometers,metres,centimetre) to millimeters

def millimeter(length_unit):
	unit_name = length_unit[0].lower()
	number = 1
	if unit_name == 'km':
		number = 1000 * 100 * 10 
	elif unit_name == 'm':
		number = 100 * 10 
	elif unit_name == 'cm':
		number = 10 
	elif unit_name == 'mi':
		number = 100 * 10 * 0.000621
	elif unit_name == 'mm':
		pass
	else:
		raise ValueError('unknown unit name {!r}'.format(unit_name))
	unit_number = length_unit[1]
	return unit_number * number