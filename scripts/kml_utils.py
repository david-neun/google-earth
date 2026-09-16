"""KML helper utilities.

Provides parse_kml_coordinates(kml_path) which returns an Earth Engine Polygon geometry
for the first polygon found in a KML file.

This module keeps I/O and parsing in one place so notebooks/scripts can import it.
"""
from xml.etree import ElementTree as ET


def parse_kml_coordinates(kml_path):
    """Parse first <coordinates> from a KML file and return a list of [lon, lat] points.

    Note: This function only parses the first <coordinates> element. It returns a list
    of coordinate pairs suitable for constructing an ee.Geometry.Polygon.
    """
    with open(kml_path, 'r') as file:
        kml_content = file.read()
    root = ET.fromstring(kml_content)
    coordinates = []
    for elem in root.iter():
        if elem.tag.endswith('coordinates'):
            coords_text = elem.text.strip()
            coords_list = coords_text.replace('\n', ' ').split()
            for coord in coords_list:
                lon_lat = coord.split(',')[:2]
                lon, lat = map(float, lon_lat)
                coordinates.append([lon, lat])
            break
    if not coordinates:
        raise ValueError('No coordinates found in KML: %s' % kml_path)
    if coordinates[0] != coordinates[-1]:
        coordinates.append(coordinates[0])
    return coordinates
