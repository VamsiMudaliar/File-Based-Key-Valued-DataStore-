import unittest
import os
import time
from LocalDataStore import LocalStorageDB



app = LocalStorageDB()

class TestLocalDataStore(unittest.TestCase):
	
	def setUp(self):
		self.case_create_1 = app.create("Vamsi",23,60)
		self.case_create_2 = app.create("Rahul",32,10)
		self.case_create_3 = app.create("Mike",43,55)
		self.case_create_4 = app.create("Vamsi21",23,34)
		self.case_create_5 = app.create("Tokyo",22)

		self.case_delete_1 = app.delete("Vamsi")
		
		#self.case_read_1 = app.read("Rahul")
		time.sleep(11)

		self.case_delete_2 = app.delete("Rahul")
		
		self.case_read_1 = app.read("Tokyo")

		self.case_read_2 = app.read("Someone")

		self.case_update_1 = app.update("Tokyo",120,234)

		self.case_update_2 = app.update("Someone_not in list",20)

	def tearDown(self):
		pass

	def test_create(self):
		self.assertEqual(self.case_create_1,'Key Inserted Successfully.')

		self.assertEqual(self.case_create_2,'Key Inserted Successfully.')

		self.assertEqual(self.case_create_3,'Key Inserted Successfully.')

		self.assertEqual(self.case_create_4,'ERROR : Key Name not Valid ! \n Note : Key Name should only contain alphabets')

		self.assertEqual(self.case_create_5,'Key Inserted Successfully.')



	def test_delete(self):
		self.assertEqual(self.case_delete_1,'Key Deleted... \n')

		self.assertEqual(self.case_delete_2,"ERROR : Couldn't Delete, Key timer has Already Expired ... \n")#'ERROR : Couldn\'t Delete, Key timer has Already Expired ... \n')
		

	def test_read(self):
		#self.assertEqual(self.case_read_1,"ERROR : Timer Expired Key No Longer Present in Database")
		
		#self.assertEqual(self.case_read_2,"ERROR : Key Not Found in Database ! ")
		pass

	def test_update(self):
		#self.assertEqual(self.case_update_1,"ERROR : Couldn't Update, Key has Already Expired \n")

		#self.assertEqual(self.case_update_2,"ERROR : Key Not Found in Database")
		pass


if __name__ =='__main__':
	unittest.main()