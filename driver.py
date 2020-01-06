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
    outputFile.write("Successfully inserted %d applications into the system.\n" %(count));
    outputFile.close()
    

  def readAndProcessPromptsFile(self):
    promptsFile = open("promptsPS8.txt", "r")
    for line in promptsFile:
      if line.startswith("Update"):
        self.updateAppDetails(line)
      elif line.startswith("memberRef"):
        self.memRef(line)
      elif line.startswith("appStatus"):
        self.appStatus()

    member = self.memberMap.getAppDetails("Deepak Prasad")


  def memRef(self,line):
    print("memRef")

  def appStatus(self):
    print("appStatus")

  
  def updateAppDetails(self, updateString):
    memberDataList = updateString.replace("Update:","").split("/")

    member = self.memberMap.getAppDetails(memberDataList[0].strip())

    newPhoneNumber = memberDataList[1].strip()
    newMRef = memberDataList[2].strip()
    newStatus = memberDataList[3].strip()

    updateString = "Updating details of " + member.name + "."

    if member.phoneNumber != newPhoneNumber:
      member.phoneNumber = newPhoneNumber
      updateString = updateString + "Phone Number has been changed.\n"
    
    if member.mRef != newMRef:
      member.mRef = newMRef
      updateString = updateString + "Member Reference has been changed.\n"
    
    if member.status != newStatus:
      member.status = newStatus
      updateString = updateString + "Status has been changed.\n"
    
    outputFile = open("outputPS8.txt", "a")
    outputFile.write(updateString);
    outputFile.close()



    



  

