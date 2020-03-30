import pyexiv2
import pprint
filename='art01.png'
metadata = pyexiv2.ImageMetadata(filename)
metadata.read()
#userdata=json.loads(metadata['Exif.Photo.UserComment'].value)
pprint.pprint(userdata)
