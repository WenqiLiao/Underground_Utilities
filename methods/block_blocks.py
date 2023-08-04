#find the 1 closest road for each point
def find_close_road(point, roads_df):
    close_road = None
    min_distance = float('inf')
    
    for idx, road in roads_df.iterrows():
        distance = point.distance(road['geometry'])
        if distance < min_distance:
            min_distance = distance
            close_road = road
    return close_road

#apply above method to all points in df_point
df_point['close_road'] = df_point.apply(lambda row: find_close_road(row['geometry'], df_road), axis=1)

#edited hydrant class
class Hydrant:
    
    def __init__(self, id, x, y, closest_road_id, close_road): # constructor
        
        # From shapefile
        self.pointID = id
        self.x = x
        self.y = y
        self.blockID = 0
        self.roadID = closest_road_id
        self.closeRoadID = close_road
        
        # Will initialize once into network generation
        self.branchID = 0
        self.neighbor = [] # List to store all the neighbors of this hydrant
        self.edge = {} # Dict to store edge information

#two functions altered for the closest point
def edge_in_block(hydrant1, hydrant2):
    return hydrant1.blockID == hydrant2.blockID

def blocked_by_block(hydrant1, hydrant2):
    if edge_in_block(hydrant1, hydrant2):
        if hydrant1.closeRoadID == hydrant2.closeRoadID
            return False  
        return True
    else:
        return False
