column1 = []
column2 = []

def mitjana(list_of_numbs):
  total_sum = 0
  #One way of doing the average
  #for i in list_of_numbs:
  #total_sum = total_sum + int(i)
  
  #A second way of doing the average (by using sum(int(i) for i in list_of_numbs)) 
  total_sum = sum(int(i) for i in list_of_numbs)
  print(float(total_sum)/len(list_of_numbs))

with open('data2.txt', 'r') as f:
  for line in f:
    if line[-1] == "\n":
      clean_line = line.rstrip()
    column1.append(clean_line.split()[0])
    column2.append(clean_line.split()[1])

mitjana(column1)
mitjana(column2)
