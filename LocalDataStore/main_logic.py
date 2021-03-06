import time
from threading import Thread
import json
from json.decoder import JSONDecodeError

FILE_LIMIT = 1024*1024*1024 # 1GB

KEY_LIMIT = 32 # max 32 characters

VALUE_LIMIT = 16*1024*1024 #16KB

MAX_CONNECTIONS = 1 # no of connections

DEFAULT_LOCATION = "./"

cache={} # our local DB
	

PATH_FORMED = DEFAULT_LOCATION + "new_obj.json"

class LocalStorageDB():

	def __init__(self):
		pass

	def create(self,key,value,time_to_live=0):
		
				# load on the data from a json file
		try:
			with open(PATH_FORMED) as f:
						
				old_cache=json.load(f)

				new_cache=old_cache

				if key in new_cache:				
					print(f"ERROR : Key {key} Already Present...")

				elif key.isalpha():

					curr_record=[]

					if len(cache)<FILE_LIMIT and value<=VALUE_LIMIT:

						if time_to_live==0: 
									#set to default
							curr_record=[value,time_to_live]
						else:
									
							curr_record=[value,time.time()+time_to_live]
									# check if key is atmost 32 chars
									
							if len(key)<=KEY_LIMIT:
									
								new_cache[key]=curr_record

								with open(PATH_FORMED,"w") as fl:
									json.dump(new_cache,fl,indent=2)

								print(f"Key {key} Inserted Successfully.")
							else:
								print("ERROR : Memory Limit Exceed !  \n Note : File size and inserting value should be no more than 1GB and 16KB ")
					else:
						print(f"ERROR : Key Name not Valid ! \n Note : Key Name should only contain alphabets and can be at max {KEY_LIMIT} size")
							#print(f"Note : Key Name should only contain alphabets and can be at max {KEY_LIMIT} size")
		except JSONDecodeError as er:
			pass
	# READ Operation in the file

	def read(self,key):
		
		
			try:

				with open(PATH_FORMED) as f:
					
					old_cache=json.load(f)
					
					new_cache=old_cache

					if key not in new_cache:
						print("ERROR : Key Not Found in Database ! ")

					else:
						store_tmp = new_cache[key]

						pattern = "{ " + str(key)+": "+str(store_tmp[0]) + " }"

						if store_tmp[1]!=0:
								
							if time.time() < store_tmp[1]: 
								return pattern
							else:
								print("ERROR : Timer Expired Key No Longer Present in Database")
						else:
							return pattern
			except JSONDecodeError as er:
				pass



	def delete(self,key):
		
		try:

			with open(PATH_FORMED) as f:
				old_cache=json.load(f)

				new_cache=old_cache

				if key not in new_cache:
					print(f"ERROR : Key {key} Not Found in Database \n")
				
				else:
					store_tmp = new_cache[key]

					if store_tmp[1]!=0:
						if time.time()<store_tmp[1]:
							del new_cache[key]
							print(f"Key {key} Deleted... \n")
						else:
							print(f"ERROR : Couldn't Delete, Key {key} has Already Expired ... \n")
					else:
						del new_cache[key]
						print(f"Key {key} Deleted... \n")

					with open(PATH_FORMED,'w') as f:
						json.dump(new_cache,f,indent=2)

		except JSONDecodeError as er:
			pass

	# Update Function to Update the key Value before it expires

	def update(self,key , value, timer=0):
		
		try:
			with open(PATH_FORMED) as ft:
				old_cache = json.load(ft)

				new_cache=old_cache

				if key not in new_cache:
					print("ERROR : Key Not Found in Database")

				else:
					store_tmp = new_cache[key]

					if time.time()<store_tmp[1] or store_tmp[1]==0:
						
						if timer>0:
							new_value = [value,timer]
						else:
							new_value = [value,store_tmp[1]]

						new_cache[key] = new_value

						with open(PATH_FORMED,"w") as fte:
							json.dump(new_cache,fte,indent=2)

						print("Values Updated..")
					else:
						print("ERROR : Couldn't Update, Key has Already Expired \n")

		except JSONDecodeError as er:
			pass

