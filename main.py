import matplotlib.pyplot as plt

from src.waveform import Waveform
from src.signal import Signal
from src.sensor import Sensor
from src.save_data import save

from src.config import load as load_config


def main() -> None:
	config = load_config("config.json")

	csimulation = config.get("simulation")
	cwaves = config.get("waves")
	csignal = config.get("signal")
	csensor = config.get("sensor")

	waves = [
		Waveform(
			amplitude = (cwave.get("max") - cwave.get("min")) / 2,
			average = cwave.get("min") + (cwave.get("max") - cwave.get("min")) / 2,
			frequency = cwave.get("frequency"),
			phase = cwave.get("phase"),
			function = cwave.get("function")
		)
		for cwave in cwaves
	]

	signal = Signal(
		waves = waves,
		error = (-csignal.get("error"), csignal.get("error"))
	)

	sensor = Sensor(
		signal = signal,
		floor = csensor.get("floor"),
		roof = csensor.get("roof"),
		precision = csensor.get("precision")
	)

	values = [sensor.value(t) for t in range(csimulation.get("time"))]

	save(csimulation.get("name") + ".csv", enumerate(values))

	plt.plot(values)
	plt.title('Sensor values')
	plt.xlabel('Time')
	plt.ylabel('Value')
	plt.show()


if __name__ == "__main__":
	main()
