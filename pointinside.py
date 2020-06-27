import numpy as np
from shapely.geometry import Polygon, Point

poly = Polygon([int(input()),int(input()) for i in range(int(input()))])

minx, miny, maxx, maxy = poly.bounds 

longs = np.arange(minx, maxx, 2); lats = np.arange(miny, maxy, 2)      
longs = np.tile(longs,3).ravel(); lats = np.repeat(lats,3).ravel()
coords = np.array([(x,y) for x,y in zip(longs,lats)])

points = [Point(xy) for xy in coords]

check = [xy.within(poly) for xy in points]
pointsInside = coords[check]

ranIdx = np.random.choice(len(pointsInside),5,replace=False)  
result = pointsInside[ranIdx]

print(result)
