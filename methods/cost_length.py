def costLength(hydrant_i, hydrant_j)
  if hydrant_i.distance(hydrant_j) <= max_edge_length:
    return (hydrant_i.distance(hydrant_j)/max_edge_length)* x
  else:
    return 1 
