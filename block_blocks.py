def edge_in_block(hydrant1, hydrant2):
    return hydrant1.blockID == hydrant2.blockID

def blocked_by_block(hydrant1, hydrant2):
    if edge_in_block(hydrant1, hydrant2):
        for roadID in hydrant1.road_ID:
           if roadID in hydrant2.road_ID:
                return False  
        return True
    else:
        return False
