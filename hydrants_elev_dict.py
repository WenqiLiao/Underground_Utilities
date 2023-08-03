#Converting elevation data for each hydrant location to a dictionary 
import geopandas as gpd
import pandas as pd 

elevation_shapefile_path = '/content/hydrant_locations_with_rasterdata.shp' #elevation data
first_hydrant_raster_gdf = gpd.read_file(elevation_shapefile_path)


second_elevation_shapefilepath = '/content/second_hydrants_with_raster.shp'
second_hydrant_raster_gdf = gpd.read_file(second_elevation_shapefilepath)

def create_hydrants_elev_dict(first_hydrant_raster_shp, second_hydrant_raster_shp): 

  hydrants_to_elev = {}

  for index, row in first_hydrant_raster_gdf.iterrows():
    hydrant_point = row['geometry']
    if pd.isna(row['SAMPLE_1']): #if the value is not in the first shapefile DEM, check second DEM file 
        corresponding_elev = second_hydrant_raster_gdf.loc[index, 'ELEV1'] #call the corresponding elevation from second DEM file 
        hydrants_to_elev[(hydrant_point.x, hydrant_point.y)] = corresponding_elev #update the dictionary value 
    else:
        hydrants_to_elev[(hydrant_point.x, hydrant_point.y)] = row['SAMPLE_1']
  return hydrants_to_elev

