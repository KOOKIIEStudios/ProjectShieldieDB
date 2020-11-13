"""This is a unit test for checking basic User handling functionality

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

def test_direct_user_fetch():
	# Import DB
	try:
		spirit = SwordieDB(host="127.0.0.1", password="", user="root", schema="spirit", port=3306)
	except Exception as e:
		print(f"Error has occurred whist attempting to load DB: \n{e}")
	user = spirit.get_user_by_username("tester")
	assert user.user_id == 90001, f"Error encountered whilst fetching User by Username: \nExpected: 90001 (Int); Encountered: {user.user_id}, Type: {type(user.user_id)}"

@pytest.fixture
def user():
	# Import DB
	try:
		spirit = SwordieDB(host="127.0.0.1", password="", user="root", schema="spirit", port=3306)
	except Exception as e:
		print(f"Error has occurred whist attempting to load DB: \n{e}")
	char_obj = spirit.get_char_by_name("tester")
	user_obj = char_obj.user
	return user_obj

# User info fetching tests
def test_fetch_acc_type(user):
	assert user.account_type == 4, f"Error encountered whilst fetching account type: \nExpected: 4 (Int); Encountered: {user.account_type}, Type: {type(user.account_type)}"

def test_acc_str(user):
	assert user.get_acc_type_string() == "Admin", f"Error encountered whilst fetching account type string: \nExpected: \"Admin\" (String); Encountered: {user.get_acc_type_string()}, Type: {type(user.get_acc_type_string())}"

def test_fetch_ban_reason(user):
	assert user.ban_reason == "Lorem Ipsum", f"Error encountered whilst fetching ban reason: \nExpected: \"Lorem Ipsum\" (String); Encountered: {user.ban_reason}, Type: {type(user.ban_reason)}"

def test_fetch_donor_points(user):
	assert user.donation_points == 0, f"Error encountered whilst fetching DP count: \nExpected: 0 (Int); Encountered: {user.donation_points}, Type: {type(user.donation_points)}"

def test_fetch_maple_points(user):
	assert user.maple_points == 0, f"Error encountered whilst fetching Maple Points: \nExpected: 0 (Int); Encountered: {user.maple_points}, Type: {type(user.maple_points)}"

def test_fetch_user_id(user):
	assert user.user_id == 90001, f"Error encountered whilst fetching User ID: \nExpected: 90001 (Int); Encountered: {user.user_id}, Type: {type(user.user_id)}"

def test_fetch_vote_points(user):
	assert user.vote_points == 0, f"Error encountered whilst fetching Vote Points: \nExpected: 0 (Int); Encountered: {user.vote_points}, Type: {type(user.vote_points)}"

def test_fetch_nx(user):
	assert user.nx_prepaid == 0, f"Error encountered whilst fetching NX: \nExpected: 0 (Int); Encountered: {user.nx_prepaid}, Type: {type(user.nx_prepaid)}"

def test_fetch_stat_by_column(user):
	assert user.get_stat_by_column("gender") == 0, f"Error encountered whilst fetching gender: \nExpected: 0 (Int); Encountered: {user.get_stat_by_column('gender')}, Type: {type(user.get_stat_by_column('gender'))}"

# User info setting tests
@pytest.mark.parametrize("before, expected",[
	("Lorem Ipsum", "dolor sit amet"),
])
def test_ban_reason_changes(user, before, expected):
	user.ban_reason = expected
	assert user.ban_reason == expected, f"Error encountered whilst setting ban reason: \nExpected: {expected} (String); Encountered: {user.ban_reason}, Type: {type(user.ban_reason)}"

# User info setting tests
@pytest.mark.parametrize("admin, intern, tester, player",[
	(4, 3, 5, 0),
])
def test_acc_type_changes(user, admin, intern, tester, player):
	# Directly set account type via property
	user.account_type = intern
	assert user.account_type == intern, f"Error encountered whilst directly setting account type: \nExpected: {intern} (String); Encountered: {user.account_type}, Type: {type(user.account_type)}"
	assert not user.is_admin(), f"Error encountered whilst checking account type: \nExpected: False (Bool); Encountered: {user.is_admin}"
	# Setting of account type by convenience functions
	user.give_player()
	assert user.account_type == player, f"Error encountered whilst setting account type with functions: \nExpected: {player} (String); Encountered: {user.account_type}, Type: {type(user.account_type)}"
	user.give_admin()
	assert user.account_type == admin, f"Error encountered whilst setting account type with functions: \nExpected: {admin} (String); Encountered: {user.account_type}, Type: {type(user.account_type)}"
	assert user.is_admin(), f"Error encountered whilst checking account type: \nExpected: True (Bool); Encountered: {user.is_admin}"

# Password change function omitted from checks - insecure function! Deprecated!

@pytest.mark.parametrize("before, delta, expected",[
	(314159, 2827433, 3141592),
])
def test_dp_changes(user, before, delta, expected):
	user.donation_points = before
	assert user.donation_points == before, f"Error encountered whilst setting DP count: \nExpected: {before} (String); Encountered: {user.donation_points}, Type: {type(user.donation_points)}"
	user.add_donation_points(delta)
	assert user.donation_points == expected, f"Error encountered whilst setting DP count: \nExpected: {expected} (String); Encountered: {user.donation_points}, Type: {type(user.donation_points)}"
	user.donation_points = 0

@pytest.mark.parametrize("before, delta, expected",[
	(314159, 2827433, 3141592),
])
def test_maple_points_changes(user, before, delta, expected):
	user.maple_points = before
	assert user.maple_points == before, f"Error encountered whilst setting Maple Points: \nExpected: {before} (String); Encountered: {user.maple_points}, Type: {type(user.maple_points)}"
	user.add_maple_points(delta)
	assert user.maple_points == expected, f"Error encountered whilst setting Maple Points: \nExpected: {expected} (String); Encountered: {user.maple_points}, Type: {type(user.maple_points)}"
	user.maple_points = 0

@pytest.mark.parametrize("before, delta, expected",[
	(314159, 2827433, 3141592),
])
def test_vp_changes(user, before, delta, expected):
	user.vote_points = before
	assert user.vote_points == before, f"Error encountered whilst setting VP count: \nExpected: {before} (String); Encountered: {user.vote_points}, Type: {type(user.vote_points)}"
	user.add_vote_points(delta)
	assert user.vote_points == expected, f"Error encountered whilst setting VP count: \nExpected: {expected} (String); Encountered: {user.vote_points}, Type: {type(user.vote_points)}"
	user.vote_points = 0

@pytest.mark.parametrize("before, delta, expected",[
	(314159, 2827433, 3141592),
])
def test_nx_changes(user, before, delta, expected):
	user.nx_prepaid = before
	assert user.nx_prepaid == before, f"Error encountered whilst setting VP count: \nExpected: {before} (String); Encountered: {user.nx_prepaid}, Type: {type(user.nx_prepaid)}"
	user.add_nx_prepaid(delta)
	assert user.nx_prepaid == expected, f"Error encountered whilst setting VP count: \nExpected: {expected} (String); Encountered: {user.nx_prepaid}, Type: {type(user.nx_prepaid)}"
	user.nx_prepaid = 0
