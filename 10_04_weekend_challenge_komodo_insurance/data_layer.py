
class Badge:
    """Badge is a class of individual badges with access to specific doors"""

    def __init__(self, badge_num, door_permissions=[]):
        self.badge_num = int(badge_num)
        self.door_permissions = door_permissions

    def __repr__(self):
        return f"{self.badge_num} " + " ".join(self.door_permissions)

    def __str__(self):
        return f"{self.badge_num} " + " ".join(self.door_permissions)

    def add_permissions(self, new_permissions=[]):
        """To add door permissions to a particular badge"""
        self.door_permissions.append(new_permissions)
        
    def remvove_permissions(self, old_permissions=[]):
        """To remove door permissions from a particular badge"""
        pass  #Fix 

class Menu:
    """Menu manages the permission levels of the badges"""

    def __init__(self, contents={}):
        self.contents = contents

    def __repr__(self):
        return f"Badge Access: \n" + {self.contents}  #fix come back and iterate this to be pretty

    def __str__(self):
        return f"Badge Access: \n" + {self.contents}  #fix come back and iterate this to be pretty

    def read(self):
        return self.contents
        # return f"Badge Access: \n" + {self.contents}  #fix come back and iterate this to be pretty

    def add_badge(self, new_badge):
        self.contents[new_badge] = []  # watch this to see if it works, append to dict

#? How to do dictionary with { badge : [permissions]} ?
#? Add/remove door permissions within the Badge class doesn't seem to work, because a badge isn't its own iterable. it's just a part of the dictionary entry. so make the changes at the menu level?