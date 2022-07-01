from flask import Flask

app = Flask(__name__)

import osmnx as ox
import matplotlib.pyplot as plt

place_name =  "Kamppi, Helsinki, Finland"

#Fetch OSM
#street network
graph = ox.graph_from_place(place_name, network_type = "drive")

fig, ax = ox.plot_graph(graph)

nodes, edges = ox.graph_to_gdfs(graph)
nodes.head()
edges.head()

#area
area=ox.gepcpde_to_gdf(place_name)
area.plot()

#building footprints
tags ={'building':True}
buildings = ox.geometries_from_place(place_name, tags)

len(buildings) #buildings received

buildings.head()
buildings.columns

#points of interest
tags{'amenity':'restaurant'}

restaurants = ox.geometries_from_place(place_name, tags)

len (restaurants) #numebr of restaurants

restaurants.column.values
cols = ['name', 'opening_hours', 'addr:city', 'addr:country', 'addr:housenumber', 'addr:postcode', 'addr:street']
restaurants[cols].head(10) #prints selcted 


tags = {'leisure': 'park', 'landuse': 'grass'}

parks = ox.geometries_from_place(place_name, tags)
print("Retrieved", len(parks), "objects")
parks.columns.values
parks.plot(color="green")
fig, ax = plt.subplots(figsize=(12,8))
# Plotted footprint
area.plot(ax=ax, facecolor='black')
# Plotted street edges
edges.plot(ax=ax, linewidth=1, edgecolor='dimgray')
# Plotted buildings
buildings.plot(ax=ax, facecolor='silver', alpha=0.7)
# Plotted restaurants
restaurants.plot(ax=ax, color='yellow', alpha=0.7, markersize=10)
plt.tight_layout()
# Create a subplot object for plotting the layers onto a common map
fig, ax = plt.subplots(figsize=(12,8))

# Plot the footprint
area.plot(ax=ax, facecolor='black')

# Plot the parks
parks.plot(ax=ax, facecolor="green")

# Plot street edges
edges.plot(ax=ax, linewidth=1, edgecolor='dimgray')

# Plot buildings
buildings.plot(ax=ax, facecolor='silver', alpha=0.7)

# Plot restaurants
restaurants.plot(ax=ax, color='yellow', alpha=0.7, markersize=10)
plt.tight_layout()

if __name__ == "__main__":
    app.run()