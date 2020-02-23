import numpy as np
import matplotlib.pyplot as plt

def retrieveInformation(teamname):
    informationAsList = []
    if (teamname == "Kings Guard Gaming"):
        return [372,164,91,192,168]
    else:
        return [429,135,117,192,164]
    return informationAsList

def drawChart(info, enemyTeamName):
    barWidth = 0.25

 
    # set height of bar
    team1 = info[0]
    team2 = info[1]
 
    # Set position of bar on X axis
    r1 = np.arange(len(team1))
    r2 = [x + barWidth for x in r1]
 
    # Make the plot
    plt.bar(r1, team1, color='#7f6d5f', width=barWidth, edgecolor='white', label="Kings Guard Gaming")
    plt.bar(r2, team2, color='#557f2d', width=barWidth, edgecolor='white', label=enemyTeamName)
 
    # Add xticks on the middle of the group bars
    plt.xlabel('group', fontweight='bold')
    plt.xticks([r + barWidth for r in range(len(team1))], ['2-pointers', '3-pointers', 'Offensive Rebounds', 'Defensive Rebounds', 'Turnovers'])
    plt.legend()
    plt.savefig('./Webpage/WebContent/resources/offensive-'+enemyTeamName+'-bar.png')
    return
enemy = "Blazer5 Gaming"
data = [retrieveInformation("Kings Guard Gaming"),retrieveInformation(enemy)]
drawChart(data,enemy)
