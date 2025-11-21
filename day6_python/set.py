team_A = {2,4,6,8}
team_B = {1,2,3,4}

common = team_A & team_B
print(common)

only_in_A = team_A - team_B
print(only_in_A)

player_in_at_least_one_team = team_A | team_B #It mean it is union
print(player_in_at_least_one_team)

player_who_are_not_in_both_team = (team_A - team_B) | (team_B - team_A)
print(player_who_are_not_in_both_team)