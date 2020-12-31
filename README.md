[![GitHub license](https://img.shields.io/github/license/VamsiMudaliar/File-Based-Key-Valued-DataStore-?style=for-the-badge)](https://github.com/VamsiMudaliar/File-Based-Key-Valued-DataStore-/blob/master/LICENSE.txt)
[![GitHub stars](https://img.shields.io/github/stars/VamsiMudaliar/File-Based-Key-Valued-DataStore-?style=for-the-badge)](https://github.com/VamsiMudaliar/File-Based-Key-Valued-DataStore-/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/VamsiMudaliar/File-Based-Key-Valued-DataStore-?style=for-the-badge)](https://github.com/VamsiMudaliar/File-Based-Key-Valued-DataStore-/issues)
[![GitHub forks](https://img.shields.io/github/forks/VamsiMudaliar/File-Based-Key-Valued-DataStore-?style=for-the-badge)](https://github.com/VamsiMudaliar/File-Based-Key-Valued-DataStore-/network) 

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

__ABOUT__

__Built a file-Based Key-Value DataStore that supports the basic CRD(Create,read and delete) operations . 
This data store is meant to be used as a local storage for one single process on one laptop. The data store is exposed as a library
to the clients that can instantiate a class and work with the data store.__

The data store will support the following functional requirements

1. It can be initialized using an optional file path. if one is not provided, it will reliably create itself in a resonable location on the laptop

2. A New Key Value pair can be added to the data store using the create operation. The key is always a string- capped at 32 chars. the value is always a JSON object - capped at 16KB

3. If Create is invoked from an existing key, an appropriate error must be returned.

4. A Read operation on a key can be performed by providing a key, and recieving the value in response as a JSON object 

5. A Delete operation can be performed by providing a key

6. Every Key supports setting a TIME TO LIVE property when it is created. This property is optional. if provided it will be evaluated as an integer defining the number of seconds 
   the key must be retained in the data store Once the TIME TO LIVE for a key has epired, the key will no longer be available for read or delete operation

7. Appropriate error messages must always be returned to a client if it uses the data store in unexpected ways or breached any limits


The data Store will also support the following non functional requirements 

1. The size of the file storing the data must never exceed 1GB

2. More than on Client process cannot be allowed to use the same file as a data store at any given time.

3. A client process is allowed to accedd the data store using multiple threads (if it desires to )
   the data must therefore be THREAD-SAFE

4. The client will bear as little memory costs as possible to use this data store while deriving maximum performance with respect to response times for accessing the data store

__To Install run this command on CMD ( on windows )__

```
   pip install LocalDataStore
```

__All the CRUD operations are done on a JSON file which is created automatically when object is created__

> (Optional) Before using this package, try running the test_LocalDataStore file which contains few unit testcase it must roughly take 45 seconds to excute this file. 


**The Package LocalDataStore contains a Class DataStorageDB which contains the main functionality to use it in your code make this import statement**

```
from LocalDataStore import DataStorageDB
```
This Class mainly contains 4 functions which allows you to perform CRUD operations all these methods return a string stating the status of the operation

```

object = DataStorageDB()


Note: that the last parameter is optional and KEY should contain alphanumeric characters and cannot be more than 32 CHAR and VALUE can be at max 16 KB size else it reports ERROR

object.create("KEY","VALUE","TIME_TO_LIVE (in seconds) ")

desc: makes a {key,[value,TTL]} pair if the key is not present already else it reports ERROR

object.delete("KEY") 

desc: deletes the record with given key reports ERROR in case when there is no KEY present in DB or if the TLL property EXPIRES

object.read("KEY")

desc : reads the value of respective KEY provided the TTL still exists else it reports ERROR


object.update("KEY","VALUE","TIME_TO_LIVE (in seconds)")

desc : updates the KEY with the VALUE provided if in DB or if the TTL didnt expire in all other cases it throws error

```
