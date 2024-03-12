import random
from typing import Tuple, List

from src.waveform import Waveform


class Signal:
	def __init__(self, waves: List[Waveform], error: Tuple[int, int]) -> None:
		self.waves = waves
		self.min, self.max = error

	def value(self, time: float) -> float:
		error = random.uniform(self.min, self.max)
		val = sum([wave.value(time) for wave in self.waves])
		return val + error
