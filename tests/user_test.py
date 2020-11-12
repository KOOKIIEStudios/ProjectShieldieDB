"""This is a unit test for checking basic Character handling functionality

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

# Not yet implemented
# def test_fetch_nx(user):
# 	 assert user.nx == 0, f"Error encountered whilst fetching NX: \nExpected: 0 (Int); Encountered: {user.nx}, Type: {type(user.nx)}"

# User info setting tests
@pytest.mark.parametrize("before, expected",[
	("Lorem Ipsum", "dolor sit amet"),
])
def test_ban_reason_changes(user, before, delta, expected):
	user.ban_reason = expected
	assert  user.ban_reason == expected, f"Error encountered whilst setting ban reason: \nExpected: {expected} (String); Encountered: {user.ban_reason}, Type: {type(user.ban_reason)}"


