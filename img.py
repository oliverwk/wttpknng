import pyexiv2
import json

filename = art01.png
metadata = pyexiv2.ImageMetadata(filename)
metadata.read()
userdata={'Category':'Human',
          'Physical': {
              'skin_type':'smooth',
              'complexion':'fair'
              },
          'Location': {
              'city': 'london'
              }
          }
metadata['Exif.Photo.UserComment']=json.dumps(userdata)
metadata.write()

