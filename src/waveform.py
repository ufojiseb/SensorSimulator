from math import pi

from typing import Callable


class Waveform:
	def __init__(self, amplitude: float, average: float, frequency: float, phase: float, function: Callable) -> None:
		self.amplitude = amplitude
		self.average = average
		self.frequency = frequency
		self.phase = phase
		self.function = function

	def value(self, time: float) -> float:
		f = self.frequency
		fun = self.function
		A = self.amplitude
		m = self.average
		phase = self.phase

		return A * fun(2*pi*f*time + phase) + m
