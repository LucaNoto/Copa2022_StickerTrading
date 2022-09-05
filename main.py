from function import FindSwappables

myNeed = ""
myRepeated = ""
peerNeed = ""
peerRepeated = ""

if __name__ == '__main__':
   result = FindSwappables(myNeed,myRepeated,peerNeed,peerRepeated,shinnyForShinny=True)
   print(result['outputText'])
