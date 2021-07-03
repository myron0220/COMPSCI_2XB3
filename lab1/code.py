from typing import List

## @brief Check if the groups are valid
#  @details The groups are valid if and only if each student number is in exactly one
#  group and each group size is 2 or 3
#  @param sl List of string representing student numbers
#  @param gl List of groups. Each group is a list of student numbers
#  @return True if the groups are valid, False otherwise
def are_valid_groups(sl : List[str], gl: List[List[str]]):
  for s in sl:
    if sum([1 if s in g for g in gl]) != 1:
      return False
  for g in gl:
    if len(g) > 3 or len(g) < 2:
      return False
  return True