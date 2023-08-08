# sorry I know this is repetitive but I cannot find any other way at this point
def find_max_min_slope(edges):
    max_slope = float('-inf')
    min_slope = float('inf')

    for edge in edges:
        point_i = points[edge.p1]
        point_j = points[edge.p2]
        hydrant_i = hydrant_instances[edge.p1]
        hydrant_j = hydrant_instances[edge.p2]
        rise = hydrant_j.elevation - hydrant_i.elevation
        run = distance(point_i, point_j)
        slope = rise / run

        # Check for maximum slope
        if slope > max_slope:
            max_slope = slope

        # Check for minimum slope
        if slope < min_slope:
            min_slope = slope

    return max_slope, min_slope


max_length = edge_df['length'].max()
min_length = edge_df['length'].min()
max_angle = edge_df['intersection_angle'].max()
min_angle = edge_df['intersection_angle'].min()
max_slope, min_slope = find_max_min_slope(edge_set_pro)


def normalize_min_max(value, min_val, max_val):
    return (value - min_val) / (max_val - min_val)


def costSlope(edge):
    hydrant_j = df_point.iloc[edge.p2]
    hydrant_i = df_point.iloc[edge.p1]
    rise = hydrant_j.elevation - hydrant_i.elevation
    run = edge.length
    slope = rise/run
    if slope < 0:
      return 1
    elif slope small:
      pass
    elif slope good:
      pass
    elif slope max:
      pass
    else:
      pass
    return normalize_min_max(slope, 0, max_slope)
