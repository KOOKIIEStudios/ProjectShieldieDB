"""This is a timing benchmarking test for checking the has_item_in_equip method in swordie_db

NOTE: This script needs to be in the same directory as the swordie_db module.
This can be run directly for a quick test of functionality (alter DB attributes prior to use).
To set up the DB for use, first follow the SwordieMS guide for setting up
a Swordie-based DB. Then, use the script in the SQLScripts folder of this
project to create a tester account. Once it's been successfully run, you can
use this script to test the functionality of SwordieDB APIs.
Note that you may re-run the SQL script to reset the tester char to
baseline values, if desired.
Copyright KOOKIIE Studios 2020. All rights reserved.
"""
from timeit import default_timer as timer
from swordie_db.database import SwordieDB

def inventory():
	"""Returns a tester Character instance"""
	# Import DB
	try:
		spirit = SwordieDB(host="127.0.0.1", password="", user="root", schema="spirit", port=3306)
	except Exception as e:
		print(f"Error has occurred whist attempting to load DB: \n{e}")
		sys.exit(0)
	character = spirit.get_char_by_name("tester")
	if character == None:
		print("CRITICAL ERROR: UNABLE TO FETCH CHARACTER BY NAME! TERMINATING...")
		sys.exit(0)
	inventory = character.inventory
	return inventory
	
def test_is_in_equip(inventory, item, iterations):
	for n in range(iterations):
		inventory.has_item_in_equip(item)

# Define new mthod here for comparision:
#def test_other_method(inventory, iterations):
# 	for n in range(iterations):
		# New method goes here

def time_method(method, item, iterations):
	start = timer()
	method(inventory, item, iterations)
	end = timer()
	return start, end

inventory = inventory()
iterations = 100000  # 100,000 iterations
item = 1002140
print(f"Attempting {iterations} iterations for better precision")
start, end = time_method(test_is_in_equip, item, iterations)
print(f"Time taken: {end - start}seconds") # Time in seconds, e.g. 5.38091952400282

# Uncomment the following for new method:
# print(f"Attempting {iterations} iterations for better precision")
# start, end = time_method(test_other_method, iterations)
# print(f"Time taken for new method: {end - start}seconds") # Time in seconds, e.g. 5.38091952400282

