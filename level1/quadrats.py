f = open("data.txt", "r")
nums=[]
mitjana = 0

for line in f:
  nums.append(int(line))
f.close()

for num in nums:
  mitjana += num

print (mitjana/len(nums))
