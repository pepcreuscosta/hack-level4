column1 = []
column2 = []

def mitjana(list_of_numbs):
  total_sum = 0
  #One way of doing the average
  #for i in list_of_numbs:
  #total_sum = total_sum + int(i)

  #A second way of doing the average (by using sum(int(i) for i in list_of_numb$
  total_sum = sum(int(i) for i in list_of_numbs)
  return float(total_sum)/len(list_of_numbs)

def variancia(list_of_numbs):  
  average = mitjana(list_of_numbs)
  return sum([(x - average)**2 for x in list_of_numbs])/len(list_of_numbs)

def minim(list_of_numbs):
  if len(list_of_numbs) == 0:
    return None
  minim_actual = list_of_numbs[0]
  for i in list_of_numbs:
    if i < minim_actual:
      minim_actual = i
  return minim_actual

def maxim(list_of_numbs):
  if len(list_of_numbs) == 0:
    return None
 
  maxim_actual = list_of_numbs[0]
  for i in list_of_numbs:
    if i > maxim_actual:
      maxim_actual = i
  return maxim_actual

def parells(nums):
  parell = []
  for x in nums:
    if x%2 == 0:
      parell.append(x)
  return parell

def parellscompactes(nums):
  return [x for x in nums if x%2 == 0]

def apply_funcs(nums, func):
    return [i(nums) for i in func]

with open('data2.txt', 'r') as f:
  for line in f:
    if line[-1] == "\n":
      clean_line = line.rstrip()
    column1.append(float(clean_line.split()[0]))
    column2.append(float(clean_line.split()[1]))

print (mitjana(column1))
print (mitjana(column2))
print (variancia(column1))
print (variancia(column2))
print (minim(column1))
print (maxim(column1))
print (minim(column2))
print (maxim(column2))
print (parells(column1))
print (parells(column2))
print (parellscompactes(column1))
print (parellscompactes(column2))
print (apply_funcs([1,2,3,4,5], [mitjana,parells,minim,maxim]))
