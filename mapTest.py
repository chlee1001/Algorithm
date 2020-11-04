import io
import sys
import folium
from PyQt5 import QtWidgets, QtWebEngineWidgets
import folium.plugins as plugins
import numpy as np

a = 1


def callback():
    a = 2
    print(a)


if __name__ == "__main__":
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
    plugins.FastMarkerCluster(data=list(zip(lats, lons)), callback=callback).add_to(m)

    locations = list(zip(lats, lons))

    data = io.BytesIO()
    m.save(data, close_file=False)

    w = QtWebEngineWidgets.QWebEngineView()
    w.setHtml(data.getvalue().decode())
    w.resize(3000, 1080)
    w.show()

    sys.exit(app.exec_())
