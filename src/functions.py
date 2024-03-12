import math


sin = math.sin
cos = math.cos
tan = math.tan


def sawtooth(time: float) -> float:
	val = time / (2 * math.pi) + 0.5
	fractional_part = val % 1

	return 2 * fractional_part - 1


def square(time: float) -> float:
	val = time / (2*math.pi) + 0.5
	fractional_part = val % 1

	return -1 if fractional_part < 0.5 else 1


def triangle(time: float) -> float:
	val = time / (2*math.pi)
	fractional_part = val % 1

	if fractional_part < 0.25:
		return 4*fractional_part
	elif 0.25 <= fractional_part < 0.75:
		return -4*fractional_part + 2
	else:
		return 4*fractional_part - 4
