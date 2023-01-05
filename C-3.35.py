def threeWaySetDisjointness(A,B,C):

  merged_list = list(A) + list(B) + list(C)
  merged_list.sort()

  for i in range(len(merged_list)-2):
    if merged_list[i] == merged_list[i+1] and merged_list[i] == merged_list[i+2]:
      return True
  return False


