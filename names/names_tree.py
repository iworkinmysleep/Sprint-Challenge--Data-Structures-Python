class NamesNode:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value < self.value:

      if not self.left:
        self.left = NamesNode(value)
      else:
        self.left.insert(value)

    else:
      if not self.right:
        self.right = NamesNode(value)
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True

    if target < self.value:
      if not self.left:
        return False
      else:
        return self.left.contains(target)

    else:
      if not self.right:
        return False
      else:
        return self.right.contains(target)
