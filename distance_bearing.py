import math


#Radius of earth in metres
R = 6371e3

def distance_bearing(homeLatitude, homeLongitude, destinationLatitude, destinationLongitude):

    """
    Simple function which returns the distance and bearing between two geographic location

    Inputs:
        1.  homeLatitude            -   Latitude of home location
        2.  homeLongitude           -   Longitude of home location
        3.  destinationLatitude     -   Latitude of Destination
        4.  destinationLongitude    -   Longitude of Destination

    Outputs:
        1. [Distance, Bearing]      -   Distance (in metres) and Bearing angle (in degrees)
                                        between home and destination

    Source:
        https://github.com/TechnicalVillager/distance-bearing-calculation
    """

    rlat1   =   homeLatitude * (math.pi/180) 
    rlat2   =   destinationLatitude * (math.pi/180) 
    rlon1   =   homeLongitude * (math.pi/180) 
    rlon2   =   destinationLongitude * (math.pi/180) 
    dlat    =   (destinationLatitude - homeLatitude) * (math.pi/180)
    dlon    =   (destinationLongitude - homeLongitude) * (math.pi/180)

    # Haversine formula to find distance
    a = (math.sin(dlat/2) * math.sin(dlat/2)) + (math.cos(rlat1) * math.cos(rlat2) * (math.sin(dlon/2) * math.sin(dlon/2)))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

    # Distance in metres
    distance = R * c

    # Formula for bearing
    y = math.sin(rlon2 - rlon1) * math.cos(rlat2)
    x = math.cos(rlat1) * math.sin(rlat2) - math.sin(rlat1) * math.cos(rlat2) * math.cos(rlon2 - rlon1)
    
    # Bearing in radians
    bearing = math.atan2(y, x)
    bearingDegrees = bearing * (180/math.pi)
    out = [distance, bearingDegrees]

    return out
