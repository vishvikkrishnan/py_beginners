import http.client
import mimetypes
import xml.etree.ElementTree as ET

def fetch_from_bmkg():
    conn = http.client.HTTPSConnection("data.bmkg.go.id")
    payload = ''
    headers = {}
    conn.request("GET", "/autogempa.xml", payload, headers)
    res = conn.getresponse()
    data = res.read()
    
    root = ET.fromstring(data.decode("utf-8"))
    return root

def print_latest_earthquake():
    earthquake = fetch_from_bmkg()
    print('Time: {} {}'.format(earthquake[0][0].text, earthquake[0][1].text))
    print('Coordinates: {}'.format(earthquake[0][2][0].text))
    print('Depth: {}'.format(earthquake[0][6].text))
    print('Tsunami Warning: {}'.format(True if 'tidak' not in earthquake[0][13].text.lower() else False))
    print('Source: BMKG | Badan Meteorologi, Klimatologi, dan Geofisika https://www.bmkg.go.id/')

if __name__ == '__main__':
    print_latest_earthquake()