# Visit https://tutorialdeep.com/knowhow/key-maximum-value-dictionary-python/

myDict = {'one': 24, 'two': 13, 'three': 54, 'four': 9}
MaxDictVal = max(myDict, key=myDict.get)
print(MaxDictVal)