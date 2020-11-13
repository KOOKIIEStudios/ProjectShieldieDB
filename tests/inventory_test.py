"""This is a unit test for checking basic Inventory handling functionality

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
import pytest
from swordie_db.database import SwordieDB

@pytest.fixture
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

# Test non-cash equipped
def test_fetch_equipped_itemid(inventory):
	assert inventory.equipped_inv[1]["itemid"] == 1002140,  \
		f"Error encountered whilst directly fetching item ID from bagindex: \n" \
		f"Expected: 1002140 (Int); Encountered: {inventory.equipped_inv[1]['itemid']}, " \
		f"Type: {type(inventory.equipped_inv[1]['itemid'])}"

def test_fetch_equipped_quantity(inventory):
	assert inventory.equipped_inv[1]["quantity"] == 1,  \
		f"Error encountered whilst directly fetching item qty from bagindex: \n" \
		f"Expected: 1 (Int); Encountered: {inventory.equipped_inv[1]['quantity']}, " \
		f"Type: {type(inventory.equipped_inv[1]['quantity'])}"

def test_is_equipped(inventory):
	assert inventory.is_equipping(1002140), \
		f"Error encountered whilst checking if non-cash equip is worn: \n" \
		f"Expected: True (Bool); Encountered: {inventory.is_equipping(1002140)}, " \
		f"Type: {type(inventory.is_equipping(1002140))}"
	assert not inventory.is_equipping(1002141), \
		f"Error encountered whilst checking for false positives, for whether non-cash equip is worn: \n" \
		f"Expected: True (Bool); Encountered: {inventory.is_equipping(1002141)}, " \
		f"Type: {type(inventory.is_equipping(1002141))}"

# Test cash equipped
def test_fetch_cash_equipped_itemid(inventory):
	assert inventory.equipped_inv[11]["itemid"] == 1702121,  \
		f"Error encountered whilst directly fetching item ID from bagindex: \n" \
		f"Expected: 1702121 (Int); Encountered: {inventory.equipped_inv[11]['itemid']}, " \
		f"Type: {type(inventory.equipped_inv[11]['itemid'])}"

def test_fetch_cash_equipped_quantity(inventory):
	assert inventory.equipped_inv[11]["quantity"] == 1,  \
		f"Error encountered whilst directly fetching item qty from bagindex: \n" \
		f"Expected: 1 (Int); Encountered: {inventory.equipped_inv[11]['quantity']}, " \
		f"Type: {type(inventory.equipped_inv[11]['quantity'])}"

def test_is_cash_equipped(inventory):
	assert inventory.is_equipping(1702121), \
		f"Error encountered whilst checking if cash equip is worn: \n" \
		f"Expected: True (Bool); Encountered: {inventory.is_equipping(1702121)}, " \
		f"Type: {type(inventory.is_equipping(1702121))}"
	assert not inventory.is_equipping(1702122), \
		f"Error encountered whilst checking for false positives, for whether cash equip is worn: \n" \
		f"Expected: True (Bool); Encountered: {inventory.is_equipping(1702122)}, " \
		f"Type: {type(inventory.is_equipping(1702122))}"

# Test non-cash equip
def test_fetch_equip_itemid(inventory):
	assert inventory.equip_inv[10]["itemid"] == 1002140,  \
		f"Error encountered whilst directly fetching item ID from bagindex: \n" \
		f"Expected: 1002140 (Int); Encountered: {inventory.equip_inv[10]['itemid']}, " \
		f"Type: {type(inventory.equip_inv[10]['itemid'])}"

def test_fetch_equip_quantity(inventory):
	assert inventory.equip_inv[10]["quantity"] == 1,  \
		f"Error encountered whilst directly fetching item qty from bagindex: \n" \
		f"Expected: 1 (Int); Encountered: {inventory.equip_inv[10]['quantity']}, " \
		f"Type: {type(inventory.equip_inv[10]['quantity'])}"

def test_is_in_equip(inventory):
	assert inventory.has_item_in_equip(1002140), \
		f"Error encountered whilst checking if non-cash equip is in inventory: \n" \
		f"Expected: True (Bool); Encountered: {inventory.has_item_in_equip(1002140)}, " \
		f"Type: {type(inventory.has_item_in_equip(1002140))}"
	assert not inventory.has_item_in_equip(1002141), \
		f"Error encountered whilst checking for false positives, for whether non-cash equip is in inventory: \n" \
		f"Expected: True (Bool); Encountered: {inventory.has_item_in_equip(1002141)}, " \
		f"Type: {type(inventory.has_item_in_equip(1002141))}"

# Test cash equip
def test_fetch_cash_equip_itemid(inventory):
	assert inventory.equip_inv[11]["itemid"] == 1702121,  \
		f"Error encountered whilst directly fetching item ID from bagindex: \n" \
		f"Expected: 1702121 (Int); Encountered: {inventory.equip_inv[11]['itemid']}, " \
		f"Type: {type(inventory.equip_inv[11]['itemid'])}"

def test_fetch_cash_equip_quantity(inventory):
	assert inventory.equip_inv[11]["quantity"] == 1,  \
		f"Error encountered whilst directly fetching item qty from bagindex: \n" \
		f"Expected: 1 (Int); Encountered: {inventory.equip_inv[11]['quantity']}, " \
		f"Type: {type(inventory.equip_inv[11]['quantity'])}"

def test_cash_is_in_equip(inventory):
	assert inventory.has_item_in_equip(1702121), \
		f"Error encountered whilst checking if cash equip is in inventory: \n" \
		f"Expected: True (Bool); Encountered: {inventory.has_item_in_equip(1702121)}, " \
		f"Type: {type(inventory.has_item_in_equip(1702121))}"
	assert not inventory.has_item_in_equip(1702122), \
		f"Error encountered whilst checking for false positives, for whether cash equip is in inventory: \n" \
		f"Expected: True (Bool); Encountered: {inventory.has_item_in_equip(1702122)}, " \
		f"Type: {type(inventory.has_item_in_equip(1702122))}"

# Test non-cash use
def test_fetch_use_itemid(inventory):
	assert inventory.consume_inv[10]["itemid"] == 2070019,  \
		f"Error encountered whilst directly fetching item ID from bagindex: \n" \
		f"Expected: 2070019 (Int); Encountered: {inventory.consume_inv[10]['itemid']}, " \
		f"Type: {type(inventory.consume_inv[10]['itemid'])}"

def test_fetch_use_quantity(inventory):
	assert inventory.consume_inv[10]["quantity"] == 31,  \
		f"Error encountered whilst directly fetching item qty from bagindex: \n" \
		f"Expected: 31 (Int); Encountered: {inventory.consume_inv[10]['quantity']}, " \
		f"Type: {type(inventory.consume_inv[10]['quantity'])}"

def test_is_in_use(inventory):
	assert inventory.has_item_in_consume(2070019), \
		f"Error encountered whilst checking if non-cash USE is in inventory: \n" \
		f"Expected: True (Bool); Encountered: {inventory.has_item_in_consume(2070019)}, " \
		f"Type: {type(inventory.has_item_in_consume(2070019))}"
	assert not inventory.has_item_in_consume(2070020), \
		f"Error encountered whilst checking for false positives, for whether non-cash USE is in inventory: \n" \
		f"Expected: True (Bool); Encountered: {inventory.has_item_in_consume(2070020)}, " \
		f"Type: {type(inventory.has_item_in_consume(2070020))}"

# Test cash equip
def test_fetch_cash_use_itemid(inventory):
	assert inventory.consume_inv[11]["itemid"] == 2023177,  \
		f"Error encountered whilst directly fetching item ID from bagindex: \n" \
		f"Expected: 2023177 (Int); Encountered: {inventory.consume_inv[11]['itemid']}, " \
		f"Type: {type(inventory.consume_inv[11]['itemid'])}"

def test_fetch_cash_use_quantity(inventory):
	assert inventory.consume_inv[11]["quantity"] == 31,  \
		f"Error encountered whilst directly fetching item qty from bagindex: \n" \
		f"Expected: 31 (Int); Encountered: {inventory.consume_inv[11]['quantity']}, " \
		f"Type: {type(inventory.consume_inv[11]['quantity'])}"

def test_cash_is_in_use(inventory):
	assert inventory.has_item_in_consume(2023177), \
		f"Error encountered whilst checking if non-cash USE is in inventory: \n" \
		f"Expected: True (Bool); Encountered: {inventory.has_item_in_consume(2023177)}, " \
		f"Type: {type(inventory.has_item_in_consume(2023177))}"
	assert not inventory.has_item_in_consume(2023178), \
		f"Error encountered whilst checking for false positives, for whether non-cash USE is in inventory: \n" \
		f"Expected: True (Bool); Encountered: {inventory.has_item_in_consume(2023178)}, " \
		f"Type: {type(inventory.has_item_in_consume(2023178))}"

# Test ETC
def test_fetch_etc_itemid(inventory):
	assert inventory.etc_inv[10]["itemid"] == 4031922,  \
		f"Error encountered whilst directly fetching item ID from bagindex: \n" \
		f"Expected: 4031922 (Int); Encountered: {inventory.etc_inv[10]['itemid']}, " \
		f"Type: {type(inventory.etc_inv[10]['itemid'])}"

def test_fetch_etc_quantity(inventory):
	assert inventory.etc_inv[10]["quantity"] == 3,  \
		f"Error encountered whilst directly fetching item qty from bagindex: \n" \
		f"Expected: 3 (Int); Encountered: {inventory.etc_inv[10]['quantity']}, " \
		f"Type: {type(inventory.etc_inv[10]['quantity'])}"

def test_is_in_etc(inventory):
	assert inventory.has_item_in_etc(4031922), \
		f"Error encountered whilst checking if ETC is in inventory: \n" \
		f"Expected: True (Bool); Encountered: {inventory.has_item_in_etc(4031922)}, " \
		f"Type: {type(inventory.has_item_in_etc(4031922))}"
	assert not inventory.has_item_in_etc(4031923), \
		f"Error encountered whilst checking for false positives, for whether ETC is in inventory: \n" \
		f"Expected: True (Bool); Encountered: {inventory.has_item_in_etc(4031923)}, " \
		f"Type: {type(inventory.has_item_in_etc(4031923))}"

# Test SETUP
def test_fetch_setup_itemid(inventory):
	assert inventory.install_inv[10]["itemid"] == 3015025,  \
		f"Error encountered whilst directly fetching item ID from bagindex: \n" \
		f"Expected: 3015025 (Int); Encountered: {inventory.install_inv[10]['itemid']}, " \
		f"Type: {type(inventory.install_inv[10]['itemid'])}"

def test_fetch_setup_quantity(inventory):
	assert inventory.install_inv[10]["quantity"] == 1,  \
		f"Error encountered whilst directly fetching item qty from bagindex: \n" \
		f"Expected: 1 (Int); Encountered: {inventory.install_inv[10]['quantity']}, " \
		f"Type: {type(inventory.install_inv[10]['quantity'])}"

def test_is_in_setup(inventory):
	assert inventory.has_item_in_install(3015025), \
		f"Error encountered whilst checking if SETUP is in inventory: \n" \
		f"Expected: True (Bool); Encountered: {inventory.has_item_in_install(3015025)}, " \
		f"Type: {type(inventory.has_item_in_install(3015025))}"
	assert not inventory.has_item_in_install(3015026), \
		f"Error encountered whilst checking for false positives, for whether SETUP is in inventory: \n" \
		f"Expected: True (Bool); Encountered: {inventory.has_item_in_install(3015026)}, " \
		f"Type: {type(inventory.has_item_in_install(3015026))}"

# Test CASH
def test_fetch_cash_itemid(inventory):
	assert inventory.cash_inv[10]["itemid"] == 5040004,  \
		f"Error encountered whilst directly fetching item ID from bagindex: \n" \
		f"Expected: 5040004 (Int); Encountered: {inventory.cash_inv[10]['itemid']}, " \
		f"Type: {type(inventory.cash_inv[10]['itemid'])}"

def test_fetch_cash_quantity(inventory):
	assert inventory.cash_inv[10]["quantity"] == 1,  \
		f"Error encountered whilst directly fetching item qty from bagindex: \n" \
		f"Expected: 1 (Int); Encountered: {inventory.cash_inv[10]['quantity']}, " \
		f"Type: {type(inventory.cash_inv[10]['quantity'])}"

def test_is_in_cash(inventory):
	assert inventory.has_item_in_cash(5040004), \
		f"Error encountered whilst checking if CASH is in inventory: \n" \
		f"Expected: True (Bool); Encountered: {inventory.has_item_in_cash(5040004)}, " \
		f"Type: {type(inventory.has_item_in_cash(5040004))}"
	assert not inventory.has_item_in_cash(5040005), \
		f"Error encountered whilst checking for false positives, for whether CASH is in inventory: \n" \
		f"Expected: True (Bool); Encountered: {inventory.has_item_in_cash(5040005)}, " \
		f"Type: {type(inventory.has_item_in_cash(5040005))}"
