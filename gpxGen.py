import xml.etree.ElementTree as ET
import datetime
from datetime import timedelta
from decimal import *
getcontext().prec = 9

default_lon = '-84.0704070'
mile_lat_increment = Decimal(.0145000)
default_startTime = datetime.datetime.now()

def create_trkpt ( trkseg, lat, lon, ele, time ):
    trkpt = ET.SubElement(trkseg, "trkpt")
    trkpt.set('lat', str(lat))
    trkpt.set('lon', lon)
    trkpt_ele = ET.SubElement(trkpt, 'ele')
    trkpt_ele.text = ele
    trkpt_time = ET.SubElement(trkpt, 'time')
    trkpt_time.text = time
    return

def create_duration ( startTime, startLat, startLon, seconds, paceSeconds, grade ):
    latPerSecond = mile_lat_increment / paceSeconds
    currentTime = startTime
    currentLat = startLat
    for second in range(seconds):
        currentTime = currentTime + timedelta(seconds=1)
        currentLat = currentLat + latPerSecond
        #calculate elevation based on grade
        print currentTime.strftime("%Y-%m-%dT%H:%M:%SZ")
        print currentLat
        if second % 5 == 0:
            create_trkpt(trkseg, currentLat, startLon, '0.0', currentTime.strftime("%Y-%m-%dT%H:%M:%SZ"))
    return

root = ET.Element('gpx')
root.set('creator', "Garmin Edge 500")
root.set('version', "1.1")
root.set('xmlns', "http://www.topografix.com/GPX/1/1")
root.set('xmlns:xsi', "http://www.w3.org/2001/XMLSchema-instance")
root.set('xsi:schemaLocation', "http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd http://www.garmin.com/xmlschemas/GpxExtensions/v3 http://www.garmin.com/xmlschemas/GpxExtensionsv3.xsd http://www.garmin.com/xmlschemas/TrackPointExtension/v1 http://www.garmin.com/xmlschemas/TrackPointExtensionv1.xsd http://www.garmin.com/xmlschemas/GpxExtensions/v3 http://www.garmin.com/xmlschemas/GpxExtensionsv3.xsd http://www.garmin.com/xmlschemas/TrackPointExtension/v1 http://www.garmin.com/xmlschemas/TrackPointExtensionv1.xsd")

metadata = ET.SubElement(root, 'metadata')
time = ET.SubElement(metadata, 'time')
time.text = default_startTime.strftime("%Y-%m-%dT%H:%M:%SZ")

trk = ET.SubElement(root, 'trk')
trkseg = ET.SubElement(trk, 'trkseg')

create_duration(default_startTime, Decimal(35.0000000), default_lon, 600, 480, 0)
#create_trkpt(trkseg, '35.0000000', default_lon, '0.0', '2016-01-07T15:00:00Z')
#create_trkpt(trkseg, '35.0145000', default_lon, '0.0', '2016-01-07T15:08:00Z')
#create_trkpt(trkseg, '35.0290000', default_lon, '80.4672', '2016-01-07T15:17:00Z')
#create_trkpt(trkseg, '35.0435000', default_lon, '160.9344', '2016-01-07T15:26:00Z')
#create_trkpt(trkseg, '35.0580000', default_lon, '241.4016', '2016-01-07T15:35:00Z')
#create_trkpt(trkseg, '35.0725000', default_lon, '321.8688', '2016-01-07T15:44:00Z')

tree = ET.ElementTree(root)
#ET.dump(root)
tree.write("updated.gpx", encoding="UTF-8", xml_declaration=True, default_namespace=None, method="xml")