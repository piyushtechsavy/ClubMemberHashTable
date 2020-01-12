class MemberHashTable:
  def __init__(self,size=500):
    self.map = [None]*size
    self.size = size
    self.keys = []
  
  def hashId(self, key):
    hash = 0
    for c in key:
      hash = hash + ord(c)
    
    return (hash % self.size)

  def initializeHash(self):
    self.map=[None]*self.size
    self.keys = []

  def destroyHash(self):
    self.map.clear()
    self.keys = []

  
  def insertAppDetails(self,member):
    key_exists = False
    key = member.name
    hashKey = self.hashId(key)
    bucket = self.map[hashKey]

    if not bucket:
      self.map[hashKey]=[]
      bucket = self.map[hashKey]

    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            key_exists = True 
            break
    if key_exists:
        bucket[i] = ((key, member))
    else:
        bucket.append((key, member))
        self.keys.append(key)

  def print(self):
    print(self.map)
    print(self.keys)

  def getAppDetails(self,name):
    key = name
    hashKey = self.hashId(key)
    bucket = self.map[hashKey]

    if bucket:
      for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
          return v
    
    return None
