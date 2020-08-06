with open("./Soccer Scoring/commentary.txt") as file:
    teams = file.readline().strip("\n").split(" versus ")
    
    teamScores = {}
    for team in teams:
        teamScores[team] = 0
    
    timestamps = file.read().strip("\n")
    teamScores[teams[0]] = timestamps.count(teams[0])
    teamScores[teams[1]] = timestamps.count(teams[1])
             
    if teamScores[teams[0]] > teamScores[teams[1]]:
        print(teams[0], teamScores[teams[0]])
        print(teams[1], teamScores[teams[1]])
    else:
        print(teams[1], teamScores[teams[1]])
        print(teams[0], teamScores[teams[0]])