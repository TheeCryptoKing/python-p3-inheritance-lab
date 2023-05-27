#!/usr/bin/env python

from user import User

class Student(User):
    
    def learn(self, stng):
        return self.knowledge.append(stng)