def costSlope(hydrant_i, hydrant_j):
  rise = hydrant_j.elevationID - hydrant_i.elevationID
  run = hydrant_j.distance(hydrant_i)
  slope = rise/run
  if slope < 0:
    return 1
  return slope / x 