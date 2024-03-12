import json

from src.functions import *


def load(filename: str):
	with open(filename, "r", encoding="utf-8") as fin:
		conf = json.load(fin)

	matches = [
		("sin", sin),
		("cos", cos),
		("tan", tan),
		("sawtooth", sawtooth),
		("square", square),
		("triangle", triangle)
	]

	# matches each function name (str) to the corresponding function (callable)
	for wave in conf.get("waves"):
		for name, function in matches:
			if wave.get("function") == name:
				wave["function"] = function

	return conf
