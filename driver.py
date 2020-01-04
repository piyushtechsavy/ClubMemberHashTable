from member import Member
from hashtable import MemberHashTable

class ApplicationDriver:
  def __init__(self):
    self.memberMap = MemberHashTable()

  def readInputFile(self):
    inputFile = open("inputPS8.txt", "r")
    count = 0
    for line in inputFile:
      memberDataList = line.split("/")
      count+= 1;
      newMember = Member(memberDataList[0].strip(),memberDataList[1].strip(),memberDataList[2].strip(),memberDataList[3].strip())
      
      self.memberMap.insertAppDetails(newMember)
    
    inputFile.close()

    outputFile = open("outputPS8.txt", "w")
    outputFile.write("Successfully inserted %d applications into the system." %(count));
    outputFile.close()

  def readAndProcessPromptsFile(self):
    promptsFile = open("promptsPS8.txt", "r")
    for line in promptsFile:
      if line.startswith("Update"):
        self.updateAppDetails(line)
  
  def updateAppDetails(self, updateString):
    print("updating")



  

