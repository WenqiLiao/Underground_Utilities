def edge_in_block(hydrant1, hydrant2):
    return hydrant1.blockID == hydrant2.blockID

def blocked_by_block(hydrant1, hydrant2):
    if edge_in_block(hydrant1, hydrant2):
        for road_id in hydrant1.roadID:
           if road_id in hydrant2.roadID:
                return False  
        return True
    else:
        return False
