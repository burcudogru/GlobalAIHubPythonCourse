listOdd=[1,3,5,7,9,11,13,15]
listEven=[2,4,6,8,10,12,14,16]
listOdd.extend(listEven)
listMix= (i*2 for i in listOdd)
for i in listMix:
  print("Variable: {} and  Type: {}".format(i,type(i)))