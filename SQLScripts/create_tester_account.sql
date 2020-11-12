-- Create admin tester user with User ID of 90,001
INSERT INTO `users` (id, votepoints, donationpoints, maplePoints, nxPrepaid, nblockreason, pblockreason, 
`name`, `password`, accounttype, chatunblockdate, pic, characterslots)
VALUES (90001, 0, 0, 0, 0, 0, 3, 
'tester', 'lorem', 4, 0, '111111', 40)
ON DUPLICATE KEY UPDATE votepoints=0, donationpoints=0, maplePoints=0, nxPrepaid=0, nblockreason=0, pblockreason=3, 
`name`='tester', `password`='lorem', accounttype=4, chatunblockdate=0, pic='111111';

-- Create admin tester account with Account ID of 90,001, Trunk ID of 90,001, and no NX
INSERT INTO accounts (id, worldid, userid, trunkid, nxCredit)
VALUES (90001, 1, 90001, 90001, 0)
ON DUPLICATE KEY UPDATE worldid=1, userid=90001, trunkid=90001, nxCredit=0;

-- Create admin tester character with Character ID of 900,001, inventories 540,001- 540,006
INSERT INTO characters (id, accid, avatardata, equippedinventory, equipinventory, consumeinventory, 
etcinventory, installinventory, cashinventory, questmanager, rewardPoints, monsterbook)
VALUES (900001, 90001, 900001, 5400001, 5400002, 
5400003, 5400004, 5400005, 5400006, 900001, 0, 900001)
ON DUPLICATE KEY UPDATE accid=90001, avatardata=900001, equippedinventory=5400001, 
equipinventory=5400002, consumeinventory=5400003, etcinventory=5400004, installinventory=5400005, 
cashinventory=5400006, questmanager=900001, rewardPoints=0, monsterbook=900001;

-- Create stats for Char 900,001
INSERT INTO characterstats (id, characterid, characteridforlog, worldidforlog, `name`, gender, skin, face, hair, 
mixbasehaircolor, mixaddhaircolor, mixhairbaseprob, `level`, job, str, dex, inte, luk, hp, maxhp, mp, maxmp, ap, sp, `exp`, pop, 
money, wp, extendsp, posmap, portal, subjob, deffaceacc, fatigue, lastfatigueupdatetime, 
charismaexp, insightexp, willexp, craftexp, senseexp, charmexp, 
noncombatstatdaylimit, pvpexp, pvpgrade, pvppoint, pvpmodelevel, pvpmodetype, 
eventpoint, albaactivityid, albastarttime, albaduration, albaspecialreward, burning, 
charactercard, accountlastlogout, lastlogout, gachexp, honorexp, nextavailablefametime)
VALUES (900001, 900001, 900001, 1, 'tester', 0, 0, 23300, 36786, 
0, 0, 0, 1, 0, 12, 5, 4, 4, 50, 50, 0, 0, 0, 0, '0', 0, 
'0', 0, 900001, '4000011', 0, 0, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 
900001, 0, 0, 0, 0, 0, 
0, 0, '1601-01-01 11:13:45.000', 0, 0, 0, 
900001, 900001, '1601-01-01 11:13:45.000', 0, 0, '1601-01-01 11:13:45.000')
ON DUPLICATE KEY UPDATE characterid=900001, characteridforlog=900001, worldidforlog=1, `name`='tester', gender=0, skin=0, face=23300, hair=36786, 
mixbasehaircolor=0, mixaddhaircolor=0, mixhairbaseprob=0, `level`=1, job=0, str=12, dex=5, inte=4, luk=4, hp=50, maxhp=50, mp=0, maxmp=0, ap=0, sp=0, `exp`='0', pop=0,
money='0', wp=0, extendsp=0, posmap='4000011', portal=0, subjob=0, deffaceacc=0, fatigue=0, lastfatigueupdatetime=0, 
charismaexp=0, insightexp=0, willexp=0, craftexp=0, senseexp=0, charmexp=0, 
noncombatstatdaylimit=900001, pvpexp=0, pvpgrade=0, pvppoint=0, pvpmodelevel=0, pvpmodetype=0, 
eventpoint=0, albaactivityid=0, albastarttime='1601-01-01 11:13:45.000', albaduration=0, albaspecialreward=0, burning=0, 
charactercard=900001, accountlastlogout=900001, lastlogout='1601-01-01 11:13:45.000', gachexp=0, honorexp=0, nextavailablefametime='1601-01-01 11:13:45.000';
