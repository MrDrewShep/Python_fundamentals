from enum import Enum

class Side(Enum):
    none = 0
    left = 1
    right = 2

class ChainLink:

    def __init__(self):
        self._left = None
        self._right = None

    def append(self, link):
        if self._right is not None: raise Exception('Link already connected!')
        self._right = link
        link._left = self

    def longer_side(self):
        current_link = self
        i = 0
        while 1:
            try:
                current_link._right
                current_link = current_link._right
                i += 1
                if current_link == self:
                    return Side.none
            except:
                break
        right = i
        
        current_link = self
        i = 0
        while 1:
            try:
                current_link._left
                current_link = current_link._left
                i += 1
            except:
                break
        left = i
        
        print(left, right)
        
        if right == left:
            return Side.none
        elif right > left:
            return Side.right
        elif left > right:
            return Side.left
        
                
        return None

left = ChainLink()
middle = ChainLink()
right = ChainLink()
left.append(middle)
middle.append(right)
print(left.longer_side() == Side.right)