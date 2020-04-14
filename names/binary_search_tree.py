class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value < self.value:
      if not self.left:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.value > target:
      if self.left:
        return self.left.contains(target)
      else:
        return False
    else:
      if self.right:
        return self.right.contains(target)
      else:
        return False

  def get_max(self):
    if self.right:
      max = self.right.get_max()
    else:
      return self.value
    return max


  def for_each(self, cb):
    cb(self.value)
    if self.right and self.left:
      cb(self.right.value)
      cb(self.left.value)
      self.right.for_each(cb)
      self.left.for_each(cb)
    elif self.right and not self.left:
      cb(self.right.value)
      self.right.for_each(cb)
    elif self.left and not self.right:
      cb(self.left.value)
      self.left.for_each(cb)
    else:
      pass