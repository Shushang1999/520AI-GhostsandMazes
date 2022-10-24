import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
x = []
y = []

for line in open("plotGraph.txt","r"):
    result = line.split()
    x.append(result[0])
    y.append(result[1])

agent1 = pd.DataFrame({"No of Ghosts":x,"Survivability":y})
# agent1.to_csv("result.csv")

sns.lineplot(x = "Survivability", y = "No of Ghosts",data=agent1)
plt.show()