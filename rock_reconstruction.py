# Place the images correctly to create a mosaic.


# Parse csv into geojson file including attributes: yaw, pitch, roll, x, y, z, and image location

# Create model with image objects
# Seed database with each image object

# Write function to geo-reference images
  # put images into matrix based on x.y values
  # find max long, min long, max lat, min lat

class Image:
  def _init_(self, lat, long, alt, yaw, pitch, roll)
      self.lat = lat
      self.long = long
      self.alt = alt
      self.yaw = yaw
      self.pitch = pitch
      self.roll = roll

if _name_ == "_main_":
  image = Image._init_(self, 38.426165, 123.113115, 90.604094, 187.491139, ­0.312975, 2.836182)












