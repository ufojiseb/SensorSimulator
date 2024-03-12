import csv


def save(filename: str, data: list) -> None:
	with open(filename, 'w', newline='') as save_file:
		wr = csv.writer(save_file, quoting=csv.QUOTE_ALL)

		for t in data:
			wr.writerow(t)
