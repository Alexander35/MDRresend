import csv
from log import logger_setup

class CSV_Worker:
	def __init__(self, csv_filename):
		self.csv_filename = csv_filename
		self.logger = logger_setup(__name__)	

	def read_file(self):
		with open(self.csv_filename) as csvfile:
			spamreader = csv.reader(csvfile, dialect=csv.unix_dialect, delimiter=',', quotechar='"')
			data_queue = [{'ID' : row[0], 'GUID' : row[2] }   for row in spamreader]
			self.logger.info('Init data has been read')
			self.logger.info('Data length - {}'.format( len(data_queue)))
			self.logger.info(data_queue)
		return data_queue		

def main():
	CSVW = CSV_Worker('c:/Users/aivanov/МДРroute_status5.csv')
	data = CSVW.read_file()

if __name__ == '__main__':
	main()