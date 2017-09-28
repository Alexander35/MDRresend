from csv_manager import CSV_Worker
from MDRresend_bot import MDRResend_bot
import configparser

def read_conf():
	config = configparser.ConfigParser()
	config.sections = []
	config.read('mdr.ini')
	return config

def main():
	CSVW = CSV_Worker('c:/Users/aivanov/МДРroute_status5.csv')
	data = CSVW.read_file()

	MDRR = MDRResend_bot(read_conf())
	[MDRR.resend_one(iden['ID']) for iden in data ]

if __name__ == '__main__':
	main()		