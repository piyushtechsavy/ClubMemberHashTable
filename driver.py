from member import Member
from memberhashtable import MemberHashTable

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
    
    promptsFile.close()


  def memRef(self,refString):
    memberRef = refString.replace("memberRef:","").strip()

    outputFile = open("outputPS8.txt", "a")
    outputFile.write("---------- Member reference by "+ memberRef +" ----------\n")

    for key in self.memberMap.keys:
      member = self.memberMap.getAppDetails(key)
      if member.mRef == memberRef:
        outputFile.write(member.memberInfo())
    
    outputFile.write("-------------------------------------\n")
    outputFile.close()


  def appStatus(self):
    applied = verified = approved = 0
    for key in self.memberMap.keys:
      member = self.memberMap.getAppDetails(key)
      if member.status == "Applied":
        applied = applied+1;
      elif member.status == "Verified":
        verified = verified + 1
      elif member.status == "Approved":
        approved = approved + 1  
    
    outputFile = open("outputPS8.txt", "a")
    outputFile.write("---------- Application Status ----------\n")
    outputFile.write("Applied: %d\n" %(applied))
    outputFile.write("Verified: %d\n" %(verified))
    outputFile.write("Approved: %d\n" %(approved))
    outputFile.write("-------------------------------------\n")
    outputFile.close()

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



    



  

