import geopandas as gpd

from shapely.geometry import Point, Polygon

def blockInfo(shapefile):
    gdf = gpd.read_file(shapefile)
    block_info_list = []
    for idx, row in gdf.iterrows():
        block_id = row['id'] 
        polygon = row['geometry'] 
        corners = list(polygon.exterior.coords)
        block_info = {
            'blockID': block_id,
            'corners': corners
        }
        block_info_list.append(block_info)
    return block_info_list

def blockIdentify(hydrantCenter, blocks):
    hydrantPoint = Point(hydrantCenter)
    for block in blocks:
        blockCoords = block['corners'] 
        blockPolygon = Polygon(blockCoords)
        if hydrantPoint.within(blockPolygon):
            hydrantBlockID = block['blockID'] 
            return hydrantBlockID
    return None

blocks = blockInfo("1920s_blocks_complete.shp")
hydrants = gpd.read_file("hydrant_location.shp")
hydrants['id'] = hydrants.reset_index().index
hydrants['block'] = hydrants.apply(lambda row: blockIdentify(row['geometry'], blocks), axis=1)
print(hydrants)
