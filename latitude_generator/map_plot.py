import folium
import matplotlib.pyplot as plt
import pandas as pd

def mapPlot():
    df = pd.read_csv('cordinates.csv')
    map = folium.Map(location=[10.024736517586764, 76.30792709032183],zoom_start=15)

    for p in points:
        folium.Marker(location=[p.x,p.y]).add_to(map)

    map.save('map.html')

mapPlot()
