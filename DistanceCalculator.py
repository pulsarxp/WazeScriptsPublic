#!/usr/bin/python

from math import sin, cos, sqrt, atan2, radians

# approximate radius of earth in km
R = 6371000.0

lat1 = radians(47.33289688880586)
lon1 = radians(19.446262121200565)
lat2 = radians(47.48008121241763)
lon2 = radians(19.201301336288456)

dlon = lon2 - lon1
dlat = lat2 - lat1

a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
c = 2 * atan2(sqrt(a), sqrt(1 - a))

unit="m"
distance = R * c
integer_part_length = len(str(int(distance)))
if(integer_part_length>3):
    distance = distance / 1000
    unit="km"

print("Distance:", round(distance, 2) ,unit )

