class MemberHashTable:
  def __init__(self):
    self.map = dict()
  
  def hashId(self, str):
    return len(str)

  def initializeHash(self):
    self.map=[None]
  
  def insertAppDetails(self,member):
    key_exists = False
    key = member.name
    hashKey = self.hashId(key)
    bucket = self.map.get(hashKey)

    if not bucket:
      self.map[hashKey]=[]
      bucket = self.map.get(hashKey)

    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            key_exists = True 
            break
    if key_exists:
        bucket[i] = ((key, member))
    else:
        bucket.append((key, member))

  def print(self):
    print(self.map)

  def getAppDetails(self,name):
    key = name
    hashKey = self.hashId(key)
    bucket = self.map.get(hashKey)

    if bucket:
      for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
          return v
    
    return None
