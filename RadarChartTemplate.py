import matplotlib.pyplot as plt
import pandas as pd
from math import pi

def retrieveData():
    dataAsList = []
    
    return dataAsList

def generateDataFrame():
    oreb = 76
    points = 181
    dreb = 80
    teamMinutesPlayed = 384
    minutesPlayed = 384
    teamOffensiveRebounds = 125
    sumTotalMinutes = 1920
    gamesPlayed = 16
    pointDif = 123

    offensivePossessions = 10*(oreb*(teamMinutesPlayed/5)/(minutesPlayed))
    defensivePossessions = 10*(dreb*(teamMinutesPlayed/5)/(minutesPlayed))
    

    pOffense = (points*100)/offensivePossessions
    pDefense = (pointDif*100)/defensivePossessions
    pUtility = 100*(pOffense*pDefense)/minutesPlayed/gamesPlayed/2
    pConsistency = 50*max(pOffense,pDefense)/(minutesPlayed/gamesPlayed)/2

    df = pd.DataFrame({
    'Player': ['East','North','West','South'],
    'Offense': [pOffense, 0, 0, 0],
    'Utility': [pUtility, 0, 0, 0],
    'Defense': [pDefense, 0, 0, 0],
    'Consistency': [pConsistency, 0, 0, 0]
    })
    return df

def generateDetailedDataFrame():
    listTemplate = []
    for i in range(0,10):
        listTemplate.append([])
        for j in range(0,10):
            listTemplate[i].append(10)
        listTemplate[i][i] = 90

    df = pd.DataFrame({
        'Player': ['1','2','3','4','5','6','7','8','9','10'],
        'Effective Field Goal %': listTemplate[0],
        'Free throw %': listTemplate[1],
        'Offensive Rebounds': listTemplate[2],
        'Defensive Rebounds': listTemplate[3],
        'Assists': listTemplate[4],
        'Personal Fouls': listTemplate[5],
        'Steals': listTemplate[6],
        'Turnovers': listTemplate[7],
        'Blocks': listTemplate[8],
        'True Shooting Percentage': listTemplate[9]
        })
    return df

def generateChart(data):
    # number of variable
    categories=list(data)[1:]
    N = len(categories)
     
    # We are going to plot the first line of the data frame.
    # But we need to repeat the first value to close the circular graph:
    values=data.loc[0].drop('Player').values.flatten().tolist()
    values += values[:1]
    values
     
    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]
     
    # Initialise the spider plot
    ax = plt.subplot(111, polar=True)
     
    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], categories, color='grey', size=8)
     
    # Draw ylabels
    ax.set_rlabel_position(0)
    ax.set
    plt.yticks([0,150], ["",""], color="grey", size=7)
    plt.ylim(0,150)
     
    # Plot data
    ax.plot(angles, values, linewidth=1, linestyle='solid')
     
    # Fill area
    ax.fill(angles, values, 'b', alpha=0.1)
    return plt

def generateDetailedChart(data):
    # number of variable
    categories=list(data)[1:]
    N = len(categories)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]
         
    # Initialise the spider plot
    ax = plt.subplot(111, polar=True)
         
    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], categories, color='grey', size=8)
         
    # Draw ylabels
    ax.set_rlabel_position(0)
    plt.yticks([0,100], ["",""], color="grey", size=7)
    plt.ylim(0,100)
    
    for i in range(0,len(data.index)):
        values=data.loc[i].drop('Player').values.flatten().tolist()
        values += values[:1]
         
        # Plot data
        ax.plot(angles, values, linewidth=1, linestyle='solid')
         
        # Fill area
        ax.fill(angles, values, 'b', alpha=0.1)
    legend = ax.legend(("Kings Guard Gaming","Test"),loc="best",labelspacing=0.1, fontsize='small')
    return plt

retrievedInformation = retrieveData()
data = generateDataFrame()
chart = generateChart(data)
#chart.savefig('playername_SimpleStat.png')
#plt.cla()
#plt.clf()
#data = generateDetailedDataFrame()
#chart = generateDetailedChart(data)
#chart.savefig('playername_DetailedStat.png')
chart.show()
