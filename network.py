import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd




#alph = string.ascii_uppercase
#for i in alph:
#    G.add_node(i)


dfNames = pd.read_csv('../cs230_project/names230.csv')
dfHelp = pd.read_csv('../cs230_project/help.csv')
dfOutside = pd.read_csv('../cs230_project/outside.csv')

name = input("Enter First and Last Name: \n")

##Names
nameRow_Names = dfNames[dfNames["Name:"] == name]
nameRow_Names = nameRow_Names.drop(columns="Name:")

#Help
nameRow_Help = dfHelp[dfHelp["Name:"] == name]
nameRow_Help = nameRow_Help.drop(columns="Name:")

##Outside
nameRow_Outside = dfOutside[dfOutside["Name:"] == name]
nameRow_Outside = nameRow_Outside.drop(columns="Name:")



# Reset index to get the row as a Series
#Names
nameRow_Names = nameRow_Names.reset_index(drop=True).iloc[0]
linksNames = nameRow_Names[nameRow_Names == 1.0].index.tolist()

#Help
nameRow_Help = nameRow_Help.reset_index(drop=True).iloc[0]
linksHelp = nameRow_Help[nameRow_Help == 1.0].index.tolist()

#Outside
nameRow_Outside = nameRow_Outside.reset_index(drop=True).iloc[0]
linksOutside = nameRow_Outside[nameRow_Outside == 1.0].index.tolist()



#Assigning weight
allNames = linksNames + linksOutside + linksHelp

weightsDict = {}

###***
#Runs through lists, adding 1 for each occurance
for n in allNames:
    if n in weightsDict:
        weightsDict[n] += 1
    else:
        weightsDict[n] = 1
            
            


#Drawing
G=nx.Graph()
#Gets all names
names = dfNames["Name:"].tolist()

G.add_nodes_from(names)

for i in weightsDict:
    G.add_edge(name, i, weight = weightsDict[i])
    
#dict for edge weights
edgeLabels = nx.get_edge_attributes(G, "weight")

pos= nx.circular_layout(G)


plt.figure(figsize=(30, 30))
nx.draw(G,pos=pos,
        with_labels=True,
        node_color="red",
        node_size=8000,
        font_color="black",
        font_size=20,
        font_family="Times New Roman",
        font_weight="bold",
        width=5,
        )

nx.draw_networkx_edge_labels(G, 
                             pos=pos, 
                             edge_labels=edgeLabels,
                             font_color="red",
                             font_size=12,
                             font_weight="bold"
                             )

plt.margins(0.02)
plt.show()






















