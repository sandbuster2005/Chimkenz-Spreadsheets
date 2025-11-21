from libs.printSpreadsheet import printScreen
import csv
import sys

from cursor import Cursor


csv.field_size_limit(sys.maxsize)

class ChimkenzSpreadsheet:
	def __init__(self,filepath):

		self.originX = 0
		self.originY = 0

		self.cursor = Cursor()

		self.spreadsheet = []
		with open(filepath , newline = "") as csvfile:
			spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
			for row in spamreader:
				self.spreadsheet.append(row)

	def updateScreen(self):
		printScreen(self.spreadsheet,self.originX,self.originY,8,cursor.X(),cursor.Y())            #add collumn size choosing when options are done









if __name__ == "__main__":
	chimkenzSpreadsheet("DIS_COM_UDI_2020.csv")