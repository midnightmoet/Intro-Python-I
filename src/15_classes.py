# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE

class LatLon():
    #class LatLon (base)
    def  __init__(self, lat, lon):
      #The __init__ method is roughly what represents a constructor in Python
      #self parameter refers to the instance of the object (this kind of)
        self.lat = lat
        self.lon = lon
place = LatLon(10,20)
print(place.lon)

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLon):
  #class Waypoint that will inherit from LatLon(subclass)(child)
    def __init__(self,name, lat, lon):
      #The __init__ method is roughly what represents a constructor in Python
      #self parameter refers to the instance of the object (this kind of)
        super().__init__(lat, lon)
            #super() lets you avoid referring to the base class explicitly
        self.name = name
    def __str__(self):
          #Pythonic way to convert Python objects into strings by using __str__
        return F"{self.name}'s location is lat: {self.lat}, lon: {self.lon}"
    #f-string used above
newPlace = Waypoint("My house maybe", 40, 50)
print(newPlace.name)


# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):
    #class Geocache that will inherit from Waypoint(subclass)(child)
  def __init__(self, name, difficulty, size, lat, lon):
      #The __init__ method is roughly what represents a constructor in Python
      #self parameter refers to the instance of the object (this kind of)
    super().__init__(name, lat, lon)
    #super() lets you avoid referring to the base class explicitly
    self.difficulty = difficulty
    self.size = size

  def __str__(self):
    #Pythonic way to convert Python objects into strings by using __str__
    return F"Geocache {self.name}, diff {self.difficulty}, size {self.size}, {self.lat}, {self.lon}"
    #f-string used above
newMomsPlace = Geocache('This', 'meh', 'Large', 69, 68 )

print( newMomsPlace.difficulty)

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
waypoint = Waypoint("Catacombs", 41.70505, -121.51521)
# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocache = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)

# Print it--also make this print more nicely
print(geocache)
