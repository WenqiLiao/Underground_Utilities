#replace find_closest_road
def find_closest_road(point, roads_df, min_distance):
    closest_road_id = []

    for idx, road in roads_df.iterrows():
        distance = point.distance(road['geometry'])
        if distance < min_distance:
            closest_road_id.append(road['id'])

    return closest_road_id

#I have found that 0.0003 is a good minimum value for 
df_point['closest_road_id'] = df_point.apply(lambda row: find_closest_road(row['geometry'], df_road, 0.0003), axis=1)

df_point.drop('Closest_Road_ID', axis=1, inplace=True)

print(df_point)
