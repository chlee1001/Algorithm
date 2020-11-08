import ast
import copy
import os
from tkinter import *
from PyQt5 import QtWidgets, QtWebEngineWidgets
import folium
import folium.plugins as plugins
import numpy as np
import io
import sys
import time

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

now = time.localtime()

timeSet = []
timeTemp = 0

for i in range(6):
    hour = now.tm_hour
    min = now.tm_min + timeTemp
    if min >= 60:
        hour += 1
        min -= 60
    timeSet.append("%04d-%02d-%02dT%02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, hour, min, now.tm_sec))
    timeTemp += 5

lines = [{'coordinates': [[127.127343, 37.450864], [127.127407, 37.450523], ],
          'dates': [timeSet[0], timeSet[1]], 'color': 'red'},
         {'coordinates': [[127.127407, 37.450523], [127.129300, 37.450067], ],
          'dates': [timeSet[2], timeSet[3]], 'color': 'blue'},
         {'coordinates': [[127.129300, 37.450067], [127.129665, 37.450391], ],
          'dates': [timeSet[4], timeSet[5]], 'color': 'green'}, ]


features = [{'type': 'Feature', 'geometry': {'type': 'LineString', 'coordinates': line['coordinates'], },
             'properties': {'times': line['dates'],
                            'style': {'color': line['color'], 'weight': line['weight'] if 'weight' in line else 5}
                            }
             } for line in lines]


def showMap():
    app = QtWidgets.QApplication(sys.argv)

    m = folium.Map(
        location=[37.4500597, 127.1276783], tiles="OpenStreetMap", zoom_start=17)

    # folium.Marker(location=[37.4500597, 127.1276783], popup='가천대 정문', tooltip="가천대 정문").add_to(m)
    # folium.Marker(location=[37.4503, 127.1276783], popup='가천대 정문', tooltip="가천대 정문").add_to(m)
    # folium.Marker(location=[37.4507, 127.1276783], popup='가천대 정문', tooltip="가천대 정문").add_to(m)
    # m.add_child(folium.LatLngPopup())

    plugins.TimestampedGeoJson({'type': 'FeatureCollection', 'features': features, }, period='PT1M',
                               add_last_point=True).add_to(m)

    data = io.BytesIO()
    m.save(data, close_file=False)

    w = QtWebEngineWidgets.QWebEngineView()
    w.setHtml(data.getvalue().decode())
    w.resize(1280, 720)
    w.show()
    sys.exit(app.exec_())


def findPath(startP, endP):
    # 출발지 도착지를 설정해준다
    departureName = startP.get()
    destinationName = endP.get()

    departure = name2Keyword[departureName]
    destination = name2Keyword[destinationName]

    print("-----------[", departureName, "->", destinationName, "]----------")

    routing = {}  # routing dictionary에 shortestDist=최단거리, route=최단경로 저장
    for place in calInfo.keys():
        routing[place] = {'shortestDist': 0, 'route': [], 'visited': 0}

    def visitPlace(visit):
        routing[visit]['visited'] = 1
        for toGo, betweenDist in calInfo[visit].items():
            toDist = routing[visit]['shortestDist'] + betweenDist
            if (routing[toGo]['shortestDist'] >= toDist) or not routing[toGo]['route']:
                routing[toGo]['shortestDist'] = toDist
                routing[toGo]['route'] = copy.deepcopy(routing[visit]['route'])
                routing[toGo]['route'].append(visit)

    visitPlace(departure)

    routeName = []

    while 1:
        minDist = max(routing.values(), key=lambda x: x['shortestDist'])['shortestDist']
        toVisit = ''
        for name, search in routing.items():
            if 0 < search['shortestDist'] <= minDist and not search['visited']:
                minDist = search['shortestDist']
                toVisit = name
        if toVisit == '':
            break

        visitPlace(toVisit)
        print("[" + vertexInfo[toVisit][0] + "] 까지의 최단거리: 약" + str(minDist) + "m")

    # 경로 정리
    Route = (routing[destination]['route'])
    Route.append(destination)
    # 'A' --> '가천관' 명칭 변경
    for i in range(len(Route)):
        routeName.append(vertexInfo[Route[i]][0])

    ShortestDistance = routing[destination]['shortestDist']
    testResult = "[" + departureName + " -> " + destinationName + "]" + "\n\n\n" + "경로 : " + str(
        routeName) + '\n\n' + "최단 거리 : " + "약 " + str(ShortestDistance) + 'm\n'
    label['text'] = testResult

    # 결과 출력 후에 지도 버튼 생성
    btn_map = Button(root, text="지도",
                     command=lambda: showMap())
    btn_map.place(relx=0.89, rely=0.9, relwidth=0.1, relheight=0.08)


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
departureInput = Entry(frameDeparture, font=40)
departureInput.place(relx=0.35, relwidth=0.65, relheight=1)

frameDestination = Frame(root, bg='#80c1ff', bd=5)
frameDestination.place(relx=0.55, rely=0.15, relwidth=0.3, relheight=0.1, anchor='n')
destinationLabel = Label(frameDestination, text="목적지", width=30)
destinationLabel.place(relwidth=0.3, relheight=1)
destinationInput = Entry(frameDestination, font=40)
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
