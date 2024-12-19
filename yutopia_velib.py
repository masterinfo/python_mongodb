# ON importe la bibliothèque Folium et Mongo
import webbrowser

import folium
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["yutopiaDB"]
mycol = mydb["velib-tr-collection"]
Cursor = mycol.find()
tablo_stations = list(Cursor)
# On crée la map
m = folium.Map(location=[48.821270,2.311693], tiles="OpenStreetMap", zoom_start=15)
# print(tablo_stations)
i= 0
for station in tablo_stations:
    print(station)
    print(station['coordonnees_geo'])
    print(station['name'])
    print("il reste ",station['ebike'], "vélos électrique à la station ",station['name'])
    print("il reste ",station['mechanical'], "vélos mécaniques à la station ",station['name'])
    #     nb de docks dispo
    print("il reste ",station['numdocksavailable'], "docks disponibles à la station ",station['name'])

    msg1= str(station['ebike'])+ " vélos électrique"
    msg2=str(station['mechanical'])+ " vélos mécaniques"
    msg3=str(station['numdocksavailable'])+ " docks disponibles"
    msg_html = f"<div><b>{station['name']}</b><br><br>{msg1}<br><br>{msg2}<br><br>{msg3}</div>"
    folium.Marker([station['coordonnees_geo']['lat'],station['coordonnees_geo']['lon']], popup= msg_html).add_to(m)
    i += 1
    if i == 10:
        break
#
#
#



# i = 0
#
# folium.Marker([48.821270,2.311693], popup="<i>toto</i>").add_to(m)
# folium.Marker([48.821270,2.521693], popup="<b>Ttiti</b>").add_to(m)


# for item in entries:
#     if i < 100:
#         folium.Marker([item['lat'],item['lng']], popup="<i>" + item['name'] + "</i>").add_to(m)
#         i += 1
#     else:break

# On sauvegarde le fichier HTML
m.save("velib_map.html")
webbrowser.open('velib_map.html')  # open file in webbrowser

