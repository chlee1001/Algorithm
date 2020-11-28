import ast
import copy
from tkinter import *
from PyQt5 import QtWidgets, QtWebEngineWidgets
import folium
import folium.plugins as plugins
import io
import sys
import time

# ### File Load ### #
file = open('./statics/vertexInfo.txt', 'r')
contents = file.read()
vertexInfo = ast.literal_eval(contents)
file.close()
file = open('./statics/calInfo.txt', 'r')
contents = file.read()
calInfo = ast.literal_eval(contents)
file.close()
file = open('./statics/keyword.txt', 'r')
contents = file.read()
name2Keyword = ast.literal_eval(contents)
file.close()
file = open('./statics/pathCoordinate.txt', 'r')
contents = file.read()
pathCoord = ast.literal_eval(contents)
file.close()

routeName = []

now = time.localtime()
timeSet = []
timeTemp = 0

for i in range(20):
    year = now.tm_year
    month = now.tm_mon
    mday = now.tm_mday
    hour = now.tm_hour
    min = now.tm_min + timeTemp
    if min >= 60:
        hour += 1
        min -= 60
    elif hour >= 60:
        mday += 1
        hour -= 60
    elif mday >= 30:
        month += 1
        mday -= 29
    elif month > 12:
        year += 1
        month -= 11
    timeSet.append("%04d-%02d-%02dT%02d:%02d:%02d" % (year, month, mday, hour, min, now.tm_sec))
    timeTemp += 7


def showMap():
    app = QtWidgets.QApplication(sys.argv)
    # print(len(routeName))

    colors = ['red', 'blue', 'green', 'black']

    lines = []

    timePos = 0
    if len(routeName) == 2:
        coordName = pathCoord[routeName[0] + ' -> ' + routeName[1]]
        # print(len(coordName))
        for j in range(len(coordName)):
            lines.append(
                {'coordinates': coordName[j], 'dates': [timeSet[timePos], timeSet[timePos + 1]], 'color': colors[j]})
            timePos += 1
    else:
        coordName = []
        for i in range((len(routeName) - 1)):
            coordName.append(pathCoord[routeName[i] + ' -> ' + routeName[i + 1]])

        for j in range(len(coordName)):
            for k in range(len(coordName[j])):
                lines.append(
                    {'coordinates': coordName[j][k], 'dates': [timeSet[timePos], timeSet[timePos + 1]],
                     'color': colors[k]})
                timePos += 1

    # print(lines)
    features = [{'type': 'Feature', 'geometry': {'type': 'LineString', 'coordinates': line['coordinates'], },
                 'properties': {'times': line['dates'],
                                'style': {'color': line['color'], 'weight': line['weight'] if 'weight' in line else 5}
                                }
                 } for line in lines]

    m = folium.Map(
        location=[37.4500597, 127.1276783], tiles="OpenStreetMap", zoom_start=17)

    plugins.TimestampedGeoJson({'type': 'FeatureCollection', 'features': features, }, period='PT1M',
                               add_last_point=True).add_to(m)

    data = io.BytesIO()
    m.save(data, close_file=False)

    w = QtWebEngineWidgets.QWebEngineView()
    w.setHtml(data.getvalue().decode())
    w.resize(1280, 720)
    w.show()
    sys.exit(app.exec_())


###########################################################################
# Find the shortest distance from the entered starting point to destination
###########################################################################
def findPath(startP, endP):
    # Input starting point and destination
    departureName = startP.get()
    destinationName = endP.get()

    departure = name2Keyword[departureName]
    destination = name2Keyword[destinationName]

    print("-----------[", departureName, "->", destinationName, "]----------")

    # Save 'shortestDist=shortest distance', 'route=shortest path' in routing dictionary
    routing = {}
    for place in calInfo.keys():  # Make a table showing all the buildings on the map and the shortest distance to each building.
        routing[place] = {'shortestDist': 0, 'route': [], 'visited': 0}

    def visitPlace(visit):
        routing[visit]['visited'] = 1
        for toGo, betweenDist in calInfo[visit].items():
            toDist = routing[visit]['shortestDist'] + betweenDist
            if (routing[toGo]['shortestDist'] >= toDist) or not routing[toGo]['route']:
                routing[toGo]['shortestDist'] = toDist
                routing[toGo]['route'] = copy.deepcopy(routing[visit]['route'])
                routing[toGo]['route'].append(visit)

    """
    Write down the shortest distance to the buildings
    where the starting point and the destination are directly connected by the road as indicated on the map,
    and leave the other buildings blank. Here, the blank value means infinity.
    """
    visitPlace(departure)

    while 1:
        # Visited buildings from the shortest to the longest, and visited buildings are displayed.
        minDist = max(routing.values(), key=lambda x: x['shortestDist'])['shortestDist']
        toVisit = ''
        for name, search in routing.items():
            if 0 < search['shortestDist'] <= minDist and not search['visited']:
                minDist = search['shortestDist']
                toVisit = name
        # Repeat the process up and down until you have visited all the buildings on the graph.
        if toVisit == '':
            break

        """
        When you visit a new building, the distance between that building and the subsequent buildings is changed.
        However, if the shortest distance has already been obtained before,
        compare the distances with each other and change or maintain the smaller ones.
        """
        visitPlace(toVisit)
        print("[" + vertexInfo[toVisit][0] + "] 까지의 최단거리: 약" + str(minDist) + "m")

    # Arragement route
    Route = (routing[destination]['route'])
    Route.append(destination)

    routeName.clear()  # Prevent path stacking in the list when user click find a way consecutively
    for i in range(len(Route)):  # Translate 'A' --> '가천관'
        routeName.append(vertexInfo[Route[i]][0])

    ShortestDistance = routing[destination]['shortestDist']
    testResult = "[" + departureName + " -> " + destinationName + "]" + "\n\n\n" + "경로 : " + str(
        routeName) + '\n\n' + "최단 거리 : " + "약 " + str(ShortestDistance) + 'm\n'
    label['text'] = testResult

    # Generate map buttons after outputting results
    btn_map = Button(root, text="지도",
                     command=lambda: showMap())
    btn_map.place(relx=0.89, rely=0.9, relwidth=0.1, relheight=0.08)


##########################################
# # Implement GUI through python thinker
##########################################
Height = 363
Width = 600

root = Tk()
root.title("가천 길 찾기")
# root.geometry("440x450")
root.resizable(True, True)

canvas = Canvas(root, height=Height, width=Width)
canvas.pack()

background_image = PhotoImage(file='./statics/gachonUniv.png')
background_label = Label(root, image=background_image)

background_label.place(x=0, y=0, relwidth=1, relheight=1)

frameDeparture = Frame(root, bg='#80c1ff', bd=5)
frameDeparture.place(relx=0.2, rely=0.15, relwidth=0.3, relheight=0.1, anchor='n')
departureLabel = Label(frameDeparture, text="출발지", width=30)
departureLabel.place(relwidth=0.3, relheight=1)
departureInput = Entry(frameDeparture, font=5)
departureInput.place(relx=0.35, relwidth=0.65, relheight=1)

frameDestination = Frame(root, bg='#80c1ff', bd=5)
frameDestination.place(relx=0.55, rely=0.15, relwidth=0.3, relheight=0.1, anchor='n')
destinationLabel = Label(frameDestination, text="목적지", width=30)
destinationLabel.place(relwidth=0.3, relheight=1)
destinationInput = Entry(frameDestination, font=5)
destinationInput.place(relx=0.35, relwidth=0.65, relheight=1)

button = Button(root, text="최단거리 찾기",
                command=lambda: findPath(departureInput,
                                         destinationInput))
button.place(relx=0.75, rely=0.155, relwidth=0.18, relheight=0.08)

frameText = Frame(root, bg='#80c1ff', bd=10)
frameText.place(relx=0.5, rely=0.28, relwidth=0.75, relheight=0.6, anchor='n')

label = Label(frameText, font=("휴먼매직체", 16), wraplength=400)
label.place(relwidth=1, relheight=1)

root.mainloop()
