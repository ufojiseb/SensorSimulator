from src.signal import Signal


class Sensor:
	def __init__(self, signal: Signal, floor: float, roof: float, precision: float) -> None:
		self.signal = signal
		self.floor = floor
		self.roof = roof
		self.precision = precision

	def value(self, time: float) -> float:
		val = self.signal.value(time)
		fraction = val % self.precision

		if fraction - (self.precision/2) < 0:
			sensor_val = val - fraction
		else:
			sensor_val = val + (self.precision - fraction)

		if sensor_val < self.floor:
			return self.floor
		if sensor_val > self.roof:
			return self.roof
		return sensor_val
