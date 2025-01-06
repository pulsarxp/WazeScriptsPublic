DistanceCalculator.py

A Haversine-formula

a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
c = 2 * atan2(sqrt(a), sqrt(1 - a))
distance = R * c

Magyarázat:
lat1, lat2: Az első és második pont szélessége radiánban.
dlat: A két pont szélességi különbsége.
dlon: A két pont hosszúsági különbsége.
R: A Föld sugara (Átlagosan. 6371000 méter).
distance: A két pont közötti gömbi távolság.
