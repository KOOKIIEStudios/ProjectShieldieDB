"""This is a unit test for checking basic functionality

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
def char():
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
	return character
	
@pytest.fixture
def user_id():
	"""Returns user ID of tester Character instance"""
	# Import DB
	try:
		spirit = SwordieDB(host="127.0.0.1", password="", user="root", schema="spirit", port=3306)
	except Exception as e:
		print(f"Error has occurred whist attempting to load DB: \n{e}")
		sys.exit(0)
	user_ID = spirit.get_user_id_by_name("tester")
	if user_ID == None:
		print("CRITICAL ERROR: UNABLE TO FETCH USER ID BY NAME! TERMINATING...")
		sys.exit(0)
	return user_ID

# Character info fetching tests
def test_fetch_char_info(char):
	assert char.name == "tester", f"Critical Error: Name test failed! Name: {char.name}; Type: {type(char.name)}"
	assert char.meso == "0", f"Meso test failed! Meso count: {char.meso}; Type: {type(char.meso)}"
	assert char.fame == 0, f"Fame test failed! Fame count: {char.fame}; Type: {type(char.fame)}"
	job = char.get_job_name()  # return job name from ID via Hashmap; String
	assert job == "Beginner", f"Job name test failed! Job name: {job}; Type: {type(job)}"
	assert char.job == 0, f"Job ID test failed! Job ID: {char.job}; Type: {type(char.job)}"
	assert char.level == 1, f"Character level test failed! Level count: {char.level}; Type: {type(char.level)}"
	honor_exp = char.get_stat_by_column("honorexp")  # Int
	assert honor_exp == 0, f"Honour EXP test failed! Honour count: {honor_exp}; Type: {type(honor_exp)}"

	assert char.map == "4000011", f"Map ID test failed! Map ID: {char.map}; Type: {type(char.map)}"
	assert char.face == 23300, f"Face ID test failed! Face ID: {char.face}; Type: {type(char.face)}"
	assert char.hair == 36786, f"Hair ID test failed! Hair ID: {char.hair}; Type: {type(char.hair)}"
	assert char.skin == 0, f"Skin ID test failed! Skin ID: {char.skin}; Type: {type(char.skin)}"
	assert char.exp == "0", f"EXP test failed! EXP amount: {char.exp}; Type: {type(char.exp)}"

	assert char.strength == 12, f"STR test failed! STR amount: {char.strength}; Type: {type(char.strength)}"
	assert char.dex == 5, f"DEX test failed! DEX amount: {char.dex}; Type: {type(char.dex)}"
	assert char.inte == 4, f"INT test failed! INT amount: {char.inte}; Type: {type(char.inte)}"
	assert char.luk == 4, f"LUK test failed! LUK amount: {char.luk}; Type: {type(char.luk)}"
	primary_stats = char.get_primary_stats()  # returns a dictionary of the 4 main stats; dictionary
	assert primary_stats == {'str': 12, 'dex': 5, 'int': 4, 'luk': 4}, f"Primary Stats test failed! \nExpected: {{'str': 12, 'dex': 5, 'int': 4, 'luk': 4}} \nEncountered: {primary_stats}"
	assert char.max_hp == 50, f"HP test failed! HP amount: {char.max_hp}; Type: {type(char.max_hp)}"
	assert char.max_mp == 0, f"MP test failed! MP amount: {char.max_mp}; Type: {type(char.max_mp)}"
	assert char.ap == 0, f"AP test failed! AP amount: {char.ap}; Type: {type(char.ap)}"
	assert char.sp == 0, f"SP test failed! SP amount: {char.sp}; Type: {type(char.sp)}"

def test_fetch_user_id(user_id):
	assert user_id == 90001, f"Database method 'get_user_id_by_name' test failed! User ID: {user_id}; Type: {type(user_id)}"

# Character info setting tests
@pytest.mark.parametrize("before, delta, expected",[
	("314159", 2827433, "3141592"),
])
def test_meso_changes(char, before, delta, expected):
	char.money = before # Sets money to 314,159 mesos in the database
	assert char.money == before, f"Meso setting test failed! Expected: {before}; Meso count: {char.money}; Type: {type(char.money)}"
	char.add_mesos(delta)  # Adds 2,827,433 to the current meso count, and saves to DB
	# character now has 3,141,592 mesos
	assert char.money == expected, f"Meso adding test failed! Expected: {expected}; Meso count: {char.money}; Type: {type(char.money)}"
	char.money = "0"  # reset to baseline

@pytest.mark.parametrize("before, delta, expected",[
	(3, 28, 31),
])
def test_fame_changes(char, before, delta, expected):
	char.fame = before # Sets money to 314,159 mesos in the database
	assert char.fame == before, f"Fame setting test failed! Expected: {before}; Fame count: {char.fame}; Type: {type(char.fame)}"
	char.add_fame(delta) # Adds 28 fame to the existing count and saves to database
	# character fame is now 31
	assert char.fame == expected, f"Fame adding test failed! Expected: {expected}; Fame count: {char.fame}; Type: {type(char.fame)}"
	char.fame = 0  # reset to baselineine

@pytest.mark.parametrize("before, delta, expected",[
	(10, 21, 31),
])
def test_level_changes(char, before, delta, expected):
	assert char.level == before, f"Character level setting test failed! Expected: {before}; Level count: {char.level}; Type: {type(char.level)}"
	char.add_level(delta)  # Adds 21 to the existing count and saves to database
	# character is now level 31
	assert char.level == expected, f"Character level adding test failed! Expected: {expected}; Level count: {char.level}; Type: {type(char.level)}"
	char.level = 1  # reset to baseline

@pytest.mark.parametrize("before, expected",[
	(0, 100),
])
def test_level_changes(char, before, expected):
	char.job = expected  # set job ID to warrior
	assert char.job == expected, f"Job ID setting test failed! Expected: {expected}; Job ID: {char.job}; Type: {type(char.job)}"
	char.job = before  # reset job ID to beginner

@pytest.mark.parametrize("before, expected",[
	("tester", "Kookiie"),
])
def test_name_changes(char, before, expected):
	char.name = expected
	assert char.name == expected, f"Name setting test failed! Expected: {expected}; Name: {char.name}; Type: {type(char.name)}"
	char.name = before  # reset to baseline

@pytest.mark.parametrize("before, expected",[
	("4000011", "100000000"),
])
def test_map_changes(char, before, expected):
	char.map = expected
	assert map == expected, f"Map ID setting test failed! Expected: {expected}; Map ID: {char.map}; Type: {type(char.map)}"
	char.map = before  # reset to baseline

@pytest.mark.parametrize("before, expected",[
	(23300, 20010),
])
def test_face_changes(char, before, expected):
	char.face =  expected
	assert char.face == expected, f"Face ID setting test failed! Expected: {expected}; Face ID: {char.face}; Type: {type(char.face)}"
	char.face = before  # reset to baseline

@pytest.mark.parametrize("before, expected",[
	(36786, 30027),
])
def test_face_changes(char, before, expected):
	char.hair = expected
	assert hair == expected, f"Hair ID setting test failed! Expected: {expected}; Hair ID: {char.hair}; Type: {type(char.hair)}"
	char.hair = before  # reset to baseline

@pytest.mark.parametrize("before, expected",[
	(0, 2),
])
def test_skin_changes(char, before, expected):
	char.skin = expected
	assert char.skin == expected, f"Skin ID setting test failed! Expected: {expected}; Skin ID: {char.skin}; Type: {type(char.skin)}"
	char.skin = before  # reset to baseline

@pytest.mark.parametrize("before, delta, expected",[
	("314159", 2827433, "3141592"),
])
def test_level_changes(char, before, delta, expected):
	char.exp = before
	assert exp == before, f"EXP test setting failed! Expected: {before}; EXP amount: {char.exp}; Type: {type(char.exp)}"
	char.add_exp(delta)
	assert char.exp == expected, f"EXP test adding failed! Expected: {expected}; EXP amount: {char.exp}; Type: {type(char.exp)}"
	char.exp = "0"  # reset to baseline


print("\nChecking the ability to write the following information to DB: ")
print("    > STR; DEX; INT; LUK. \n")
# Set values for STR, DEX, INT, LUK
char.strength = 31
char.dex = 31
char.inte = 31
char.luk = 31

strength = char.strength  # re-fetch data
assert strength == 31, f"STR setting test failed! Expected: {expected}; STR amount: {strength}; Type: {type(strength)}"
char.add_str(1)
strength = char.strength  # re-fetch data
assert strength == 32, f"STR adding test failed! Expected: {expected}; STR amount: {strength}; Type: {type(strength)}"
char.strength = 12  # reset to baseline

dex = char.dex  # re-fetch data
assert dex == 31, f"DEX setting test failed! Expected: {expected}; DEX amount: {dex}; Type: {type(dex)}"
char.add_dex(1)
dex = char.dex  # re-fetch data
assert dex == 32, f"DEX adding test failed! Expected: {expected}; DEX amount: {dex}; Type: {type(dex)}"
char.dex = 5  # reset to baseline

inte = char.inte  # re-fetch data
assert inte == 31, f"INT setting test failed! Expected: {expected}; INT amount: {inte}; Type: {type(inte)}"
char.add_inte(1)
inte = char.inte  # re-fetch data
assert inte == 32, f"INT adding test failed! Expected: {expected}; INT amount: {inte}; Type: {type(inte)}"
char.inte = 4  # reset to baseline

luk = char.luk  # re-fetch data
assert luk == 31, f"LUK setting test failed! Expected: {expected}; LUK amount: {luk}; Type: {type(luk)}"
char.add_luk(1)
luk = char.luk  # re-fetch data
assert luk == 32, f"LUK adding test failed! Expected: {expected}; LUK amount: {luk}; Type: {type(luk)}"
char.luk = 4  # reset to baseline


print("\nChecking the ability to write the following information to DB: ")
print("    > HP; MP; AP; SP. \n")
# Set values for HP, MP, AP, SP
char.max_hp = 31
char.max_mp = 31
char.ap = 31
char.sp = 31

hp = char.max_hp  # re-fetch data
assert hp == 31, f"HP setting test failed! Expected: {expected}; HP amount: {hp}; Type: {type(hp)}"
char.add_max_hp(1)
hp = char.max_hp  # re-fetch data
assert hp == 32, f"HP adding test failed! Expected: {expected}; HP amount: {hp}; Type: {type(hp)}"
char.max_hp = 50  # reset to baseline

mp = char.max_mp  # re-fetch data
assert mp == 31, f"MP setting test failed! Expected: {expected}; MP amount: {mp}; Type: {type(mp)}"
char.add_max_mp(1)
mp = char.max_mp  # re-fetch data
assert mp == 32, f"MP adding test failed! Expected: {expected}; MP amount: {mp}; Type: {type(mp)}"
char.max_mp = 0  # reset to baseline

ap = char.ap  # re-fetch data
assert ap == 31, f"AP setting test failed! Expected: {expected}; AP amount: {ap}; Type: {type(ap)}"
char.add_ap(1)
ap = char.ap  # re-fetch data
assert ap == 32, f"AP adding test failed! Expected: {expected}; AP amount: {ap}; Type: {type(ap)}"
char.ap = 0  # reset to baseline

sp = char.sp  # re-fetch data
assert sp == 31, f"SP setting test failed! Expected: {expected}; SP amount: {sp}; Type: {type(sp)}"
char.add_sp(1)
sp = char.sp  # re-fetch data
assert sp == 32, f"SP adding test failed! Expected: {expected}; SP amount: {sp}; Type: {type(sp)}"
char.sp = 0  # reset to baseline

print("\nChar info write tests complete!")
print("----------------------------------")
