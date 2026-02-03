import random
from prettytable import PrettyTable
import pandas as pd
import re

# skill variation. opposition reports. post match reports. injured and susp randomizers. form randomizer.
# win rewards. more specific player report messages - lowest skill player/lowest form player etc.
# quadruple fixture quantity
# player scout spotting worthy recuits in pools. could also incorporate academy players to promote?
# substitutes?
# cpu transfers and intelligence - adjust slightly so that cpu doesnt just take best players always. include form consideration
# view league anytime
# good players want to leave bad performing club? want to go to big club
# random players requesting transfer
# signing star player boosts form
# change form to morale?


# top of program


full_names = ['Oliver Smith', 'Finn Jones', 'Ollie Brown', 'Hugo Wilson', 'Ethan Johnson', 'Eddie Davies', 'Ethan Thompson', 'Cameron Evans', 'Jacob Walker', 'Jay White', 'Kieran Green', 'Jacob Hall', 'Calvin Wood', 'Coen Clarke', 'Caleb Clark', 'Conor Lewis', 'Connor Harris', 'Nathan Cooper', 'Nath Baker', 'Daniel Morgan', 'Danny Allen', 'Jack Edwards', 'Joe Campbell', 'Alexander Cook', 'Al Bailey', 'Frederick Mitchell', 'Freddie Kelly', 'Adam Richardson', 'Ad Adams', 'Zachary Wells', 'Zac Price', 'Sean Jenkins', 'Seany Ellis', 'Gregory Dixon', 'G Murray', 'Theodore Weaver', 'T Harrison', 'Miles Berry', 'Mikey Ellison', 'Rufus Foster', 'Arthur West', 'Ralphie Reid', 'Ralph Stewart', 'William Hunt', 'Wills Owen', 'Ivor Booth', 'Barnaby Mcdonald', 'Gilbert Rose', 'G Warren', 'Kilian Riley', 'Vincent Graham', 'Dylan Webb', 'D Shaw', 'Fraser Simpson', 'Frase Pearce', 'Callum Holmes', 'Call Morrison', 'Hamish Barnes', 'Seb Harper', 'Lewis Cunningham', 'Lewy Lloyd', 'Maxwell Hart', 'Max Griffiths', 'Gordon Bishop', 'Symon Gardner', 'Fintan Scott', 'Finn Burton', 'Alistair Chapman', 'Ali Manning', 'Euan Webster', 'Eddie Chambers', 'Lachlan Neal', 'Lach Hunter', 'Gus Craig', 'Angus Bennett', 'Graeme Wallace', 'Graham Bradley', 'Alastair Fletcher', 'Ali Douglas', 'Douglas Lucas', 'Doug Day', 'Malcolm Berry', "Mac O'Brien", 'Bruce Ryan', 'Brucey Lynch', 'Stuart Burgess', 'Stewart Perkins', "Keith O'Connor", 'Keefy Hayes', 'Ewan Duncan', 'Eddie Arnold', 'Rory Hammond', 'R Hardy', 'Finnegan Burke', 'Ben Phelps', 'Murdo Gallagher', 'Murray Whitehead', 'Ian Pierce', 'I Sharp', 'Owen Mcguire', 'Eoin Fitzgerald', 'Aidan Hancock', "Ronan O'Neill", 'Lee Preston', 'Li Barrett', 'Shane Hayward', 'Shaney Boyd', 'Oscar Parsons', 'Ossie Oneill', 'Grayson Mcdowell', 'Alfie Crawford', 'Archie Fleming', 'George Rice', 'Finley Higgins', 'Finny Walsh', 'Robert Hutchinson', 'Robbie Clements', 'Kenzie Abbott', 'Ken Cross', 'Blair Little', 'Beau May', 'Crispin Elliott', 'Dashiell Cohen', 'Ephraim Stevenson', 'Galen Bowers', 'Hawthorn Brennan', 'Jago Smith', 'Lorcan Jones', 'Magnus Brown', 'Niall Wilson', 'Orson Johnson', 'Peregrine Davies', 'Quinlan Robinson', 'Rhett Wright', 'Sylvester Thompson', 'Tadhg Evans', 'Harley Walker', 'James White', 'Daniel Roberts', 'Thomas Green', 'Samuel Hall', 'Matthew Wood', 'David Jackson', 'Christopher Clarke', 'Joshua Clark', 'Adam Lewis', 'Richard Harris', 'Robert Cooper', 'Michael King', 'Andrew Baker', 'William Phillips', 'Benjamin Morgan',
              'Luke Allen', 'Alexander Edwards', 'Joseph Turner', 'Oliver Campbell', 'Harry Cook', 'Edward Bailey', 'Jonathan Morris', 'Peter Mitchell', 'George Ward', 'Nicholas Kelly', 'Timothy Carter', 'Stephen Richardson', 'Jack Adams', 'Philip Collins', 'Charles Nelson', 'Mark Cox', 'Lewis Wells', 'Simon Price', 'Anthony Gray', 'Patrick Howard', 'Paul Jenkins', 'Jonathan Ellis', 'Edward Dixon', 'Gregory Murray', 'Marcus Weaver', 'Alex Harrison', 'Ben Berry', 'Sam Gibson', 'Tom Ellison', 'Rob Foster', 'Mike Mills', 'Chris Pearson', 'Jon West', 'Nick Reid', 'Tim Knight', 'Steve Hill', 'Andy Stewart', 'Will Hunt', 'Luke Owen', 'Matt Mason', 'Jamie Palmer', 'Danny Booth', 'Joe Mcdonald', 'Nathan Fox', 'Ryan Rose', 'Jacob Perry', 'Max Warren', 'Charlie Riley', 'Samuel Graham', 'Henry Webb', 'Connor Shaw', 'Leo Simpson', 'Isaac Ford', 'Tyler Pearce', 'Oscar Holmes', 'Alaric Morrison', 'Alden Barnes', 'Alonso Harper', 'Alton Cunningham', 'Amadeus Nicholson', 'Amias Lloyd', 'Anders Hart', 'Andre Mills', 'Apollo Johnston', 'Archer Griffiths', 'Ari Bishop', 'Armand Gardner', 'Arrow Scott', 'Arturo Burton', 'Atlas Bryant', 'Atticus Chapman', 'Auden Marshall', 'Gus Manning', 'Auri Hudson', 'Austin Webster', 'Avery Chambers', 'Balthazar Lawrence', 'Barnabas Neal', 'Barrett Sutton', 'Bastian Hunter', 'Bear Craig', 'Jules Bennett', 'Bellamy Wallace', 'Benedict Gregory', 'Benson Bradley', 'Blaise Fletcher', 'Bodhi Douglas', 'Booker Sullivan', 'Bowie Lucas', 'Branson Day', 'Braxton Berry', "Breccan O'Brien", 'Brendan Ryan', 'Bridger Lynch', 'Brigham Carr', 'Brock Burgess', 'Bronson Perkins', 'Brooks Greene', "Bryant O'Connor", 'Caius Curtis', 'Callahan Sweeney', 'Callum Walters', 'Calvin Hayes', 'Camden Duncan', 'Cameron Arnold', 'Cannon Hammond', 'Cassian Hardy', 'Cato Burke', 'Cedric Phelps', 'Cillian Gallagher', 'Clarence Whitehead', 'Clark Pierce', 'Clement Conner', 'Clifford Sharp', 'Coby Mcguire', 'Cohen Williamson', 'Colin Fitzgerald', 'Conall Porter', 'Connell Hancock', 'Conner Doyle', "Conrad O'Neill", 'Constantine Preston', 'Cormac Shepherd', 'Corbin Barrett', 'Corey Hayward', 'Crosby Boyd', 'Cruz Moss', 'Cullen Parsons', 'Curtis Oneill', 'Cyrus Mcdowell', 'Dakota Crawford', 'Damon Fleming', 'Dane Rice', 'Darian Higgins', 'Dario Gibbons', 'Darius Walsh', 'Dash Hutchinson', 'Dawson Clements', 'Declan Abbott', 'Delaney Cross', 'Delmar Little', 'Denis May', 'Desmond Bass', 'Devin Elliott', 'Dexter Cohen', 'Diego Miles', 'Dmitri Stevenson', 'Donovan Bowers']


positions = ["Loosehead Prop", "Hooker", "Tighthead Prop", "Lock", "Lock", "Flanker",
             "Flanker", "Number 8", "Scrum Half", "Fly Half", "Wing", "Inside Centre",
             "Outside Centre", "Wing", "Fullback"]

player_id_nums = list(range(1, 301))
team_id_nums = list(range(1, 11))

team_list = ['Aberford RC', 'Addington Rugby', 'Bledlow Adders', 'Charing RC', 'Clifton Sirens', 'Culworth Ghosts',
             'Farnham Devils', 'Kemsing Harriers', 'Nettleton Wildcats', 'Petherton Hornets']

# Shuffle the list of names
random.shuffle(full_names)

# position dicts
lh_dict = {}
hook_dict = {}
th_dict = {}
l1_dict = {}
l2_dict = {}
f1_dict = {}
f2_dict = {}
n8_dict = {}
sh_dict = {}
fh_dict = {}
w1_dict = {}
c1_dict = {}
c2_dict = {}
w2_dict = {}
fb_dict = {}


pos_dict_list = [lh_dict, hook_dict, th_dict, l1_dict, l2_dict, f1_dict, f2_dict,
                 n8_dict, sh_dict, fh_dict, w1_dict, c1_dict, c2_dict, w2_dict, fb_dict]

id = 1
no = 1
inj_count = 0
susp_count = 0
inj_list = []
sus_list = []

# create pos dicts

for pos, pos_dict in enumerate(pos_dict_list):

    count = 0
    while count < 20:
        player_name = random.choice(full_names)
        full_names.remove(player_name)

        player_status = 'Fit'
        injured = False
        sus = False

        # player skill number
        weights = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 6, 5, 5,
                   4, 3, 3, 2, 2, 1, 1, 1, 1, 1, 0.5, 0.5, 0.5, 0.5, 0.5]
        player_skill = random.choices(range(65, 96), weights)[0]

        # injury determine
        inj_lot = random.randint(1, 4)
        inj_num = 1

        if inj_lot == inj_num:
            if inj_count < 2:
                player_status = "Injured"
                inj_count += 1
                injured = True
                inj_len = random.randint(1, 5)
        else:
            inj_len = 0

        inj_text_2 = "{} weeks"
        inj_text = "{} week"

        # suspension determine

        sus_lot = random.randint(1, 4)
        sus_num = 1
        # check if player skill in sus_num list
        if sus_lot == sus_num:
            if susp_count < 2:
                player_status = "Suspended"
                susp_count += 1
                sus = True

                sus_len = random.randint(1, 5)
        else:
            sus_len = 0

        ban_text = "{} week ban"

# form determine
        form = round(random.uniform(3.0, 9.6), 1)
        form_txt = "+Form player+"

        if player_status == 'Injured':
            if inj_len == 1:
                info = inj_text.format(inj_len)
            elif inj_len > 1:
                info = inj_text_2.format(inj_len)

        elif player_status == 'Suspended':
            info = ban_text.format(sus_len)

        elif player_status == 'Fit':
            if player_skill >= 90:
                info = "*Star Player*"
            elif form > 8.4:
                info = form_txt
            else:
                info = ""
        else:
            info = ""

# create pos dicts

        pos_dict[id] = {
            "player_id": id,
            "no.": no,
            "name": player_name,
            "age": random.randint(18, 36),
            "position": positions[pos],
            "form": form,
            "skill": player_skill,
            "status": player_status,
            "injured": injured,
            'sus': sus,
            "inj len": inj_len,
            "sus len": sus_len,
            "info": info,
            "game pts": 0,
            "total pts": 0
        }

        id += 1
        count += 1

    no += 1
    inj_count = 0
    susp_count = 0
    count = 0

    # print(pos_dict)


# make club dict


club_dict = {}
players = {}
stats = {
    "played": 0,
    "won": 0,
    "draw": 0,
    "lost": 0,
    "+/-": 0,
    "BP": 0,
    "Pts": 0,
}

x = 0
for num in team_id_nums:
    club = team_list[x]
    club_dict[club] = {
        "club_id": num,
        "club_name": club,
        "user_team": False,
        "stats": dict(stats),
        "players": dict(players),
        "credit": 1300,
        "total_skill": 0
    }
    x += 1

# Loop through pos dicts and assign players to teams
count = 0
x = 0

for team in club_dict:
    p_store = {}
    while count < 15:
        pos = pos_dict_list[x]
        player_choice = random.choice(list(pos))
        player_data = pos.pop(player_choice)
        price = player_data['skill']
        club_dict[team]['credit'] -= price
        club_dict[team]['total_skill'] += price
        if price > club_dict[team]['credit']:

            club_dict[team]['credit'] = 0

        p_store.update({player_choice: player_data})
        count += 1
        x += 1

    count = 0
    x = 0
    club_dict[team]['players'] = p_store
    # print(club_dict[team]['credit'])


# print tables for club select

def team_selection_table():
    table = PrettyTable()
    table.field_names = ["Team ID", "Team Name", "Finances"]

    for club_data in club_dict.values():
        team_name = club_data["club_name"]
        team_id = club_data["club_id"]
        finance = club_data["credit"]
        if finance > 150:
            finance = "Wealthy"
        elif finance > 100:
            finance = "Excellent"
        elif finance > 50:
            finance = "Good"
        elif finance > 20:
            finance = "Fair"
        elif finance > 10:
            finance = "Stable"
        elif finance < 10:
            finance = "Poor"
        table.add_row([team_id, team_name, finance])

    print(table)


def team_print(team):
    players = club_dict[team]['players']

    table = PrettyTable()
    table.field_names = ['Player ID', 'Number', 'Name',
                         'Age', 'Position', 'Form', 'Skill', 'Status', 'Info']

    for player_id, player_info in players.items():
        table.add_row([
            player_info['player_id'],
            player_info['no.'],
            player_info['name'],
            player_info['age'],
            player_info['position'],
            player_info['form'],
            player_info['skill'],
            player_info['status'],
            player_info['info']
        ])

    table.title = f"Team: {team}"
    table.title_align = "center"
    print(table)


def pos_print(pos):
    players = pos

    table = PrettyTable()
    table.field_names = ['Player ID', 'Number', 'Name',
                         'Age', 'Position', 'Form', 'Skill', 'Status', 'Info']

    for player_id, player_info in players.items():
        table.add_row([
            player_info['player_id'],
            player_info['no.'],
            player_info['name'],
            player_info['age'],
            player_info['position'],
            player_info['form'],
            player_info['skill'],
            player_info['status'],
            player_info['info']
        ])

    table.title = f"Pool: {player_info['position']}"
    table.title_align = "center"
    print(table)


def get_user_team():
    team_selection_table()

    # Reset user_team to False for all teams
    for team_info in club_dict.values():
        team_info["user_team"] = False

    while True:
        user_input = input(
            f"{manager_name}, choose the team you wish to manage by entering the Team ID: ")

        if user_input.isnumeric():
            team_id = int(user_input)

            for team_name, team_info in club_dict.items():
                if team_id == team_info["club_id"]:
                    team_info["user_team"] = True
                    return team_name

            print("Team not found.")
        else:
            print("Invalid input. Please enter a numeric Team ID.")


def confirm_team_selection(team):
    while True:
        team_print(team)
        user_input = input(
            f"{manager_name}, press Y to confirm team select, or N to choose a different team: ").lower()

        if user_input.isalpha():
            choice = user_input

            if choice == "y":
                return True
            elif choice == "n":
                return False

        print("Invalid input. Please enter Y or N.")


# manager name
manager_name = input("Manager, enter your name: ")

# user choose team
selected_team = get_user_team()
# user confirm team select
while True:
    # user confirm team
    team_confirmed = confirm_team_selection(selected_team)

    if team_confirmed:
        print("Team selection confirmed.")
        break
    else:
        selected_team = get_user_team()


# allocate clubs to operators

team_id_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# identifying user contolled team name
for k, v in club_dict.items():
    if club_dict[k]["user_team"] == True:
        user_team_id = club_dict[k]["club_id"]

        team_id_list.remove(user_team_id)
        user_team = k

# print(user_team)
# print(team_id_list)


# display fixtures

fixtures = [
    [["Aberford RC", "Kemsing Harriers"], ["Addington Rugby", "Bledlow Adders"], ["Charing RC",
                                                                                  "Farnham Devils"], ["Clifton Sirens", "Culworth Ghosts"], ["Petherton Hornets", "Nettleton Wildcats"]],
    [["Bledlow Adders", "Aberford RC"], ["Culworth Ghosts", "Petherton Hornets"], ["Farnham Devils",
                                                                                   "Clifton Sirens"], ["Kemsing Harriers", "Charing RC"], ["Nettleton Wildcats", "Addington Rugby"]],
    [["Aberford RC", "Nettleton Wildcats"], ["Addington Rugby", "Culworth Ghosts"], ["Charing RC",
                                                                                     "Bledlow Adders"], ["Kemsing Harriers", "Farnham Devils"], ["Petherton Hornets", "Clifton Sirens"]],
    [["Bledlow Adders", "Kemsing Harriers"], ["Clifton Sirens", "Addington Rugby"], ["Culworth Ghosts",
                                                                                     "Aberford RC"], ["Farnham Devils", "Petherton Hornets"], ["Nettleton Wildcats", "Charing RC"]],
    [["Aberford RC", "Clifton Sirens"], ["Addington Rugby", "Petherton Hornets"], ["Bledlow Adders",
                                                                                   "Farnham Devils"], ["Charing RC", "Culworth Ghosts"], ["Kemsing Harriers", "Nettleton Wildcats"]],
    [["Clifton Sirens", "Charing RC"], ["Culworth Ghosts", "Kemsing Harriers"], ["Farnham Devils",
                                                                                 "Addington Rugby"], ["Nettleton Wildcats", "Bledlow Adders"], ["Petherton Hornets", "Aberford RC"]],
    [["Aberford RC", "Addington Rugby"], ["Bledlow Adders", "Culworth Ghosts"], ["Charing RC",
                                                                                 "Petherton Hornets"], ["Kemsing Harriers", "Clifton Sirens"], ["Nettleton Wildcats", "Farnham Devils"]],
    [["Aberford RC", "Farnham Devils"], ["Addington Rugby", "Charing RC"], ["Clifton Sirens", "Bledlow Adders"], [
        "Culworth Ghosts", "Nettleton Wildcats"], ["Petherton Hornets", "Kemsing Harriers"]],
    [["Bledlow Adders", "Petherton Hornets"], ["Charing RC", "Aberford RC"], ["Farnham Devils",
                                                                              "Culworth Ghosts"], ["Kemsing Harriers", "Addington Rugby"], ["Nettleton Wildcats", "Clifton Sirens"]]
]


fixtures_dict = {
    1: {
        "Aberford RC": "Kemsing Harriers",
        "Addington Rugby": "Bledlow Adders",
        "Charing RC": "Farnham Devils",
        "Clifton Sirens": "Culworth Ghosts",
        "Petherton Hornets": "Nettleton Wildcats"
    },
    2: {
        "Bledlow Adders": "Aberford RC",
        "Culworth Ghosts": "Petherton Hornets",
        "Farnham Devils": "Clifton Sirens",
        "Kemsing Harriers": "Charing RC",
        "Nettleton Wildcats": "Addington Rugby"
    },
    3: {
        "Aberford RC": "Nettleton Wildcats",
        "Addington Rugby": "Culworth Ghosts",
        "Charing RC": "Bledlow Adders",
        "Kemsing Harriers": "Farnham Devils",
        "Petherton Hornets": "Clifton Sirens"
    },
    4: {
        "Bledlow Adders": "Kemsing Harriers",
        "Clifton Sirens": "Addington Rugby",
        "Culworth Ghosts": "Aberford RC",
        "Farnham Devils": "Petherton Hornets",
        "Nettleton Wildcats": "Charing RC"
    },
    5: {
        "Aberford RC": "Clifton Sirens",
        "Addington Rugby": "Petherton Hornets",
        "Bledlow Adders": "Farnham Devils",
        "Charing RC": "Culworth Ghosts",
        "Kemsing Harriers": "Nettleton Wildcats"
    },
    6: {
        "Clifton Sirens": "Charing RC",
        "Culworth Ghosts": "Kemsing Harriers",
        "Farnham Devils": "Addington Rugby",
        "Nettleton Wildcats": "Bledlow Adders",
        "Petherton Hornets": "Aberford RC"
    },
    7: {
        "Aberford RC": "Addington Rugby",
        "Bledlow Adders": "Culworth Ghosts",
        "Charing RC": "Petherton Hornets",
        "Kemsing Harriers": "Clifton Sirens",
        "Nettleton Wildcats": "Farnham Devils"
    },
    8: {
        "Aberford RC": "Farnham Devils",
        "Addington Rugby": "Charing RC",
        "Clifton Sirens": "Bledlow Adders",
        "Culworth Ghosts": "Nettleton Wildcats",
        "Petherton Hornets": "Kemsing Harriers"
    },
    9: {
        "Bledlow Adders": "Petherton Hornets",
        "Charing RC": "Aberford RC",
        "Farnham Devils": "Culworth Ghosts",
        "Kemsing Harriers": "Addington Rugby",
        "Nettleton Wildcats": "Clifton Sirens"
    }
}


# Function to print a specific round
def print_round(round_num):
    round_fixtures = fixtures_dict[round_num]

    # Create a PrettyTable instance
    table = PrettyTable()
    table.title = "HighBet Rugby Union League North-West"
    table.field_names = [f"Round {round_num}: Fixtures"]

    # Add rows to the table
    for team1, team2 in round_fixtures.items():
        table.add_row([f"{team1} vs {team2}"])

    # Print the table
    print(table)


def print_round_results(round_num):
    round_fixtures = fixtures_dict[round_num]

    # Create a PrettyTable instance
    table = PrettyTable()
    table.title = "HighBet Rugby Union League North-West"
    table.field_names = [f"Round {round_num}: Results"]

    s = 0
    # Add rows to the table
    for team1, team2 in round_fixtures.items():
        home_result = f"{home[s]}"
        sep = ' - '
        away_result = f"{away[s]}"
        row = f"{team1:<20s} {home_result:^2s} {sep:^5s} {away_result:^2s} {team2:>20s}"
        table.add_row([row])
        s += 1

    # Print the table
    print(table)


def league_print():
    # Create a PrettyTable instance
    table = PrettyTable()

    # Define table columns
    table.field_names = ["", "Team Name", "Played",
                         "Won", "Draw", "Lost", "+/-", "BP", "Pts"]

    # Sort club dictionary by 'pts' and '+/-' in descending order
    sorted_club_dict = sorted(club_dict.items(), key=lambda x: (
        x[1]['stats']['Pts'], x[1]['stats']['+/-']), reverse=True)

    # Iterate over the sorted club dictionary
    for rank, (club_name, club_data) in enumerate(sorted_club_dict, start=1):
        stats = club_data["stats"]
        played = stats["played"]
        won = stats["won"]
        draw = stats["draw"]
        lost = stats["lost"]
        plus_minus = stats["+/-"]
        bp = stats["BP"]
        pts = stats["Pts"]

        # Add a row to the table
        table.add_row([rank, club_name.ljust(20), played,
                      won, draw, lost, plus_minus, bp, pts])

    table.title = "HighBet Rugby Union League North-West"

    # Print the table
    print(table)


def player_transfer_in(pos):
    players = pos

    while True:
        credit_balance = club_dict[user_team]['credit']
        print(f"We currently have €{credit_balance}k to spend on new players.")
        user_input = input(
            "Type the Player ID of the player to be transferred to your team: ")

        if user_input.isnumeric():
            player_in_id = int(user_input)

            if player_in_id in players:
                player_data = players[player_in_id]
                player_skill = player_data['skill']
                user_team_credit = club_dict[user_team]['credit']

                if player_skill <= user_team_credit:
                    players.pop(player_in_id)
                    club_dict[user_team]['players'].update(
                        {player_in_id: player_data})
                    club_dict[user_team]['credit'] -= player_skill
                    club_dict[user_team]['total_skill'] += player_skill

                    # Sort the players by shirt number
                    club_dict[user_team]['players'] = dict(
                        sorted(club_dict[user_team]['players'].items(), key=lambda x: x[1]['no.']))

                    break
                else:
                    print("Insufficient credit to transfer this player.")
            else:
                print("Player not available.")
        else:
            print("Invalid input. Please type Player ID.")

    team_modify()


def player_transfer_out():

    players = club_dict[user_team]['players']

    while True:
        credit_balance = club_dict[user_team]['credit']
        print(f"We currently have €{credit_balance}k to spend on new players.")
        # Prompt for user input and convert to uppercase
        user_input = input(
            "Type the Player ID of the player to be transferred: ")

        if user_input.isnumeric():
            player_out_id = int(user_input)

            if player_out_id in players:

                player_data = players.pop(player_out_id)
                club_dict[user_team]['credit'] += player_data['skill']
                club_dict[user_team]['total_skill'] -= player_data['skill']

                if player_out_id in range(1, 21):
                    lh_dict.update({player_out_id: player_data})
                    pos_print(lh_dict)
                    player_transfer_in(lh_dict)
                elif player_out_id in range(21, 41):
                    hook_dict.update({player_out_id: player_data})
                    pos_print(hook_dict)
                    player_transfer_in(hook_dict)
                elif player_out_id in range(41, 61):
                    th_dict.update({player_out_id: player_data})
                    pos_print(th_dict)
                    player_transfer_in(th_dict)
                elif player_out_id in range(61, 81):
                    l1_dict.update({player_out_id: player_data})
                    pos_print(l1_dict)
                    player_transfer_in(l1_dict)
                elif player_out_id in range(81, 101):
                    l2_dict.update({player_out_id: player_data})
                    pos_print(l2_dict)
                    player_transfer_in(l2_dict)
                elif player_out_id in range(101, 121):
                    f1_dict.update({player_out_id: player_data})
                    pos_print(f1_dict)
                    player_transfer_in(f1_dict)
                elif player_out_id in range(121, 141):
                    f2_dict.update({player_out_id: player_data})
                    pos_print(f2_dict)
                    player_transfer_in(f2_dict)
                elif player_out_id in range(141, 161):
                    n8_dict.update({player_out_id: player_data})
                    pos_print(n8_dict)
                    player_transfer_in(n8_dict)
                elif player_out_id in range(161, 181):
                    sh_dict.update({player_out_id: player_data})
                    pos_print(sh_dict)
                    player_transfer_in(sh_dict)
                elif player_out_id in range(181, 201):
                    fh_dict.update({player_out_id: player_data})
                    pos_print(fh_dict)
                    player_transfer_in(fh_dict)
                elif player_out_id in range(201, 221):
                    w1_dict.update({player_out_id: player_data})
                    pos_print(w1_dict)
                    player_transfer_in(w1_dict)
                elif player_out_id in range(221, 241):
                    c1_dict.update({player_out_id: player_data})
                    pos_print(c1_dict)
                    player_transfer_in(c1_dict)
                elif player_out_id in range(241, 261):
                    c2_dict.update({player_out_id: player_data})
                    pos_print(c2_dict)
                    player_transfer_in(c2_dict)
                elif player_out_id in range(261, 281):
                    w2_dict.update({player_out_id: player_data})
                    pos_print(w2_dict)
                    player_transfer_in(w2_dict)
                elif player_out_id in range(281, 301):
                    fb_dict.update({player_out_id: player_data})
                    pos_print(fb_dict)
                    player_transfer_in(fb_dict)

                # Valid input
                break
            else:
                print("Player not in your team.")
        else:
            print("Invalid input. Please type Player ID.")
    # print(p_out)


def player_in_cpu(team, player_out_id, player_out_data, pos_dict):
    # print(f"you are transferring {player_out_id} from {team} ")

    player_out_value = player_out_data['skill']
    # print(f"player out value is {player_out_value}")
    club_dict[team]['credit'] += player_out_value
    club_dict[team]['total_skill'] -= player_out_value

    player_in_id = None  # Initialize with None

    for id, player_data in pos_dict.items():
        player_id = player_data['player_id']
        player_status = player_data['status']
        player_cost = player_data['skill']
        credit = club_dict[team]['credit']
        player_name = player_data['name']
        player_pos = player_data['position']
        # print(f"{team} credit is {credit}")
        if player_status == 'Fit' and credit >= player_cost:
            # print(f"player {player_id} is suitable")
            player_in_id = player_id
            break

    if player_in_id is not None:  # Check if a suitable player is found
        player_data = pos_dict.pop(player_in_id)
        pos_dict.update({player_out_id: player_out_data})
        # print(f"{player_out_id} has joined the {player_out_data['position']} pool.")
        club_dict[team]['players'].update({player_in_id: player_data})
        print(f"{player_name}, {player_pos}, has joined {team}")
        print()
        club_dict[team]['credit'] -= player_cost
        club_dict[team]['total_skill'] += player_cost

        # Sort the players by shirt number
        club_dict[team]['players'] = dict(
            sorted(club_dict[team]['players'].items(), key=lambda x: x[1]['no.']))
        # pos_dict = dict(sorted(pos_dict.items(), key=lambda x: x[1]['player_id']))
    else:
        print("No suitable player found.")


def player_out_cpu():

    inj_list = []
    sus_list = []
    for team, team_data in club_dict.items():
        if team_data["user_team"] == False:
            players = team_data["players"]
            for player_choice, player_data in players.items():
                player_id = player_data['player_id']
                player_status = player_data['status']
                if player_status == 'Injured':
                    # print(f"Player {player_id} in {team} is injured.")
                    inj_list.append(player_id)
                elif player_status == 'Suspended':
                    # print(f"Player {player_id} in {team} is suspended.")
                    sus_list.append(player_id)

    # for pos in pos_dict_list:
    #     for id,player_data in pos.items():
    #         player_id = player_data['player_id']
    #         player_status = player_data['status']
    #         player_pos = player_data['position']
    #         if player_status == 'Injured':
    #             # print(f"Player {player_id} in {player_pos} is injured.")
    #             # inj_list.append(player_id)
    #         elif player_status == 'Suspended':
                # print(f"Player {player_id} in {player_pos} is suspended.")
                # sus_list.append(player_id)

    # print(f"injuries: {inj_list}")
    # print(f"suspensions: {sus_list}")
    #
    total_list = inj_list+sus_list
    # print(f"total list {total_list}")

    club_dict_copy = dict(club_dict)

    for team, team_data in club_dict_copy.items():
        if team_data["user_team"] == False:
            players = team_data["players"]
            players = dict(team_data["players"])
            credit = team_data['credit']
            for player_choice, player_data in players.items():
                player_out_id = player_data['player_id']
                player_out_skill = player_data['skill']

                if player_out_id in total_list:

                    if player_out_id in range(1, 21):
                        # print("this is a loosehead")

                        player_in_cpu(team, player_out_id,
                                      player_data, lh_dict)
                        del club_dict[team]['players'][player_out_id]
                        # team_print(team)
                    elif player_out_id in range(21, 41):
                        # print("this is a hooker")
                        player_in_cpu(team, player_out_id,
                                      player_data, hook_dict)
                        del club_dict[team]['players'][player_out_id]
                        # team_print(team)
                    elif player_out_id in range(41, 61):
                        # print("this is a tighthead")
                        player_in_cpu(team, player_out_id,
                                      player_data, th_dict)
                        del club_dict[team]['players'][player_out_id]
                        # team_print(team)
                    elif player_out_id in range(61, 81):
                        player_in_cpu(team, player_out_id,
                                      player_data, l1_dict)
                        del club_dict[team]['players'][player_out_id]
                    elif player_out_id in range(81, 101):
                        player_in_cpu(team, player_out_id,
                                      player_data, l2_dict)
                        del club_dict[team]['players'][player_out_id]
                    elif player_out_id in range(101, 121):
                        player_in_cpu(team, player_out_id,
                                      player_data, f1_dict)
                        del club_dict[team]['players'][player_out_id]
                    elif player_out_id in range(121, 141):
                        player_in_cpu(team, player_out_id,
                                      player_data, f2_dict)
                        del club_dict[team]['players'][player_out_id]
                    elif player_out_id in range(141, 161):
                        player_in_cpu(team, player_out_id,
                                      player_data, n8_dict)
                        del club_dict[team]['players'][player_out_id]
                    elif player_out_id in range(161, 181):
                        player_in_cpu(team, player_out_id,
                                      player_data, sh_dict)
                        del club_dict[team]['players'][player_out_id]
                    elif player_out_id in range(181, 201):
                        player_in_cpu(team, player_out_id,
                                      player_data, fh_dict)
                        del club_dict[team]['players'][player_out_id]
                    elif player_out_id in range(201, 221):
                        player_in_cpu(team, player_out_id,
                                      player_data, w1_dict)
                        del club_dict[team]['players'][player_out_id]
                    elif player_out_id in range(221, 241):
                        player_in_cpu(team, player_out_id,
                                      player_data, c1_dict)
                        del club_dict[team]['players'][player_out_id]
                    elif player_out_id in range(241, 261):
                        player_in_cpu(team, player_out_id,
                                      player_data, c2_dict)
                        del club_dict[team]['players'][player_out_id]
                    elif player_out_id in range(261, 281):
                        player_in_cpu(team, player_out_id,
                                      player_data, w2_dict)
                        del club_dict[team]['players'][player_out_id]
                    elif player_out_id in range(281, 301):
                        player_in_cpu(team, player_out_id,
                                      player_data, fb_dict)
                        del club_dict[team]['players'][player_out_id]


def team_modify():
    team_print(user_team)
    # Define the list of allowed letters
    allowed_letters = ['T', 'S', 'O', 'Q']

    while True:
        # Prompt for user input and convert to uppercase
        user_input = input(
            "To transfer a player, press T. \nTo view the opposition, press O. \nTo go back to messages, press S.\nTo quit, press Q").upper()

        if user_input in allowed_letters:
            # Valid input
            break
        else:
            print("Invalid input. Please select from available options.")

    # Continue with the rest of your program using the valid user input
    print("Valid input:", user_input)
    # if user_input=='T':
    #     player_transfer()
    if user_input == 'S':
        news_screen(x)
    elif user_input == 'O':
        view_opp()
    elif user_input == 'T':
        player_transfer_out()

    #     team_print()
    elif user_input == 'Q':
        quit()


home_team = None
away_team = None
week = 0

# view opposition


def view_opp():

    current_round = fixtures[week]

    for i in range(5):

        # code to calculate skill and form for home and away backs and forwards.

        home_team = current_round[i][0]
        away_team = current_round[i][1]

        if home_team == user_team:
            team_print(away_team)
        elif away_team == user_team:
            team_print(home_team)

    allowed_letters = ['S']  # Define the list of allowed letters

    while True:
        # Prompt for user input and convert to uppercase
        user_input = input("To go back to messages, press S.").upper()

        if user_input in allowed_letters:
            # Valid input
            break
        else:
            print("Invalid input. Please select from available options.")

    # Continue with the rest of your program using the valid user input
    print("Valid input:", user_input)
    # if user_input=='T':
    #     player_transfer()
    if user_input == 'S':
        news_screen(x)


def news_screen_options():
    # Define the list of allowed letters
    allowed_letters = ['S', 'M', 'O', 'Q']

    while True:
        # Prompt for user input and convert to uppercase
        user_input = input(
            "To view or modify squad, press S.\nTo view the opposition, press O.\nTo proceed to the next match, press M.\nTo quit, press Q: ").upper()

        flag = False  # Flag variable to track injured or suspended players

        if user_input in allowed_letters:
            if user_input == 'M':
                team_data = club_dict[user_team]
                for player_data in team_data['players'].values():
                    player_status = player_data['status']
                    player_name = player_data['name']
                    if player_status == 'Injured':
                        print(f"{player_name} is injured and must be replaced.")
                        print()
                        flag = True
                    elif player_status == 'Suspended':
                        print(f"{player_name} is banned and must be replaced.")
                        print()
                        flag = True

            if flag:
                continue  # Continue the loop if any player is injured or suspended

            # Valid input
            break
        else:
            print("Invalid input. Please select from available options.")

    # Continue with the rest of your program using the valid user input
    print("Valid input:", user_input)
    if user_input == 'S':
        team_modify()
    elif user_input == 'O':
        view_opp()
    elif user_input == 'Q':
        quit()

# news screen


def news_screen(x):
    hc_message = "hi from head coach!"
    s_message = "hi from the scout!"
    head_coach = "Head Coach"
    scout = "Scout"
    finance = "Finance Manager"
    f_rep = "Finance Report"
    s_opp = "Next Opponent Report"
    hc_perf = "Performance Report"
    hc_inj = "Fitness Report"
    hc_sus = "Suspension Report"

    # scout report
    current_round = fixtures[week]
    for i in range(5):
        home_team = current_round[i][0]
        away_team = current_round[i][1]

        if home_team == user_team:
            s_message = f"This week, we are playing at home against {away_team}"
            if club_dict[away_team]['total_skill'] > club_dict[user_team]['total_skill']:
                s_message = f"This week, we are playing at home against {away_team}.\n{away_team} have a strong team. We would benefit from investing in more quality or bringing in players who are in form."
            else:
                s_message = f"This week, we are playing at home against {away_team}.\nIf the players are on form, we should win."

        elif away_team == user_team:
            s_message = f"This week, we are playing away against {home_team}"
            if club_dict[home_team]['total_skill'] > club_dict[user_team]['total_skill']:
                s_message = f"This week, we are playing away against {home_team}.\n{home_team} have a strong team. We would benefit from investing in more quality or bringing in players who are in form."
            else:
                s_message = f"This week, we are playing at away against {home_team}.\nIf the players are on form, we should win."

    credit_balance = club_dict[user_team]['credit']

    team_data = club_dict[user_team]
    hc_inj_message = "No players are currently injured."
    hc_sus_message = "No players are currently suspended."
    hc_perf_message = "No players particularly stand out as major assets to the team."
    lo_hc_perf_message = "No players particularly stand out needing immediate improvement."
    f_message = f"We currently have €{credit_balance}k to spend on new players."

    inj_list = []
    susp_list = []
    lo_perf_list = []
    hi_perf_list = []

    for player_data in team_data['players'].values():
        player_status = player_data['status']
        player_info = player_data['info']
        player_name = player_data['name']
        player_skill = player_data['skill']
        player_form = player_data['form']

        if player_status == 'Injured':
            inj_list.append(player_name)

        elif player_status == 'Suspended':
            susp_list.append(player_name)

        elif player_skill < 71 or player_form < 4.0:

            lo_perf_list.append(player_name)
            if player_skill > 76:
                lo_perf_list.remove(player_name)

        elif player_skill >= 90:
            hi_perf_list.append(player_name)

        elif player_form > 7.0:
            hi_perf_list.append(player_name)

    inj = ', '.join(map(str, inj_list))
    sus = ', '.join(map(str, susp_list))
    lo_perf = ', '.join(map(str, lo_perf_list))
    hi_perf = ', '.join(map(str, hi_perf_list))

    if len(inj_list) > 0:
        hc_inj_message = f"Current injuries: {inj}"
    if len(susp_list) > 0:
        hc_sus_message = f"Current suspensions: {sus}"

    if len(lo_perf_list) > 0:
        lo_hc_perf_message = f"Players that are holding back the team with generally poor match form or skill level: \n{lo_perf}"

    if len(hi_perf_list) > 0:
        hc_perf_message = f"Players that leading by example with exceptional ability or good form: \n{hi_perf}"

    inj_list.clear()
    susp_list.clear()
    hi_perf_list.clear()
    lo_perf_list.clear()

    # news screen dict
    news_screen_dict = {
        'from_hc': head_coach,
        'from_s': scout,
        'from f': finance,
        'f rep': f_rep,
        'opp_report': s_opp,
        'performance': hc_perf,
        'injury_report': hc_inj,
        'sus_report': hc_sus,
        'hc_inj_message': hc_inj_message,
        'hc_sus_message': hc_sus_message,
        'hc_perf_report': hc_perf_message,
        'lo_hc_perf_report': lo_hc_perf_message,
        's_message': s_message,
        'f_message': f_message,
        'title': f"Team news for {manager_name} of {user_team}, it is Week:{week + 1}",
        'team': f"{user_team}"
    }

    # Create a PrettyTable instance
    table = PrettyTable()
    table.title = news_screen_dict['title']
    table.field_names = ['From', 'Subject', 'Message']
    # Create an empty row with the same number of columns
    empty_row = [""] * len(table.field_names)

    # Add rows to the table
    table.add_row([news_screen_dict['from f'],
                  news_screen_dict['f rep'], news_screen_dict['f_message']])
    table.add_row(empty_row)

    table.add_row([news_screen_dict['from_hc'],
                  news_screen_dict['performance'], news_screen_dict['hc_perf_report']])
    table.add_row(empty_row)
    table.add_row([news_screen_dict['from_hc'], news_screen_dict['performance'],
                  news_screen_dict['lo_hc_perf_report']])
    table.add_row(empty_row)

    table.add_row([news_screen_dict['from_hc'],
                  news_screen_dict['injury_report'], news_screen_dict['hc_inj_message']])
    table.add_row(empty_row)
    table.add_row([news_screen_dict['from_hc'],
                  news_screen_dict['sus_report'], news_screen_dict['hc_sus_message']])
    table.add_row(empty_row)
    table.add_row([news_screen_dict['from_s'],
                  news_screen_dict['opp_report'], news_screen_dict['s_message']])
    table.add_row(empty_row)

    # Print the table
    print(table)
    print()
    news_screen_options()

# lineup print


def lineup_print():
    home_team_players = []
    away_team_players = []

    for player in club_dict[home_team]["players"]:
        home_player = club_dict[home_team]["players"][player]["name"]
        if club_dict[home_team]["players"][player]["info"] == "*Star Player*":
            home_player += "*"
        home_team_players.append(home_player)

    for player in club_dict[away_team]["players"]:
        away_player = club_dict[away_team]["players"][player]["name"]
        if club_dict[away_team]["players"][player]["info"] == "*Star Player*":
            away_player = "*" + away_player
        away_team_players.append(away_player)

    # Create a PrettyTable instance
    table = PrettyTable()
    table.field_names = [f'{home_team}', 'v', f'{away_team}']

    # Add rows to the table
    for i, (home, away) in enumerate(zip(home_team_players, away_team_players), 1):
        i = str(i)
        if len(i) < 2:
            i = " " + i
        table.add_row([f'{home}', f'{i:^5s}', f'{away}'])

    # Print the table
    print(table)


def cont():

    allowed_letters = ['C', 'Q']  # Define the list of allowed letters

    while True:
        # Prompt for user input and convert to uppercase
        user_input = input("Press 'C' to continue.").upper()

        if user_input in allowed_letters:
            # Valid input
            break
        else:
            pass
    if user_input == 'Q':
        quit()

# functions to subract a week from injury and suspensions


def pos_inj_count(pos_dict):
    inj_text_2 = "{} weeks"
    inj_text = "{} week"
    ban_text = "{} week ban"
    form_txt = "+Form player+"
    star_txt = "*Star Player*"

    for player_id, player_data in pos_dict.items():
        player_status = player_data['status']
        player_info = player_data['info']
        player_skill = player_data['skill']
        player_form = player_data['form']
        player_id = player_data['player_id']
        player_inj = player_data['injured']
        player_sus = player_data['sus']
        injury_len = player_data['inj len']
        suspen_len = player_data['sus len']

        if player_inj:
            # print('inj before', player_inj)
            injury_len -= 1
            # print('inj after', player_inj)

            if injury_len == 1:
                player_info = inj_text.format(injury_len)
            elif injury_len > 1:
                player_info = inj_text_2.format(injury_len)
            elif injury_len == 0:
                if player_form > 8.4:
                    player_status = 'Fit'
                    player_info = form_txt
                if player_skill >= 90:
                    player_info = star_txt
                    player_status = 'Fit'
                else:
                    player_info = ""
                    player_status = 'Fit'

        elif player_sus:
            # print('sus before', suspen_len)
            suspen_len -= 1
            # print('sus after', suspen_len)

            if suspen_len == 1:
                player_info = ban_text.format(suspen_len)
            elif suspen_len > 1:
                player_info = ban_text.format(suspen_len)
            elif suspen_len == 0:
                if player_form > 8.4:
                    player_status = 'Fit'
                    player_info = form_txt
                if player_skill >= 90:
                    player_info = star_txt
                    player_status = 'Fit'
                else:
                    player_info = ""
                    player_status = 'Fit'

        # Update the values in the dictionary
        player_data['status'] = player_status
        player_data['info'] = player_info
        player_data['skill'] = player_skill
        player_data['form'] = player_form
        player_data['inj len'] = injury_len
        player_data['sus len'] = suspen_len


def club_inj_count(team):
    inj_text_2 = "{} weeks"
    inj_text = "{} week"
    ban_text = "{} week ban"
    form_txt = "+Form player+"
    star_txt = "*Star Player*"

    team_data = club_dict[team]

    for player_id, player_data in team_data['players'].items():
        player_inj = player_data['injured']
        player_sus = player_data['sus']
        player_status = player_data['status']
        player_info = player_data['info']
        player_skill = player_data['skill']
        player_form = player_data['form']
        player_id = player_data['player_id']
        injury_len = player_data['inj len']
        suspen_len = player_data['sus len']

        if player_inj:
            # print('inj before', player_info)
            # print('inj len', injury_len)
            injury_len -= 1

            if injury_len == 1:
                player_info = inj_text.format(injury_len)
            elif injury_len > 1:
                player_info = inj_text_2.format(injury_len)
            elif injury_len == 0:
                if player_form > 8.4:
                    player_status = 'Fit'
                    player_info = form_txt
                if player_skill >= 90:
                    player_info = star_txt
                    player_status = 'Fit'
                else:
                    player_info = ""
                    player_status = 'Fit'

            # print('inj after', player_info)
            # print('inj len', injury_len)

        elif player_sus:
            # print('sus before', player_info)
            # print('sus len', suspen_len)
            suspen_len -= 1

            if suspen_len == 1:
                player_info = ban_text.format(suspen_len)
            elif suspen_len > 1:
                player_info = ban_text.format(suspen_len)
            elif suspen_len == 0:
                if player_form > 8.4:
                    player_status = 'Fit'
                    player_info = form_txt
                if player_skill >= 90:
                    player_info = star_txt
                    player_status = 'Fit'
                else:
                    player_info = ""
                    player_status = 'Fit'

            # print('sus after', player_info)
            # print('sus len', suspen_len)

        # Update the values in the dictionary
        player_data['injured'] = player_inj
        player_data['sus'] = player_sus
        player_data['status'] = player_status
        player_data['info'] = player_info
        player_data['skill'] = player_skill
        player_data['form'] = player_form
        player_data['inj len'] = injury_len
        player_data['sus len'] = suspen_len


# main gam eloop
while week < 9:

    player_out_cpu()

    print(f"this is the news screen and it is week{week+1}")
    # print news screen
    news_screen(week)

    # print Round
    round_num = week+1
    print_round(round_num)
    cont()

    # comparing home and away skill totals to produce skill points difference number

    current_round = fixtures[week]
    home = []
    away = []

    # calculate round scores

    for i in range(5):

        home_score = 0
        away_score = 0

        home_team = current_round[i][0]
        away_team = current_round[i][1]

        home_team_data = club_dict[home_team]

        home_skill = home_team_data['total_skill']

        away_team_data = club_dict[away_team]

        away_skill = away_team_data['total_skill']

        home_score += home_skill
        away_score += away_skill

        # incorporate form into score:

        # calculate form for each team

        home_form = 0
        away_form = 0

        for player_data in home_team_data['players'].values():
            home_form += player_data['form']

        for player_data in away_team_data['players'].values():
            away_form += player_data['form']

        home_score *= home_form
        away_score *= away_form

        home_score /= 1000
        away_score /= 1000

        home_score -= 100
        away_score -= 100

        home_score = round(home_score)
        away_score = round(away_score)

        if home_score < 3:
            home_score = 0
        elif home_score < 5:
            home_score = 3

        if away_score < 3:
            away_score = 0
        elif away_score < 5:
            away_score = 3

        # key players

        # for i in home_team_data['players'].values():
        #     if home_team_data['players']['position']=='Fly Half':
        #         home_fh=home_team_data['players']['name']
        #
        #
        # def penalty(home_or_away_score,minute,home_or_away_fh):
        #
        #     print(f"PEN {minute}, {home_or_away_fh}")
        #
        #
        # def tri_conv(home_or_away_score,home_or_away_fh):
        #
        #
        #
        # def tri(home_or_away_score,home_or_away_fh):

        # print(home_score)
        # print(away_score)

        full_minutes = list(range(0, 81))
        home_event_minutes = []
        away_event_minutes = []

        # function to identify the points value in scorelines

        def distribute_numbers(home_or_away_score, points, weights):
            goal_list = []
            goal_total = 0

            while goal_total != home_or_away_score:
                goal = random.choices(points, weights)[0]
                goal_list.append(goal)
                goal_total += goal

                if goal_total > home_or_away_score:
                    diff = goal_total - home_or_away_score
                    if diff in goal_list:
                        goal_total -= diff
                        goal_list.remove(diff)
                    else:
                        # Reset goal_total and goal_list if the difference is not in points
                        goal_total = 0
                        goal_list = []
                elif goal_total < home_or_away_score:
                    diff = home_or_away_score - goal_total
                    if diff in points:
                        goal_total += diff
                        goal_list.append(diff)

            return goal_list


# home points identify

        home_goal_list = distribute_numbers(home_score, [3, 5, 7], [3, 1, 2])
        # print("home score",home_score)
        # print("home goals",home_goal_list)
        scores_q = len(home_goal_list)


# identify home fly half


        def fh(home_team):

            for player_data in home_team_data['players'].values():
                if player_data['position'] == 'Fly Half':
                    p_name = player_data['name']
                    p_name = p_name.split()
                    surname = p_name[1]
                    p_skill = player_data['skill']
                    p_form = player_data['form']
                    p_id = player_data['player_id']
                    home_fh = (p_skill, p_form, surname, p_id)

                    return home_fh
        home_fh = fh(home_team)
        h_fh_name = home_fh[2]
        # print(home_fh)

   # function to gather playing stats of players in team

        def player_stats(home_team):
            stat_list = []
            for player_data in home_team_data['players'].values():
                p_name = player_data['name']
                p_name = p_name.split()
                surname = p_name[1]
                p_skill = player_data['skill']
                p_form = player_data['form']
                p_id = player_data['player_id']
                p_stats = (p_skill, p_form, surname, p_id)
                stat_list.append(p_stats)
                stat_list = sorted(stat_list, key=lambda x: (x[1], x[0]))

            return stat_list
        home_stat_list = player_stats(home_team)
        # print(home_stat_list)

        # generate weights

        home_minute_list = []

        if home_score > 0:

            weights = list(range(1, len(home_stat_list) + 1))
            home_scorers_selection = random.choices(
                home_stat_list, weights=weights, k=scores_q)

            # identify the minute the score was made (followed by conversion/missed conversion if a try)

            for goal in home_goal_list:
                minute = random.choice(full_minutes)
                full_minutes.remove(minute)
                home_minute_list.append(minute)

            combined_list = [[x, y]
                             for x, y in zip(home_goal_list, home_minute_list)]
            home_event_minutes = sorted(combined_list, key=lambda x: x[1])
            home_minute_list = sorted(home_minute_list)

            # print("home goals ",home_goal_list)
            # print("home minutes ", home_minute_list)
            # print("home scorers: ",home_scorers_selection)


# away points identify

        away_goal_list = distribute_numbers(away_score, [3, 5, 7], [3, 1, 2])
        # print("away score",away_score)
        # print("away goals",away_goal_list)
        scores_q = len(away_goal_list)


# identify away team fh


        def fh(away_team):

            for player_data in away_team_data['players'].values():
                if player_data['position'] == 'Fly Half':
                    p_name = player_data['name']
                    p_name = p_name.split()
                    surname = p_name[1]
                    p_skill = player_data['skill']
                    p_form = player_data['form']
                    p_id = player_data['player_id']
                    away_fh = (p_skill, p_form, surname, p_id)

                    return away_fh
        away_fh = fh(away_team)
        a_fh_name = away_fh[2]
        # print(away_fh)
   #

   # function to gather playing stats of players in team

        def player_stats(away_team):
            stat_list = []
            for player_data in away_team_data['players'].values():
                p_name = player_data['name']
                p_name = p_name.split()
                surname = p_name[1]
                p_skill = player_data['skill']
                p_form = player_data['form']
                p_id = player_data['player_id']
                p_stats = (p_skill, p_form, surname, p_id)
                stat_list.append(p_stats)
                stat_list = sorted(stat_list, key=lambda x: (x[1], x[0]))

            return stat_list
        away_stat_list = player_stats(away_team)
        # print(away_stat_list)

        # generate weights

        away_minute_list = []

        if away_score > 0:

            weights = list(range(1, len(away_stat_list) + 1))
            away_scorers_selection = random.choices(
                away_stat_list, weights=weights, k=scores_q)

            # identify the minute the score was made (followed by conversion/missed conversion if a try)

            for goal in away_goal_list:
                minute = random.choice(full_minutes)
                full_minutes.remove(minute)
                away_minute_list.append(minute)

            combined_list = [[x, y]
                             for x, y in zip(away_goal_list, away_minute_list)]
            away_event_minutes = sorted(combined_list, key=lambda x: x[1])
            away_minute_list = sorted(away_minute_list)

            # print("away goals ",away_goal_list)
            # print("away minutes ", away_minute_list)
            # print("away scorers: ",away_scorers_selection)

        # match process
        import time
        import sys

        clock = 0
        x = 0
        y = 0
        home_sc = 0
        away_sc = 0
        home_scorers = []
        away_scorers = []
# user match simulations
        if user_team == home_team or user_team == away_team:

            lineup_print()
            cont()

            while clock < 81:
                sys.stdout.write(f"\rClock: {clock:<10} ")
                sys.stdout.write(
                    f"{home_team} {home_sc} - {away_sc} {away_team}")
                sys.stdout.flush()
     # home match simulation
                if len(home_minute_list) > 0 and clock == home_minute_list[y]:

                    home_goal = home_goal_list[y]

                    if home_goal == 3:

                        event_line = f"PENALTY to {home_team}!"
                        sys.stdout.write(f"\r{' ' * 150}")
                        sys.stdout.write(f"\rClock: {clock:<10} ")
                        sys.stdout.write(
                            f"{home_team} {home_sc} - {away_sc} {away_team}")
                        sys.stdout.write(f"{event_line:>80}")
                        sys.stdout.flush()
                        time.sleep(5)
                        event_line = f"{h_fh_name} nails penalty!"
                        home_sc += home_goal_list[y]
                        sys.stdout.write(f"\r{' ' * 150}")
                        sys.stdout.write(f"\rClock: {clock:<10} ")
                        sys.stdout.write(
                            f"{home_team} {home_sc} - {away_sc} {away_team}")
                        sys.stdout.write(f"{event_line:>80}")
                        sys.stdout.flush()

                        time.sleep(5)
                        sys.stdout.write(f"\r{' ' * 150}")
                        sys.stdout.write(f"\rClock: {clock:<10} ")
                        sys.stdout.write(
                            f"{home_team} {home_sc} - {away_sc} {away_team}")
                        sys.stdout.flush()

                        home_minute_list.remove(home_minute_list[x])
                        home_goal_list.remove(home_goal)
                        home_scorers.append(home_fh)

                        # update player form and popints scored in club dicts - this method works!
                        id = home_fh[3]
                        player = club_dict[home_team]['players'][id]
                        form = club_dict[home_team]['players'][id]['form']
                        form += 0.1
                        form = round(form, 1)
                        club_dict[home_team]['players'][id]['form'] = form
                        if form > 9.5:
                            club_dict[home_team]['players'][id]['form'] = 9.5

                        if club_dict[home_team]['players'][id]['form'] > 8.4 and club_dict[home_team]['players'][id]['skill'] < 90:
                            club_dict[home_team]['players'][id]['info'] = form_txt

                        club_dict[home_team]['players'][id]['game pts'] += 3
                        club_dict[home_team]['players'][id]['total pts'] += 3

                        # print(player)

                    elif home_goal == 5:
                        # change scoer to surname

                        scorer = random.choice(home_scorers_selection)
                        scorer_name = scorer[2]
                        try_quotes = [
                            f"{scorer_name} breaks through the defense and scores for a brilliant individual effort!"]
                        quote = random.choice(try_quotes)

                        event_line = f"TRY! {home_team} {clock:>3}' mins."
                        sys.stdout.write(f"\r{' ' * 150}")
                        home_sc += 5
                        sys.stdout.write(f"\rClock: {clock:<10} ")
                        sys.stdout.write(
                            f"{home_team} {home_sc} - {away_sc} {away_team}")
                        sys.stdout.write(f"{event_line:>80}")
                        sys.stdout.flush()
                        time.sleep(5)
                        event_line = f"{quote}"
                        sys.stdout.write(f"\r{' ' * 150}")
                        sys.stdout.write(f"\rClock: {clock:<10} ")
                        sys.stdout.write(
                            f"{home_team} {home_sc} - {away_sc} {away_team}")
                        sys.stdout.write(f"{event_line:>80}")
                        sys.stdout.flush()
                        time.sleep(5)
                        event_line = f"{h_fh_name} misses conversion."
                        sys.stdout.write(f"\r{' ' * 150}")
                        sys.stdout.write(f"\rClock: {clock:<10} ")
                        sys.stdout.write(
                            f"{home_team} {home_sc} - {away_sc} {away_team}")
                        sys.stdout.write(f"{event_line:>80}")
                        sys.stdout.flush()
                        time.sleep(5)
                        sys.stdout.write(f"\r{' ' * 150}")
                        sys.stdout.write(f"\rClock: {clock:<10} ")
                        sys.stdout.write(
                            f"{home_team} {home_sc} - {away_sc} {away_team}")
                        sys.stdout.flush()

                        home_minute_list.remove(home_minute_list[x])
                        home_goal_list.remove(home_goal)
                        home_scorers.append(scorer)

                        id = scorer[3]
                        player = club_dict[home_team]['players'][id]

                        form = club_dict[home_team]['players'][id]['form']
                        form += 0.2
                        form = round(form, 1)
                        club_dict[home_team]['players'][id]['form'] = form
                        if form > 9.5:
                            club_dict[home_team]['players'][id]['form'] = 9.5

                        if club_dict[home_team]['players'][id]['form'] > 8.4 and club_dict[home_team]['players'][id]['skill'] < 90:
                            club_dict[home_team]['players'][id]['info'] = form_txt

                        club_dict[home_team]['players'][id]['game pts'] += 5
                        club_dict[home_team]['players'][id]['total pts'] += 5

                        # print(player)

                        id = home_fh[3]
                        player = club_dict[home_team]['players'][id]
                        form = club_dict[home_team]['players'][id]['form']
                        form -= 0.1
                        form = round(form, 1)
                        club_dict[home_team]['players'][id]['form'] = form
                        if form > 9.5:
                            club_dict[home_team]['players'][id]['form'] = 9.5

                        if club_dict[home_team]['players'][id]['form'] < 3.0 and club_dict[home_team]['players'][id]['skill'] < 90:
                            club_dict[home_team]['players'][id]['info'] = ""

                        # print(player)

                    elif home_goal == 7:

                        # change scoer to surname

                        scorer = random.choice(home_scorers_selection)
                        scorer_name = scorer[2]
                        try_quotes = [
                            f"Great team effort as {scorer_name} breaks through and touches down!"]
                        quote = random.choice(try_quotes)

                        event_line = f"TRY! {home_team} {clock:>3}' mins."
                        home_sc += 5
                        sys.stdout.write(f"\r{' ' * 150}")
                        sys.stdout.write(f"\rClock: {clock:<10} ")
                        sys.stdout.write(
                            f"{home_team} {home_sc} - {away_sc} {away_team}")
                        sys.stdout.write(f"{event_line:>80}")
                        sys.stdout.flush()
                        time.sleep(5)
                        event_line = f"{quote}"
                        sys.stdout.write(f"\r{' ' * 150}")
                        sys.stdout.write(f"\rClock: {clock:<10} ")
                        sys.stdout.write(
                            f"{home_team} {home_sc} - {away_sc} {away_team}")
                        sys.stdout.write(f"{event_line:>80}")
                        sys.stdout.flush()
                        time.sleep(5)
                        event_line = f"{h_fh_name} adds the extras!"
                        home_sc += 2
                        sys.stdout.write(f"\r{' ' * 150}")
                        sys.stdout.write(f"\rClock: {clock:<10} ")
                        sys.stdout.write(
                            f"{home_team} {home_sc} - {away_sc} {away_team}")
                        sys.stdout.write(f"{event_line:>80}")
                        sys.stdout.flush()
                        time.sleep(5)
                        sys.stdout.write(f"\r{' ' * 150}")
                        sys.stdout.write(f"\rClock: {clock:<10} ")
                        sys.stdout.write(
                            f"{home_team} {home_sc} - {away_sc} {away_team}")
                        sys.stdout.flush()

                        home_minute_list.remove(home_minute_list[x])
                        home_goal_list.remove(home_goal)
                        home_scorers.append(scorer)
                        home_scorers.append(home_fh)

                        id = scorer[3]
                        player = club_dict[home_team]['players'][id]

                        form = club_dict[home_team]['players'][id]['form']
                        form += 0.2
                        form = round(form, 1)
                        club_dict[home_team]['players'][id]['form'] = form
                        if form > 9.5:
                            club_dict[home_team]['players'][id]['form'] = 9.5

                        if club_dict[home_team]['players'][id]['form'] > 8.4 and club_dict[home_team]['players'][id]['skill'] < 90:
                            club_dict[home_team]['players'][id]['info'] = form_txt

                        club_dict[home_team]['players'][id]['game pts'] += 5
                        club_dict[home_team]['players'][id]['total pts'] += 5

                        # print(player)

                        id = home_fh[3]
                        player = club_dict[home_team]['players'][id]

                        form = club_dict[home_team]['players'][id]['form']
                        form += 0.1
                        form = round(form, 1)
                        club_dict[home_team]['players'][id]['form'] = form
                        if form > 9.5:
                            club_dict[home_team]['players'][id]['form'] = 9.5

                        if club_dict[home_team]['players'][id]['form'] > 8.4 and club_dict[home_team]['players'][id]['skill'] < 90:
                            club_dict[home_team]['players'][id]['info'] = form_txt

                        club_dict[home_team]['players'][id]['game pts'] += 2
                        club_dict[home_team]['players'][id]['total pts'] += 2

                        # print(player)

     # away match simulation
                if len(away_minute_list) > 0 and clock == away_minute_list[y]:

                    away_goal = away_goal_list[y]

                    if away_goal == 3:

                        event_line = f"PENALTY to {away_team}!"
                        sys.stdout.write(f"\r{' ' * 150}")
                        sys.stdout.write(f"\rClock: {clock:<10} ")
                        sys.stdout.write(
                            f"{home_team} {home_sc} - {away_sc} {away_team}")
                        sys.stdout.write(f"{event_line:>80}")
                        sys.stdout.flush()
                        time.sleep(5)
                        event_line = f"{a_fh_name} nails penalty!"
                        away_sc += away_goal_list[y]
                        sys.stdout.write(f"\r{' ' * 150}")
                        sys.stdout.write(f"\rClock: {clock:<10} ")
                        sys.stdout.write(
                            f"{home_team} {home_sc} - {away_sc} {away_team}")
                        sys.stdout.write(f"{event_line:>80}")
                        sys.stdout.flush()
                        time.sleep(5)
                        sys.stdout.write(f"\r{' ' * 150}")
                        sys.stdout.write(f"\rClock: {clock:<10} ")
                        sys.stdout.write(
                            f"{home_team} {home_sc} - {away_sc} {away_team}")
                        sys.stdout.flush()

                        away_minute_list.remove(away_minute_list[x])
                        away_goal_list.remove(away_goal)
                        away_scorers.append(away_fh)

                        # update player form and popints scored in club dicts - this method works!
                        id = away_fh[3]
                        player = club_dict[away_team]['players'][id]
                        form = club_dict[away_team]['players'][id]['form']
                        form += 0.1
                        form = round(form, 1)
                        club_dict[away_team]['players'][id]['form'] = form
                        if form > 9.5:
                            club_dict[away_team]['players'][id]['form'] = 9.5

                        if club_dict[away_team]['players'][id]['form'] > 8.4 and club_dict[away_team]['players'][id]['skill'] < 90:
                            club_dict[away_team]['players'][id]['info'] = form_txt

                        club_dict[away_team]['players'][id]['game pts'] += 3
                        club_dict[away_team]['players'][id]['total pts'] += 3

                        # print(player)

                    elif away_goal == 5:
                        # change scoer to surname

                        scorer = random.choice(away_scorers_selection)
                        scorer_name = scorer[2]
                        try_quotes = [
                            f"{scorer_name} breaks through the defense and scores for a brilliant individual effort!"]
                        quote = random.choice(try_quotes)

                        event_line = f"TRY! {away_team} {clock:>3}' mins."
                        away_sc += 5
                        sys.stdout.write(f"\r{' ' * 150}")
                        sys.stdout.write(f"\rClock: {clock:<10} ")
                        sys.stdout.write(
                            f"{home_team} {home_sc} - {away_sc} {away_team}")
                        sys.stdout.write(f"{event_line:>80}")
                        sys.stdout.flush()
                        time.sleep(5)
                        event_line = f"{quote}"
                        sys.stdout.write(f"\r{' ' * 150}")
                        sys.stdout.write(f"\rClock: {clock:<10} ")
                        sys.stdout.write(
                            f"{home_team} {home_sc} - {away_sc} {away_team}")
                        sys.stdout.write(f"{event_line:>80}")
                        sys.stdout.flush()
                        time.sleep(5)
                        event_line = f"{a_fh_name} misses conversion."
                        sys.stdout.write(f"\r{' ' * 150}")
                        sys.stdout.write(f"\rClock: {clock:<10} ")
                        sys.stdout.write(
                            f"{home_team} {home_sc} - {away_sc} {away_team}")
                        sys.stdout.write(f"{event_line:>80}")
                        sys.stdout.flush()
                        time.sleep(5)
                        sys.stdout.write(f"\r{' ' * 150}")
                        sys.stdout.write(f"\rClock: {clock:<10} ")
                        sys.stdout.write(
                            f"{home_team} {home_sc} - {away_sc} {away_team}")
                        sys.stdout.flush()

                        away_minute_list.remove(away_minute_list[x])
                        away_goal_list.remove(away_goal)
                        away_scorers.append(scorer)

                        id = scorer[3]
                        player = club_dict[away_team]['players'][id]

                        form = club_dict[away_team]['players'][id]['form']
                        form += 0.2
                        form = round(form, 1)
                        club_dict[away_team]['players'][id]['form'] = form
                        if form > 9.5:
                            club_dict[away_team]['players'][id]['form'] = 9.5

                        if club_dict[away_team]['players'][id]['form'] > 8.4 and club_dict[away_team]['players'][id]['skill'] < 90:
                            club_dict[away_team]['players'][id]['info'] = form_txt

                        club_dict[away_team]['players'][id]['game pts'] += 5
                        club_dict[away_team]['players'][id]['total pts'] += 5

                        # print(player)

                        id = away_fh[3]
                        player = club_dict[away_team]['players'][id]
                        # print(player)
                        form = club_dict[away_team]['players'][id]['form']
                        form -= 0.1
                        form = round(form, 1)
                        club_dict[away_team]['players'][id]['form'] = form
                        if form > 9.5:
                            club_dict[away_team]['players'][id]['form'] = 9.5

                        if club_dict[away_team]['players'][id]['form'] < 3.0 and club_dict[away_team]['players'][id]['skill'] < 90:
                            club_dict[away_team]['players'][id]['info'] = form_txt

                        # print(player)

                    elif away_goal == 7:

                        # change scoer to surname

                        scorer = random.choice(away_scorers_selection)
                        scorer_name = scorer[2]
                        try_quotes = [
                            f"Great team effort as {scorer_name} breaks through and touches down!"]
                        quote = random.choice(try_quotes)

                        event_line = f"TRY! {away_team} {clock:>3}' mins."
                        away_sc += 5
                        sys.stdout.write(f"\r{' ' * 150}")
                        sys.stdout.write(f"\rClock: {clock:<10} ")
                        sys.stdout.write(
                            f"{home_team} {home_sc} - {away_sc} {away_team}")
                        sys.stdout.write(f"{event_line:>80}")
                        sys.stdout.flush()
                        time.sleep(5)
                        event_line = f"{quote}"
                        sys.stdout.write(f"\r{' ' * 150}")
                        sys.stdout.write(f"\rClock: {clock:<10} ")
                        sys.stdout.write(
                            f"{home_team} {home_sc} - {away_sc} {away_team}")
                        sys.stdout.write(f"{event_line:>80}")
                        sys.stdout.flush()
                        time.sleep(5)
                        event_line = f"{a_fh_name} adds the extras!"
                        away_sc += 2
                        sys.stdout.write(f"\r{' ' * 150}")
                        sys.stdout.write(f"\rClock: {clock:<10} ")
                        sys.stdout.write(
                            f"{home_team} {home_sc} - {away_sc} {away_team}")
                        sys.stdout.write(f"{event_line:>80}")
                        sys.stdout.flush()
                        time.sleep(5)
                        sys.stdout.write(f"\r{' ' * 150}")
                        sys.stdout.write(f"\rClock: {clock:<10} ")
                        sys.stdout.write(
                            f"{home_team} {home_sc} - {away_sc} {away_team}")
                        sys.stdout.flush()

                        away_minute_list.remove(away_minute_list[x])
                        away_goal_list.remove(away_goal)
                        away_scorers.append(scorer)
                        away_scorers.append(away_fh)

                        id = scorer[3]
                        player = club_dict[away_team]['players'][id]

                        form = club_dict[away_team]['players'][id]['form']
                        form += 0.2
                        form = round(form, 1)
                        club_dict[away_team]['players'][id]['form'] = form
                        if form > 9.5:
                            club_dict[away_team]['players'][id]['form'] = 9.5

                        if club_dict[away_team]['players'][id]['form'] > 8.4 and club_dict[away_team]['players'][id]['skill'] < 90:
                            club_dict[away_team]['players'][id]['info'] = form_txt

                        club_dict[away_team]['players'][id]['game pts'] += 5
                        club_dict[away_team]['players'][id]['total pts'] += 5

                        # print(player)

                        id = away_fh[3]
                        player = club_dict[away_team]['players'][id]

                        form = club_dict[away_team]['players'][id]['form']
                        form += 0.1
                        form = round(form, 1)
                        club_dict[away_team]['players'][id]['form'] = form
                        if form > 9.5:
                            club_dict[away_team]['players'][id]['form'] = 9.5

                        if club_dict[away_team]['players'][id]['form'] > 8.4 and club_dict[away_team]['players'][id]['skill'] < 90:
                            club_dict[away_team]['players'][id]['info'] = form_txt

                        club_dict[away_team]['players'][id]['game pts'] += 2
                        club_dict[away_team]['players'][id]['total pts'] += 2

                        # print(player)

                clock += 1
                time.sleep(1)

            sys.stdout.write(f"\r{' ' * 150}")
            print(f"\rFT: {home_team} {home_sc} - {away_sc} {away_team}")

            # print("\nMatch end")
            # print("home scorers ", home_scorers)
            # print("away scorers ", away_scorers)

# cpu match simulations
        else:

            while clock < 81:

             # home match simulation
                if len(home_minute_list) > 0 and clock == home_minute_list[y]:

                    home_goal = home_goal_list[y]

                    if home_goal == 3:

                        home_sc += home_goal_list[y]
                        home_minute_list.remove(home_minute_list[x])
                        home_goal_list.remove(home_goal)
                        home_scorers.append(home_fh)

                        # update player form and popints scored in club dicts - this method works!
                        id = home_fh[3]
                        player = club_dict[home_team]['players'][id]
                        # print(player)
                        form = club_dict[home_team]['players'][id]['form']
                        form += 0.1
                        form = round(form, 1)
                        club_dict[home_team]['players'][id]['form'] = form
                        if form > 9.5:
                            club_dict[home_team]['players'][id]['form'] = 9.5

                        if club_dict[home_team]['players'][id]['form'] > 8.4 and club_dict[home_team]['players'][id]['skill'] < 90:
                            club_dict[home_team]['players'][id]['info'] = form_txt

                        club_dict[home_team]['players'][id]['game pts'] += 3
                        club_dict[home_team]['players'][id]['total pts'] += 3

                    elif home_goal == 5:
                        # change scoer to surname

                        scorer = random.choice(home_scorers_selection)
                        scorer_name = scorer[2]
                        try_quotes = [
                            f"{scorer_name} breaks through the defense and scores for a brilliant individual effort!"]
                        quote = random.choice(try_quotes)

                        home_sc += 5

                        home_minute_list.remove(home_minute_list[x])
                        home_goal_list.remove(home_goal)
                        home_scorers.append(scorer)

                        id = scorer[3]
                        player = club_dict[home_team]['players'][id]

                        form = club_dict[home_team]['players'][id]['form']
                        form += 0.2
                        form = round(form, 1)
                        club_dict[home_team]['players'][id]['form'] = form
                        if form > 9.5:
                            club_dict[home_team]['players'][id]['form'] = 9.5

                        if club_dict[home_team]['players'][id]['form'] > 8.4 and club_dict[home_team]['players'][id]['skill'] < 90:
                            club_dict[home_team]['players'][id]['info'] = form_txt

                        club_dict[home_team]['players'][id]['game pts'] += 5
                        club_dict[home_team]['players'][id]['total pts'] += 5

                        id = home_fh[3]
                        player = club_dict[home_team]['players'][id]
                        # print(player)
                        form = club_dict[home_team]['players'][id]['form']
                        form -= 0.1
                        form = round(form, 1)
                        club_dict[home_team]['players'][id]['form'] = form
                        if form > 9.5:
                            club_dict[home_team]['players'][id]['form'] = 9.5

                        if club_dict[home_team]['players'][id]['form'] < 3.0 and club_dict[home_team]['players'][id]['skill'] < 90:
                            club_dict[home_team]['players'][id]['info'] = form_txt

                    elif home_goal == 7:

                        # change scoer to surname

                        scorer = random.choice(home_scorers_selection)
                        scorer_name = scorer[2]
                        try_quotes = [
                            f"Great team effort as {scorer_name} breaks through and touches down!"]
                        quote = random.choice(try_quotes)

                        home_sc += 5
                        home_sc += 2

                        home_minute_list.remove(home_minute_list[x])
                        home_goal_list.remove(home_goal)
                        home_scorers.append(scorer)
                        home_scorers.append(home_fh)

                        id = scorer[3]
                        player = club_dict[home_team]['players'][id]

                        form = club_dict[home_team]['players'][id]['form']
                        form += 0.2
                        form = round(form, 1)
                        club_dict[home_team]['players'][id]['form'] = form
                        if form > 9.5:
                            club_dict[home_team]['players'][id]['form'] = 9.5

                        if club_dict[home_team]['players'][id]['form'] > 8.4 and club_dict[home_team]['players'][id]['skill'] < 90:
                            club_dict[home_team]['players'][id]['info'] = form_txt

                        club_dict[home_team]['players'][id]['game pts'] += 5
                        club_dict[home_team]['players'][id]['total pts'] += 5

                        id = home_fh[3]
                        player = club_dict[home_team]['players'][id]

                        form = club_dict[home_team]['players'][id]['form']
                        form += 0.1
                        form = round(form, 1)
                        club_dict[home_team]['players'][id]['form'] = form
                        if form > 9.5:
                            club_dict[home_team]['players'][id]['form'] = 9.5

                        if club_dict[home_team]['players'][id]['form'] > 8.4 and club_dict[home_team]['players'][id]['skill'] < 90:
                            club_dict[home_team]['players'][id]['info'] = form_txt

                        club_dict[home_team]['players'][id]['game pts'] += 2
                        club_dict[home_team]['players'][id]['total pts'] += 2

     # away match simulation
                if len(away_minute_list) > 0 and clock == away_minute_list[y]:

                    away_goal = away_goal_list[y]

                    if away_goal == 3:

                        away_sc += away_goal_list[y]

                        away_minute_list.remove(away_minute_list[x])
                        away_goal_list.remove(away_goal)
                        away_scorers.append(away_fh)

                        # update player form and popints scored in club dicts - this method works!
                        id = away_fh[3]
                        player = club_dict[away_team]['players'][id]
                        # print(player)
                        form = club_dict[away_team]['players'][id]['form']
                        form += 0.1
                        form = round(form, 1)
                        club_dict[away_team]['players'][id]['form'] = form
                        if form > 9.5:
                            club_dict[away_team]['players'][id]['form'] = 9.5

                        if club_dict[away_team]['players'][id]['form'] > 8.4 and club_dict[away_team]['players'][id]['skill'] < 90:
                            club_dict[away_team]['players'][id]['info'] = form_txt

                        club_dict[away_team]['players'][id]['game pts'] += 3
                        club_dict[away_team]['players'][id]['total pts'] += 3

                    elif away_goal == 5:
                        # change scoer to surname

                        scorer = random.choice(away_scorers_selection)
                        scorer_name = scorer[2]
                        try_quotes = [
                            f"{scorer_name} breaks through the defense and scores for a brilliant individual effort!"]
                        quote = random.choice(try_quotes)

                        away_sc += 5

                        away_minute_list.remove(away_minute_list[x])
                        away_goal_list.remove(away_goal)
                        away_scorers.append(scorer)

                        id = scorer[3]
                        player = club_dict[away_team]['players'][id]

                        form = club_dict[away_team]['players'][id]['form']
                        form += 0.2
                        form = round(form, 1)
                        club_dict[away_team]['players'][id]['form'] = form
                        if form > 9.5:
                            club_dict[away_team]['players'][id]['form'] = 9.5

                        if club_dict[away_team]['players'][id]['form'] > 8.4 and club_dict[away_team]['players'][id]['skill'] < 90:
                            club_dict[away_team]['players'][id]['info'] = form_txt

                        club_dict[away_team]['players'][id]['game pts'] += 5
                        club_dict[away_team]['players'][id]['total pts'] += 5

                        id = away_fh[3]
                        player = club_dict[away_team]['players'][id]
                        # print(player)
                        form = club_dict[away_team]['players'][id]['form']
                        form -= 0.1
                        form = round(form, 1)
                        club_dict[away_team]['players'][id]['form'] = form
                        if form > 9.5:
                            club_dict[away_team]['players'][id]['form'] = 9.5

                        if club_dict[away_team]['players'][id]['form'] < 3.0 and club_dict[away_team]['players'][id]['skill'] < 90:
                            club_dict[away_team]['players'][id]['info'] = form_txt

                    elif away_goal == 7:

                        # change scoer to surname

                        scorer = random.choice(away_scorers_selection)
                        scorer_name = scorer[2]
                        try_quotes = [
                            f"Great team effort as {scorer_name} breaks through and touches down!"]
                        quote = random.choice(try_quotes)

                        away_sc += 5
                        away_sc += 2

                        away_minute_list.remove(away_minute_list[x])
                        away_goal_list.remove(away_goal)
                        away_scorers.append(scorer)
                        away_scorers.append(away_fh)

                        id = scorer[3]
                        player = club_dict[away_team]['players'][id]

                        form = club_dict[away_team]['players'][id]['form']
                        form += 0.2
                        form = round(form, 1)
                        club_dict[away_team]['players'][id]['form'] = form
                        if form > 9.5:
                            club_dict[away_team]['players'][id]['form'] = 9.5

                        if club_dict[away_team]['players'][id]['form'] > 8.4 and club_dict[away_team]['players'][id]['skill'] < 90:
                            club_dict[away_team]['players'][id]['info'] = form_txt

                        club_dict[away_team]['players'][id]['game pts'] += 5
                        club_dict[away_team]['players'][id]['total pts'] += 5

                        id = away_fh[3]
                        player = club_dict[away_team]['players'][id]

                        form = club_dict[away_team]['players'][id]['form']
                        form += 0.1
                        form = round(form, 1)
                        club_dict[away_team]['players'][id]['form'] = form
                        if form > 9.5:
                            club_dict[away_team]['players'][id]['form'] = 9.5

                        if club_dict[away_team]['players'][id]['form'] > 8.4 and club_dict[away_team]['players'][id]['skill'] < 90:
                            club_dict[away_team]['players'][id]['info'] = form_txt

                        club_dict[away_team]['players'][id]['game pts'] += 2
                        club_dict[away_team]['players'][id]['total pts'] += 2

                clock += 1

            # print("\nMatch end")
            # print("home scorers ", home_scorers)
            # print("away scorers ", away_scorers)

        #  to do list

        # update player skill in club dict dependant on performance after each Match (may include weighted random up or down if not on scoresheet)
        # random suspensions after each match.
        # random injuries after each match.
        # injuries, suspensions, form above 8.5 or star player will be automatically updated.
        # need solution to report individual performances.
        # make decision on substitutes - half time etc.
        # reset each players game points after player performance reports are returned.
        # player points leaderboard?
        # extra column in player dicts for value? maybe not obvious that value equates to skill number!?
        # value goes up when skill goes up etc. does not change transfer mechanics in this system.

        # first stage complete

        # need to find some way of pre defining game outcomes

        # for a final score to be achieved, there needs to be events in the game where points are scored.
        # the events have attributes: points scored on each event, the frequency of events, the variety of events.
        # the frequency of events can be completely random. the points scored needs to be managed to control game outcome.
        # the variety of events makes the match experience interesting and real.

        # logically, a final score should be the first numbers to generate. this has been done above and generates realist numbers.
        # these final scores are based on team skill and form. there are not surprises and the best team simply wins.

        # first stage to avoid over complicating the code would be to determine the game events based on these simple scores.
        # for example, if a team wins 11 - 3, the game events could be minute 5, away team penalty, 42 mins, home team try and conv etc.
        # stage two would be to introduce event variety: example: 58 mins, away team misses penalty. 73 mins home team try disallowed etc.
        # stage 3 would be to introduce event surprises based on player attributes. also bans, injuries.
        # stage 4 would be to modify the original score based on pre-defined game surprises and random events.
        # random events could be sudden drop in form, sudden increase in form.

  # team points update
        home_team_stats = club_dict[home_team]['stats']
        away_team_stats = club_dict[away_team]['stats']
        # increase one gmae played for both teams
        home_team_stats['played'] += 1
        away_team_stats['played'] += 1

        if home_score > away_score:

            point_diff = home_score-away_score

            home_team_stats['won'] += 1
            home_team_stats['Pts'] += 4
            home_team_stats['+/-'] += point_diff
            away_team_stats['+/-'] -= point_diff
            away_team_stats['lost'] += 1

            # increase home team form for win

            for player_data in home_team_data['players'].values():
                p_form = player_data['form']
                p_form += 0.2
                p_form = round(p_form, 1)
                player_data['form'] = p_form
                if player_data['form'] > 9.5:
                    player_data['form'] = 9.5
                if player_data['form'] > 8.4 and player_data['skill'] < 90:
                    player_data['info'] = form_txt
                else:
                    player_data['info'] = ""
                if player_data['form'] > 9.5:
                    player_data['form'] = 9.5
                elif player_data['form'] < 3.0:
                    player_data['form'] = 3.0

            if point_diff >= 20:

                for player_data in home_team_data['players'].values():
                    p_form = player_data['form']
                    p_form += 0.2
                    p_form = round(p_form, 1)
                    player_data['form'] = p_form
                    if player_data['form'] > 9.5:
                        player_data['form'] = 9.5
                    if player_data['form'] > 8.4 and player_data['skill'] < 90:
                        player_data['info'] = form_txt
                    else:
                        player_data['info'] = ""
                    if player_data['form'] > 9.5:
                        player_data['form'] = 9.5
                    elif player_data['form'] < 3.0:
                        player_data['form'] = 3.0

        elif home_score < away_score:

            point_diff = away_score-home_score

            away_team_stats['won'] += 1
            away_team_stats['Pts'] += 4
            away_team_stats['+/-'] += point_diff
            home_team_stats['+/-'] -= point_diff
            home_team_stats['lost'] += 1

            # increase away_fh team form for win

            for player_data in away_team_data['players'].values():
                p_form = player_data['form']
                p_form += 0.2
                p_form = round(p_form, 1)
                player_data['form'] = p_form
                if player_data['form'] > 9.5:
                    player_data['form'] = 9.5

                if player_data['form'] > 8.4 and player_data['skill'] < 90:
                    player_data['info'] = form_txt
                else:
                    player_data['info'] = ""
                if player_data['form'] > 9.5:
                    player_data['form'] = 9.5
                elif player_data['form'] < 3.0:
                    player_data['form'] = 3.0

            if point_diff >= 20:
                for player_data in away_team_data['players'].values():
                    p_form = player_data['form']
                    p_form += 0.2
                    p_form = round(p_form, 1)
                    player_data['form'] = p_form
                    if player_data['form'] > 9.5:
                        player_data['form'] = 9.5
                    if player_data['form'] > 8.4 and player_data['skill'] < 90:
                        player_data['info'] = form_txt
                    else:
                        player_data['info'] = ""
                    if player_data['form'] > 9.5:
                        player_data['form'] = 9.5
                    elif player_data['form'] < 3.0:
                        player_data['form'] = 3.0

        else:
            home_team_stats['draw'] += 1
            away_team_stats['draw'] += 1
            home_team_stats['Pts'] += 1
            away_team_stats['Pts'] += 1

        home.append(home_score)
        away.append(away_score)

        # random up or dip in form home

        random_form = random.choices(player_id_nums, k=30)
        for player_id in club_dict[home_team]['players']:
            adjust = random.randint(-3, 3)
            adjust = round(adjust, 1)
            if player_id in random_form:
                club_dict[home_team]['players'][player_id]['form'] += adjust
                if club_dict[home_team]['players'][player_id]['form'] > 8.4 and club_dict[home_team]['players'][player_id]['skill'] < 90:
                    club_dict[home_team]['players'][player_id]['info'] = form_txt
                else:
                    club_dict[home_team]['players'][player_id]['info'] = ""
                if club_dict[home_team]['players'][player_id]['form'] > 9.5:
                    club_dict[home_team]['players'][player_id]['form'] = 9.5
                elif club_dict[home_team]['players'][player_id]['form'] < 3.0:
                    club_dict[home_team]['players'][player_id]['form'] = 3.0

      # random up or dip in form away
        random_form = random.choices(player_id_nums, k=30)
        for player_id in club_dict[away_team]['players']:
            adjust = random.randint(-3, 3)
            adjust = round(adjust, 1)
            if player_id in random_form:
                club_dict[away_team]['players'][player_id]['form'] += adjust
                if club_dict[away_team]['players'][player_id]['form'] > 8.4 and club_dict[away_team]['players'][player_id]['skill'] < 90:
                    club_dict[away_team]['players'][player_id]['info'] = form_txt
                else:
                    club_dict[away_team]['players'][player_id]['info'] = ""
                if club_dict[away_team]['players'][player_id]['form'] > 9.5:
                    club_dict[away_team]['players'][player_id]['form'] = 9.5
                elif club_dict[away_team]['players'][player_id]['form'] < 3.0:
                    club_dict[away_team]['players'][player_id]['form'] = 3.0

        # print(home_scorers)
        # print(away_scorers)

        # reward scorers with skill points (then reset game pts)

        for player_data in home_team_data['players'].values():
            p_skill = player_data['skill']
            p_points = player_data['game pts']
            p_id = player_data['player_id']
            if player_data['game pts'] > 0:
                player_data['skill'] += 1
            if player_data['game pts'] > 3:
                player_data['skill'] += 1
            if player_data['game pts'] > 5:
                player_data['skill'] += 1
            if player_data['game pts'] > 10:
                player_data['skill'] += 1
            if player_data['skill'] > 89:
                player_data['info'] = "*Star Player*"
            if player_data['skill'] > 95:
                player_data['skill'] = 95
            player_data['game pts'] = 0

        #  random skill up or down
        # Choose a random player from the team

        num = random.randint(0, 5)

        for i in range(num):

            adjust = random.randint(-1, 1)

            # Get the players of the specified team
            team_players = club_dict[home_team]['players']

            random_player_id = random.choice(list(team_players.keys()))
            random_player = team_players[random_player_id]

            # Adjust the value of the random player
            # print('old skill',random_player['skill'])
            new_value = random_player['skill'] + \
                adjust  # Modify the value as needed
            random_player['skill'] = new_value
            # print('new skill',random_player['skill'])

            # Print the updated player information

            # Update the player in the club_dict
            club_dict[home_team]['players'][random_player_id] = random_player

        for i in range(num):

            adjust = random.randint(-1, 1)

            # Get the players of the specified team
            team_players = club_dict[away_team]['players']

            random_player_id = random.choice(list(team_players.keys()))
            random_player = team_players[random_player_id]

            # Adjust the value of the random player
            # print('old skill',random_player['skill'])
            new_value = random_player['skill'] + \
                adjust  # Modify the value as needed
            random_player['skill'] = new_value
            # print('new skill',random_player['skill'])

            # Print the updated player information

            # Update the player in the club_dict
            club_dict[home_team]['players'][random_player_id] = random_player

        # need to adjust info if affected by skill change

 # print round results and league print
    print_round_results(round_num)

    # print league table
    league_print()
    home.clear()
    away.clear()

    for d in pos_dict_list:
        pos_inj_count(d)

    for t in club_dict:
        club_inj_count(t)

    # return "future" message for news screen function based on match result
    week += 1

 # game end


def league_print_winner():
    # Create a PrettyTable instance
    table = PrettyTable()

    # Define table columns
    table.field_names = ["", "Team Name", "Played",
                         "Won", "Draw", "Lost", "+/-", "BP", "Pts"]

    # Sort club dictionary by 'Pts' and '+/-' in descending order
    sorted_club_dict = sorted(club_dict.items(), key=lambda x: (
        x[1]['stats']['Pts'], x[1]['stats']['+/-']), reverse=True)

    # Iterate over the sorted club dictionary
    for rank, (club_name, club_data) in enumerate(sorted_club_dict, start=1):
        stats = club_data["stats"]
        played = stats["played"]
        won = stats["won"]
        draw = stats["draw"]
        lost = stats["lost"]
        plus_minus = stats["+/-"]
        bp = stats["BP"]
        pts = stats["Pts"]

        # Add a row to the table
        table.add_row([rank, club_name.ljust(20), played,
                      won, draw, lost, plus_minus, bp, pts])

        # Check if it's the first team (top of the league)
        if rank == 1:
            top_team = club_name

    table.title = "HighBet Rugby Union League North-West"

    # Print the table
    # print(table)

    # Print the top team
    # print("Top team: ", top_team)
    print(f"End of season. winner is {top_team}")


league_print_winner()


quit()

# print(club_dict[team]['players'])
