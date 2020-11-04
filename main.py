import ast
import copy
from tkinter import *
from PyQt5 import QtWidgets, QtWebEngineWidgets
import folium
import folium.plugins as plugins
import numpy as np
import io
import sys

file = open('vertexInfo.txt', 'r')
contents = file.read()
vertexInfo = ast.literal_eval(contents)
file.close()
print(type(vertexInfo))
print(vertexInfo)

file = open('calInfo.txt', 'r')
contents = file.read()
calInfo = ast.literal_eval(contents)
file.close()
print(type(calInfo))
print(calInfo)


def map(root):
    app = QtWidgets.QApplication(sys.argv)
    m = folium.Map(
        location=[37.4500597, 127.1276783], zoom_start=17
    )

    folium.Marker(location=[37.4500597, 127.1276783], popup='가천대 정문', tooltip="가천대 정문").add_to(m)
    folium.Marker(location=[37.4503, 127.1276783], popup='가천대 정문', tooltip="가천대 정문").add_to(m)
    folium.Marker(location=[37.4507, 127.1276783], popup='가천대 정문', tooltip="가천대 정문").add_to(m)
    m.add_child(folium.LatLngPopup())

    size = 100
    lons = np.random.randint(-180, 180, size=size)
    lats = np.random.randint(-90, 90, size=size)
    # plugins.FastMarkerCluster(data=list(zip(lats, lons)), callback=callback).add_to(m)

    locations = list(zip(lats, lons))

    data = io.BytesIO()
    m.save(data, close_file=False)

    w = QtWebEngineWidgets.QWebEngineView()
    w.setHtml(data.getvalue().decode())
    w.resize(3000, 1080)
    w.show()

    sys.exit(app.exec_())


def findPath(text, root, a, b):
    # 출발지 도착지를 설정해준다
    departure = a.get()
    destination = b.get()
    print("-----------[", departure, "->", destination, "]----------")

    routing = {}
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

    cursor = 0

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
        print("[" + toVisit + "]")
        print("Dist :", minDist)

    # print("\n", "[", departure, "->", destination, "]")
    # print("Route : ", routing[destination]['route'])
    # print("ShortestDistance : ", routing[destination]['shortestDist'])
    Route = (routing[destination]['route'])
    Route.append(destination)
    ShortestDistance = routing[destination]['shortestDist']
    text.insert(2.0, "[" + departure + "->" + destination + "]" + "\n")
    text.insert(3.0, "Route : " + str(Route) + '\n')
    text.insert(4.0, "ShortestDistance : " + str(ShortestDistance) + '\n')
    text.pack()
    btn2 = Button(root, width=10, text="지도보기",
                  command=lambda: map(root))
    btn2.pack()


root = Tk()
root.title("길찾기")
root.geometry("250x350+360+170")
root.resizable(True, True)
root.configure(background='#A2B5CD')
t1 = Label(root, text="출발지")
t1.pack()
entry1 = Entry(root, width=10)
entry1.pack()
t2 = Label(root, text="출발지")
t2.pack()
entry2 = Entry(root, width=10)
entry2.pack()
textbox = Entry(root, width=20, textvariable=str)

btn1 = Button(root, width=10, text="공개키 만들기",
              command=lambda: findPath(textbox, root, entry1, entry2))  # 위젯들을 파라미터로 넘겨주어 외부 함수에서 entry 값을 받아올 수 있도록 하였다
btn1.pack()
btn2 = Button(root, width=10, text="지도",
              command=lambda: map( root))  # 위젯들을 파라미터로 넘겨주어 외부 함수에서 entry 값을 받아올 수 있도록 하였다
btn2.pack()
textbox = Text(root)
textbox.insert(CURRENT, "결과: " + "\n")
mainloop()


