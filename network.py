import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

# Load data from CSV files
dfNames = pd.read_csv('../cs230_project/data/names230.csv')
dfHelp = pd.read_csv('../cs230_project/data/help.csv')
dfOutside = pd.read_csv('../cs230_project/data/outside.csv')


name = input("Enter First and Last Name or x for entire network: ")


def oneNetwork(name):
    
    
    # Extract rows corresponding to the entered name
    nameRow_Names = dfNames[dfNames["Name:"] == name].drop(columns="Name:")
    nameRow_Help = dfHelp[dfHelp["Name:"] == name].drop(columns="Name:")
    nameRow_Outside = dfOutside[dfOutside["Name:"] == name].drop(columns="Name:")

    # Get list of connections for each category
    linksNames = nameRow_Names.reset_index(drop=True).iloc[0][nameRow_Names.iloc[0] == 1.0].index.tolist()
    linksHelp = nameRow_Help.reset_index(drop=True).iloc[0][nameRow_Help.iloc[0] == 1.0].index.tolist()
    linksOutside = nameRow_Outside.reset_index(drop=True).iloc[0][nameRow_Outside.iloc[0] == 1.0].index.tolist()


    # Combine all connections and count occurrences
    allLinks = linksNames + linksHelp + linksOutside
    weightsDict = {n: allLinks.count(n) for n in set(allLinks)}
    
    

    # Create graph and add nodes
    G = nx.Graph()
    names = dfNames["Name:"].tolist()
    G.add_nodes_from(names)




    # Add edges with weights
    for node, weight in weightsDict.items():
        G.add_edge(name, node, weight=weight)

    # Get edge labels and widths
    widths = [G[u][v]["weight"] * 4 for u, v in G.edges()]

    #Transparency #####NEEDS WORK
    transList = []
    for i in widths:
        transList.append(float(i) / 30)
        


    # Use circular layout for positioning nodes
    pos = nx.circular_layout(G)

    # Extract first names for labeling
    labels = {node: node.split()[0] for node in G.nodes()}

    
    
    #Get node sizes and covert to a list
    node_sizes = {node: G.degree(node) * 4000 + 1000 for node in G.nodes()} 
    sizes = [node_sizes[node] for node in G.nodes()]


    #Node color #### NEED WORK
    tmp_colorList = sorted(widths)
       
        


    plt.figure(figsize=(30, 30))
    nx.draw(G, pos=pos, labels=labels, with_labels=True, node_color="red", node_size=sizes, 
            font_color="black", font_size=20, font_family="Times New Roman", font_weight="bold", width=5)


    nx.draw_networkx_edges(G, pos, 
                           edgelist=G.edges(),
                           alpha= transList
                           )

    plt.margins(0.02)
    plt.show()


def wholeNetwork():
    # Create graph and add nodes
    G = nx.Graph()
    names = dfNames["Name:"].tolist()
    G.add_nodes_from(names)

    weightsDict = {}  # Define weightsDict outside the loop

    transList = []
    
    for name in names:
        # Extract rows corresponding to the entered name
        nameRow_Names = dfNames[dfNames["Name:"] == name].drop(columns="Name:")
        nameRow_Help = dfHelp[dfHelp["Name:"] == name].drop(columns="Name:")
        nameRow_Outside = dfOutside[dfOutside["Name:"] == name].drop(columns="Name:")

        # Get list of connections for each category
        linksNames = nameRow_Names.reset_index(drop=True).iloc[0][nameRow_Names.iloc[0] == 1.0].index.tolist() if not nameRow_Names.empty else []
        linksHelp = nameRow_Help.reset_index(drop=True).iloc[0][nameRow_Help.iloc[0] == 1.0].index.tolist() if not nameRow_Help.empty else []
        linksOutside = nameRow_Outside.reset_index(drop=True).iloc[0][nameRow_Outside.iloc[0] == 1.0].index.tolist() if not nameRow_Outside.empty else []

        # Combine all connections and count occurrences
        allLinks = linksNames + linksHelp + linksOutside
        weightsDict[name] = {n: allLinks.count(n) for n in set(allLinks)}
        
        
        
        


    # Add edges with weights
    for name, connections in weightsDict.items():
        for node, weight in connections.items():
            G.add_edge(name, node, weight=weight)

    # Get widths
    widths = [G[u][v]["weight"] * 4 for u, v in G.edges()]
    

    # Use circular layout for positioning nodes
    pos = nx.circular_layout(G)

    # Extract first names for labeling
    labels = {node: node.split()[0] for node in G.nodes()}

    # Get node sizes and convert to a list
    node_sizes = {node: G.degree(node) * 1000 + 500 for node in G.nodes()}
    sizes = [node_sizes[node] for node in G.nodes()]

    plt.figure(figsize=(30, 30))
    nx.draw(G, pos=pos, labels=labels, with_labels=True, node_color="red", node_size=sizes, 
            font_color="black", font_size=20, font_family="Times New Roman", font_weight="bold", width=5)


    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), width=widths)

    plt.margins(0.02)
    plt.show()




if name == "x":
    wholeNetwork()
else:
    oneNetwork(name)


