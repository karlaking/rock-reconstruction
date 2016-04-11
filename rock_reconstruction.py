# Place the images correctly to create a mosaic.


# Parse csv into geojson file including attributes: yaw, pitch, roll, x, y, z, and image location

# Create model with image objects
# Seed database with each image object

# Write function to geo-reference images
  # put images into matrix based on x.y values
  # find max long, min long, max lat, min lat


class Image:

  def __init__(self, lat, long, alt):
      self.lat = lat
      self.long = long
      self.alt = alt

my_first_image = Image(12,15,87)

print my_first_image







