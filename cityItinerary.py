from cityDatabase import Session
from citySchemas import Attraction
from cityUtils import AttractionTemp
import os

def getAttractions(location):
    '''
    Get the top 10 attractions from ChatGPT

    Parameters:
    location (str): the name of a city

    Returns:
    str:Recommendations of attractions in a specific location
    '''
    recommendations = "Fenway Park, Freedom Trail, Boston Common, New England Aquarium, Museum of Fine Arts, Harvard University, Boston Tea Party Ships & Museum, Isabella Stewart Gardner Museum, Samuel Adams Brewery, USS Constitution Museum"
    return recommendations

def createAttraction(attraction, location, attraction_information = None, latitude = None, longitude = None):
    '''
    Create Attraction Object

    Parameters:
    attraction (str): attraction name
    location (str): city name
    attraction_information (str): description about the attraction and its offerings
    latitude (int): latitude of the attraction
    longitude (int): longitude of the attraction

    Returns:
    AttractionTemp: Attraction temporary object to be placed into the database
    '''
    return AttractionTemp(attraction, location, attraction_information, latitude, longitude)

def cleanName(name):
    '''
    Clean name to have no whitespace

    Parameters:
    name (str || other): name to be inserted in the database

    Returns:
    str: removes the whitespace from name to return
    other: the same object
    '''
    if type(name) is str:
        return name.strip()
    return name
    

def insertAttraction(attraction:AttractionTemp, sess):
    '''
    Insert a attraction object into the database

    Parameters:
    attraction (AttractionTemp): attraction object to be inserted in the database
    sess (Session): database session to commit with
    '''
    attractionRow = Attraction(cleanName(attraction.attraction_name), cleanName(attraction.attraction_information), attraction.latitude, attraction.longitude, cleanName(attraction.location))
    sess.add(attractionRow)
    sess.commit()
    print("Added attraction: ", cleanName(attraction.attraction_name))

def saveAttractions(location):
    '''
    Get and save attractions of a specific location into the database

    Parameters:
    location (str): city name

    Returns:
    str:Recommendations of attractions in a specific location.
    '''
    recommendations = getAttractions(location)
    
    sess = Session()
    for attraction in recommendations.split(","):
        attraction_object = createAttraction(attraction, location, attraction_information = None, latitude = None, longitude = None)
        insertAttraction(attraction_object, sess)
    sess.close()
    
    return recommendations

if __name__=="__main__":
    location = "Boston, MA"
    saveAttractions(location)