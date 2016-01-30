import xml.etree.ElementTree as ET
import datetime
from datetime import timedelta
from decimal import *
getcontext().prec = 9

#63.411937, -18.750182 Iceland "Treadmill Winter Island"
mile_lat_increment = Decimal(.0145000)
meters_per_mile = Decimal(1609.344)
default_startTime = datetime.datetime.now()
currentTime = default_startTime
currentLat = Decimal(63.411937)
currentLon = '-18.750182'
currentEle = Decimal(0)

def create_trkpt ( trkseg, lat, lon, ele, time ):
    trkpt = ET.SubElement(trkseg, "trkpt")
    trkpt.set('lat', str(lat))
    trkpt.set('lon', lon)
    trkpt_ele = ET.SubElement(trkpt, 'ele')
    trkpt_ele.text = str(ele)
    trkpt_time = ET.SubElement(trkpt, 'time')
    trkpt_time.text = time
    return

def create_duration ( seconds, paceSeconds, grade ):
    latPerSecond = mile_lat_increment / paceSeconds
    if grade == 0:
        eleMetersPerSecond = 0
    else:
        eleMetersPerSecond = (meters_per_mile * grade) / paceSeconds
    global currentTime, currentLat, currentEle
    for second in range(seconds):
        currentTime = currentTime + timedelta(seconds=1)
        currentLat = currentLat + latPerSecond
        currentEle = currentEle + eleMetersPerSecond
        #print currentTime.strftime("%Y-%m-%dT%H:%M:%SZ")
        #print currentLat
        #print currentEle
        if second % 5 == 0:
            create_trkpt(trkseg, currentLat, currentLon, currentEle, currentTime.strftime("%Y-%m-%dT%H:%M:%SZ"))
        #just write the last trackpoint again regardless of if its a dupe, be sure not to miss up to 4 seconds on the last trackpoint
    create_trkpt(trkseg, currentLat, currentLon, currentEle, currentTime.strftime("%Y-%m-%dT%H:%M:%SZ"))
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

create_duration(495, 990, Decimal(.1))
create_duration(125, 495, Decimal(.05))
create_duration(125, 495, Decimal(.07))
create_duration(125, 495, Decimal(.09))
create_duration(125, 495, Decimal(.1))
create_duration(125, 495, Decimal(.05))
create_duration(125, 495, Decimal(.07))
create_duration(125, 495, Decimal(.09))
create_duration(125, 495, Decimal(.1))
create_duration(125, 495, Decimal(.05))
create_duration(125, 495, Decimal(.07))
create_duration(125, 495, Decimal(.09))
create_duration(125, 495, Decimal(.1))
create_duration(100, 990, Decimal(.05))
create_duration(125, 495, Decimal(.05))
create_duration(125, 495, Decimal(.07))
create_duration(125, 495, Decimal(.09))
create_duration(125, 495, Decimal(.1))
create_duration(255, 990, Decimal(.12))

tree = ET.ElementTree(root)
#ET.dump(root)
tree.write("updated.gpx", encoding="UTF-8", xml_declaration=True, default_namespace=None, method="xml")