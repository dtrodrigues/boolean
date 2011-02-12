#!/usr/bin/env python
#
# power.py
# allows the user to explore the boolean lattice
# Author: Dustin Rodrigues
# Date: Feb 12, 2011

from itertools import combinations

# for readability, change class name from ps to PowerSet or Power or
# something
class ps:
    """insert class documentation here"""

    def __init__(self, x=5):
        """initializes the powerset 2^[x].  default is 5"""
        self.size = x
        self.PowerSet = []
        for i in range(0,x+1):
            temp = combinations(range(1, x+1), i)
            for item in temp:
                self.PowerSet.append(list(item))

    def contains(self, elt1, elt2):
        """returns True if elt1 contains elt2 and False otherwise"""
        for i in elt2:
            if i not in elt1:
                return False
        return True

    def hasDiamond(self, eltList):
        """NOT YET IMPLEMENTED: returns True if the list contains a 'diamond' as we have discussed in our meetings"""
        self.makeDict(eltList)

    def makeDict(self, eltList):
        """returns a list of the elements in eltList indexed by their length"""
        eltDict = {}
        for elt in eltList:
            if len(elt) in eltDict:
                eltDict[len(elt)].append(elt)
            else:
                eltDict[len(elt)] = [elt]
        return eltDict

    def interDict(self, elt1, elt2, eltDict):
        """NOT YET IMPLEMENTED: returns True if the images of elt1 and elt2 have a non-trivial intersection in eltDict"""
        im1 = self.makeDict(self.imageDict(elt1, eltDict))
        im2 = self.makeDict(self.imageDict(elt2, eltDict))


    def imageList(self, elt, elts):
        """takes a list or dict and returns a list of the elements of the image (elements contained by elt)"""
        temp = []

        if type(elts) is list:
            eltDict = self.makeDict(elts)
        else:
            eltDict = elts

        cut = len(elt)
        # removes items that are at the same or lower level as our elt
        popList = []
        for i in eltDict:
            if i <= cut:
                popList.append(i)
        for i in popList:
            eltDict.pop(i)

        for i in eltDict.itervalues():
            for j in i:
                if self.contains(j, elt):
                    temp.append(j)

        return temp

    def shadowDict(self, elt, eltDict):
        """NOT IMPLEMENTED: returns a list of the elements of the shadow (elements that contain elt)"""
        pass

    def induced(self, elt1, elt2):
        """NOT IMPLEMENTED: returns the subposet indued between el1 and elt2 (with elt1 < elt2)"""
        pass

if __name__ == '__main__':
    pass

