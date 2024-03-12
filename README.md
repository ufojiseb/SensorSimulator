# SensorSimulator

Simulates the values that a sensor would return in a real-world scenario

## Requisites

SensorSimulator is a Python application that requires Matplotlib, which can be installed by running the command:

```
pip install matplotlib
```

or:

```
pip install -r requirements.txt
```

## Description

The project has three main classes:

|      |      |
| --- | --- |
| Waveform | Represents a simple wave, with its amplitude, frequency, phase, ... |
| Signal | Represents a real-world signal, which is the value of one or more waveforms plus or minus an error |
| Sensor | Represents a sensor, which has minimum and maximum operating values, and a precision |

One or more Waveforms are included in a Signal which in turn is included in a Sensor

# Configuration

The configuration is a json file containing a dictionary with the following keys:

|      |      |
| --- | --- |
| "simulation" | A dictionary containing the name and for how long to run the simulation |
| "waves" | A list of dictionaries, each one representing a waveform, containing the "min" and "max" values of the waveform, its frequency and phase, and the periodic function of the waveform (sin, cos, tan, sawtooth, square, triangle) |
| "signal" | A dictionary containing just the key "error", which is how much the real-world signal is far from the ideal waveform |
| "sensor" | A dictionary containing the keys "floor" and "roof", which represent the minimum and maximum values that the sensor is able to sense (e.g. a sensor with floor 10 sensing a real-world signal of 8.3 would return 10), and "precision", which represents the precision of the sensor (e.g. a sensor with precision 1 sensing a real-world signal of 7.2 would return 7) |

# Usage

In order to run the program, just type in a terminal:

```
python3 main.py
```

The program will run with the configuration specified in config.json, it will save the values in a .csv file, and will display a graph with all the values of the simulation
