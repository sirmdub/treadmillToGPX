import xml.etree.ElementTree as ET

default_lon = '-84.0704070'

def create_trkpt ( trkseg, lat, lon, ele, time ):
    trkpt = ET.SubElement(trkseg, "trkpt")
    trkpt.set('lat', lat)
    trkpt.set('lon', lon)
    trkpt_ele = ET.SubElement(trkpt, 'ele')
    trkpt_ele.text = ele
    trkpt_time = ET.SubElement(trkpt, 'time')
    trkpt_time.text = time
    return

root = ET.Element('gpx')
root.set('creator', "Garmin Edge 500")
root.set('xmlns', "http://www.topografix.com/GPX/1/1")
root.set('xmlns:xsi', "http://www.w3.org/2001/XMLSchema-instance")
root.set('xsi:schemaLocation', "http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd http://www.garmin.com/xmlschemas/GpxExtensions/v3 http://www.garmin.com/xmlschemas/GpxExtensionsv3.xsd http://www.garmin.com/xmlschemas/TrackPointExtension/v1 http://www.garmin.com/xmlschemas/TrackPointExtensionv1.xsd http://www.garmin.com/xmlschemas/GpxExtensions/v3 http://www.garmin.com/xmlschemas/GpxExtensionsv3.xsd http://www.garmin.com/xmlschemas/TrackPointExtension/v1 http://www.garmin.com/xmlschemas/TrackPointExtensionv1.xsd")

metadata = ET.SubElement(root, 'metadata')
time = ET.SubElement(metadata, 'time')
time.text = '2016-01-07T15:00:00Z'

trk = ET.SubElement(root, 'trk')
trkseg = ET.SubElement(trk, 'trkseg')

create_trkpt(trkseg, '35.0000000', default_lon, '0.0', '2016-01-07T15:00:00Z')
create_trkpt(trkseg, '35.0145000', default_lon, '0.0', '2016-01-07T15:08:00Z')
create_trkpt(trkseg, '35.0290000', default_lon, '80.4672', '2016-01-07T15:17:00Z')
create_trkpt(trkseg, '35.0435000', default_lon, '160.9344', '2016-01-07T15:26:00Z')
create_trkpt(trkseg, '35.0580000', default_lon, '241.4016', '2016-01-07T15:35:00Z')
create_trkpt(trkseg, '35.0725000', default_lon, '321.8688', '2016-01-07T15:44:00Z')

tree = ET.ElementTree(root)
ET.dump(root)
tree.write("updated.gpx", encoding="UTF-8", xml_declaration=True, default_namespace=None, method="xml")