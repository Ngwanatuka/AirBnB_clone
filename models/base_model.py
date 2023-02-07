#!/usr/bin/env python3
""" A Base class with common methods/attributes
for other classes
"""

import uuid
from datetime import datetime, time, date

class BaseModel:
   """a class that defines attributes id,
   created_at, udated_at and methods
   """
   def __init__(self):
    """ constructor for class attrs id
    created_at and mehtods
    """
        
    self.id = str(uuid.uuid4())
    
    self.created_at = datetime.now()
    
    self.updated_at = datetime.now()
        
    def __str__(self):
        """ returns a string repr of the class
        """
        return (f"[{self.__class__.__name__}]({self.id}) {self.__dict__}")
        
        
    def save(self):
        """updates the update_at attr
        """
        self.updated_at = datetime.now()
        
        
        def to_dict(self):
        """ returns a dictionsary repr of the instance
        """
        my_dict = self.__dict__.copy()
        my_dict.update({
            "__class__": self.__class__.__name__,
            "update_at": self.updated_at.isoformat(),
            "created_at": self.created_at.isoformat()
            })
        return my_dict
