import csv
from email import header
import pandas as pd

data = []
no_of_ghosts = []
agent1 = []
agent2 = []
agent3 = []
agent4 = []
agent5 = []

i = 1
with open("./Ghosts_invisible_in_walls/output_agent4_invisible.txt","r") as o:
    lines = o.readlines()
for j in range(3,300,5):
    no_of_ghosts.append(i)
    agent4.append(lines[j][19:])
    i = i + 5
for k in range(0,len(agent4)):
    agent4[k] = agent4[k][1:-1]

with open("output_agent1.txt","r") as o:
    lines = o.readlines()
for j in range(3,300,5):
    agent1.append(lines[j][19:])
for k in range(0,len(agent1)):
    agent1[k] = agent1[k][1:-1]

with open("output_agent2.txt","r") as o:
    lines = o.readlines()
for j in range(3,300,5):
    agent2.append(lines[j][19:])
for k in range(0,len(agent2)):
    agent2[k] = agent2[k][1:-1]

with open("./Ghosts_invisible_in_walls/output_agent5.txt","r") as o:
    lines = o.readlines()
for j in range(3,300,5):
    agent5.append(lines[j][19:])
for k in range(0,len(agent5)):
    agent5[k] = agent5[k][1:-1]

data.append(no_of_ghosts)
data.append(agent1)
data.append(agent2)
data.append(agent4)
data.append(agent5)
# print(data)

df = pd.DataFrame(data).transpose().to_csv("Ghosts_invisible_in_walls/Ghosts_invisible_results.csv",header=["No of Ghosts","Agent 1","Agent 2","Agent 4","Agent 5"],index=None)
