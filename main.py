# Libraries
import time
import csv
from itertools import combinations
from datetime import datetime

# Player Object
class Player:
	def __init__(self, name, cost, position):
		self.name = name
		self.cost = cost
		self.position = position

class QbDfTe1Object:
    def __init__(self, cost, qb, df, te):
        self.cost = cost
        self.qb = qb
        self.df = df
        self.te = te

class Rb2Object:
    def __init__(self, cost, rb1, rb2):
        self.cost = cost
        self.rb1 = rb1 
        self.rb2 = rb2 

class Rb3Object:
    def __init__(self, cost, rb1, rb2, rb3):
        self.cost = cost
        self.rb1 = rb1 
        self.rb2 = rb2 
        self.rb3 = rb3

class Te2Object:
    def __init__(self, cost, te1, te2):
        self.cost = cost
        self.te1 = te1 
        self.te2 = te2 
class QbDfTe2Object:
    def __init__(self, cost, qb, df, te1, te2):
        self.cost = cost
        self.qb = qb,
        self.df = df,
        self.te1 = te1 
        self.te2 = te2 

class Wr3Object:
    def __init__(self, cost, wr1, wr2, wr3):
        self.cost = cost
        self.wr1 = wr1 
        self.wr2 = wr2 
        self.wr3 = wr3

class Wr4Object:
    def __init__(self, cost, wr1, wr2, wr3, wr4):
        self.cost = cost
        self.wr1 = wr1 
        self.wr2 = wr2 
        self.wr3 = wr3
        self.wr4 = wr4
class RosterObject:
    def __init__(self, cost, qb, rb1, rb2, wr1, wr2, wr3, te, df, flx):
        self.cost = cost
        self.qb = qb 
        self.rb1 = rb1
        self.rb2 = rb2 
        self.wr1 = wr1
        self.wr2 = wr2
        self.wr3 = wr3  
        self.te = te 
        self.df = df
        self.flx = flx

#Global Variables
all_players = []
quarter_backs = []
running_backs = []
wide_receivers = []
tight_ends = []
defenses = []
qb_df_te1_combos = []
qb_df_te2_combos = []
rb2_combos = []
rb3_combos = []
te2_combos = []
wr3_combos = []
wr4_combos = []
type1_rosters = []
type2_rosters = []
type3_rosters = []
all_rosters = []
too_much = []
budget = 50000
players_csv = 'players.csv'
rosters_csv = 'rosters.csv'
start_time = datetime.now()

#funcitons
def read_players():
    with open(players_csv, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            player = Player(line[0], int(line[1]), line[2])
            all_players.append(player)

def set_positions():
    for player in all_players:
        if(player.position == "QB"):
            quarter_backs.append(player)
        elif(player.position == "RB"):
            running_backs.append(player)
        elif(player.position == "WR"):
            wide_receivers.append(player)
        elif(player.position == "TE"):
            tight_ends.append(player)
        elif(player.position == "DF"):
            defenses.append(player)
        else:
            print(player)
    
    tight_ends.sort(key=lambda x: x.cost, reverse=False)
    

def set_combinations():
    for rbs in (combinations(running_backs, 2)):
        cost = rbs[0].cost + rbs[1].cost
        rb2_combos.append(Rb2Object(cost, rbs[0], rbs[1]))
    for rbs in (combinations(running_backs, 3)):
        cost = rbs[0].cost + rbs[1].cost + rbs[2].cost
        rb3_combos.append(Rb3Object(cost, rbs[0], rbs[1], rbs[2]))
    for wrs in (combinations(wide_receivers, 3)):
        cost = wrs[0].cost + wrs[1].cost + wrs[2].cost
        wr3_combos.append(Wr3Object(cost, wrs[0], wrs[1], wrs[2]))
    for wrs in (combinations(wide_receivers, 4)):
        cost = wrs[0].cost + wrs[1].cost + wrs[2].cost + wrs[3].cost
        wr4_combos.append(Wr4Object(cost, wrs[0], wrs[1], wrs[2], wrs[3]))
    for tes in (combinations(tight_ends, 2)):
        cost = tes[0].cost + tes[1].cost
        te2_combos.append(Te2Object(cost, tes[0], tes[1]))
    
    for qb in quarter_backs:
        for df in defenses:
            for te in tight_ends:
                cost = qb.cost + df.cost + te.cost
                qb_df_te1_combos.append(QbDfTe1Object(cost, qb, df, te))
            for tes in te2_combos:
                cost = tes.cost + qb.cost + df.cost
                qb_df_te2_combos.append(QbDfTe2Object(cost, qb, df, tes.te1, tes.te2))
    
    rb2_combos.sort(key=lambda x: x.cost, reverse=False)
    rb3_combos.sort(key=lambda x: x.cost, reverse=False)
    wr3_combos.sort(key=lambda x: x.cost, reverse=False)
    wr4_combos.sort(key=lambda x: x.cost, reverse=False)   
    qb_df_te1_combos.sort(key=lambda x: x.cost, reverse=False)
    qb_df_te2_combos.sort(key=lambda x: x.cost, reverse=False)

def calculate_possible_rosters():
    type1 = len(qb_df_te1_combos) * len(rb2_combos) * len(wr4_combos)
    type2 = len(qb_df_te1_combos) * len(rb3_combos) * len(wr3_combos)
    type3 = len(qb_df_te2_combos) * len(rb2_combos) * len(wr3_combos)
    print("There are " + str(type1) + " potential type 1 rosters without considering budget")
    print("There are " + str(type2) + " potential type 2 rosters without considering budget")
    print("There are " + str(type3) + " potential type 3 rosters without considering budget")
    print("There are " + str(type1 + type2 + type3) + " potential total rosters without considering budget")

def create_roster1():
    for qbdfte in qb_df_te1_combos:
        for rbs in rb2_combos:
            for wrs in wr4_combos:
                cost = qbdfte.cost + rbs.cost + wrs.cost
                if (cost <= budget):                 
                    qb = qbdfte.qb
                    rb1 = rbs.rb1
                    rb2 = rbs.rb2
                    wr1 = wrs.wr1
                    wr2 = wrs.wr2
                    wr3 = wrs.wr3
                    te = qbdfte.te
                    df = qbdfte.df
                    flx = wrs.wr4
                    roster_object = RosterObject(cost, qb, rb1, rb2, wr1, wr2, wr3, te, df, flx)
                    type1_rosters.append(roster_object)
                    all_rosters.append(roster_object)
                else:
                    break
    print(str(len(type1_rosters)) + " valid type 1 rosters exist and are being created")


def create_roster2():
    for qbdfte in qb_df_te1_combos:
        for rbs in rb3_combos:
            for wrs in wr3_combos:
                cost = qbdfte.cost + rbs.cost + wrs.cost
                if (cost <= budget):                 
                    qb = qbdfte.qb
                    rb1 = rbs.rb1
                    rb2 = rbs.rb2
                    wr1 = wrs.wr1
                    wr2 = wrs.wr2
                    wr3 = wrs.wr3
                    te = qbdfte.te
                    df = qbdfte.df
                    flx = rbs.rb3
                    roster_object = RosterObject(cost, qb, rb1, rb2, wr1, wr2, wr3, te, df, flx)
                    type2_rosters.append(roster_object)
                    all_rosters.append(roster_object)
                else:
                    break
    print(str(len(type2_rosters)) + " valid type 2 rosters exist")


def create_roster3():
    for qbdfte in qb_df_te2_combos:
        for rbs in rb2_combos:
            for wrs in wr3_combos:
                cost = qbdfte.cost + rbs.cost + wrs.cost
                if (cost <= budget):                 
                    qb = qbdfte.qb[0]
                    rb1 = rbs.rb1
                    rb2 = rbs.rb2
                    wr1 = wrs.wr1
                    wr2 = wrs.wr2
                    wr3 = wrs.wr3
                    te = qbdfte.te1
                    df = qbdfte.df[0]
                    flx = qbdfte.te2
                    roster_object = RosterObject(cost, qb, rb1, rb2, wr1, wr2, wr3, te, df, flx)
                    type3_rosters.append(roster_object)
                    all_rosters.append(roster_object)
                else:
                    break
    print(str(len(type3_rosters)) + " valid type 3 rosters exist")
    all_rosters.sort(key=lambda x: x.cost, reverse=False)


def write_rosters():
    print(str(len(all_rosters)) + " valid unique rosters exist")
    count = 0

    with open(rosters_csv, 'w') as f:
		the_writer = csv.writer(f)
		the_writer.writerow(['QB', 'RB1', 'RB2', 'WR1', 'WR2', 'WR3', 'TE', 'DF', 'FX', 'BUDGET'])
		lcl_roster_array = []
		for player in all_rosters:
			qb = player.qb.name
			rb1 = player.rb1.name
			rb2 = player.rb2.name
			wr1 = player.wr1.name
			wr2 = player.wr2.name
			wr3 = player.wr3.name
			te = player.te.name
			df = player.df.name
			fx = player.flx.name
			amt = player.cost
			lcl_roster = [qb, rb1, rb2, wr1, wr2, wr3, te, df, fx, amt]
			the_writer.writerow(lcl_roster)

			lcl_roster_array.append(lcl_roster)
			count += 1
			if count % 100000 == 0:
				print(str(count) + ' rosters created')
    print(str(len(all_rosters)) +  " unique rosters were created in " + str((datetime.now() - start_time).seconds) + " seconds")

#function calls
read_players()
set_positions()
set_combinations()
calculate_possible_rosters()
create_roster1()
create_roster2()
create_roster3()
write_rosters()

