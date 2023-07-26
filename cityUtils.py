class AttractionTemp:
    
    def __init__(self, attraction_name, location, attraction_information = None, latitude = None, longitude = None):
        self.attraction_name = attraction_name
        self.attraction_information = attraction_information
        self.latitude = latitude
        self.longitude = longitude
        self.location = location

    def set_attraction_information(self, attraction_information):
        self.attraction_information = attraction_information
    
    def set_latitude(self, latitude):
        self.latitude = latitude

    def set_longitude(self, longitude):
        self.longitude = longitude