#!/usr/bin/env python

from user import User

import random

class Teacher(User):

    def teach(self):
        index = random.randint(0, 7)
        return self.knowledge[index]

