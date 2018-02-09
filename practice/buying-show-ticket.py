# Buying Show Ticket Problem
# First Appeared on Feb 8, 2018 by CTP Prep

def calculateTime(array, index):
  for counter, value in enumerate(array):
    array[counter] = {'id_num': counter, 'count': value}
  
  from collections import deque
  queue= deque(array)
  
  counter = 1
  
  while len(queue) != 0:
    head = queue.popleft()
    if (head['id_num'] == index) and (head['count'] - 1 == 0):
      break
    
    counter += 1
    
    if (head['count'] - 1) > 0:
      head['count'] -= 1
      queue.append(head)
      
  return counter


# The following are a set of simple assertion tests
# There should be no message shown in CLI when this script is run
assert(calculateTime([2,6,3,4,5], 2) == 12)
assert(calculateTime([5,5,2,3], 3) == 11)
assert(calculateTime([1,1,1,1], 0) == 1)