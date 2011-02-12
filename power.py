#!/usr/bin/env python
#
# power.py
# allows the user to explore the boolean lattice
# Author: Dustin Rodrigues
# Date: Feb 12, 2011

from itertools import combinations

# TODO: finish diamondFree
# TODO: finish interDict
# TODO: finish maxFree


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

    def diamondFree(self, eltList):
        """NOT FULLY IMPLEMENTED: returns True if the list is diamond-free"""
        eltDict = self.makeDict(eltList)

        for elt in eltList:
            bot = elt
            mids = []
            modList = eltList[:]
            modList.remove(elt)
            temp = combinations(modList, 2)

            # removes items that have one mid candidate that is lower
            # than bottom
            for item in temp:
                if (len(item[0]) > len(bot)) and (len(item[1]) > len(bot)):
                    mids.append(item)
            print mids

            for i in mids:
                modModList = modList[:]
                print modModList
                print i[0]
                print i[1]
                modModList.remove(i[0])
                modModList.remove(i[1])

                if self.interDict(i[0], i[1], modModList):
                    return True

        return False


    def makeDict(self, eltList):
        """returns a list of the elements in eltList indexed by their length"""
        eltDict = {}
        for elt in eltList:
            if len(elt) in eltDict:
                eltDict[len(elt)].append(elt)
            else:
                eltDict[len(elt)] = [elt]
        return eltDict

    def makeList(self, eltDict):
        """takes a dict and returns the list of elts in it"""
        res = []
        for i in eltDict.itervalues():
            for j in i:
                res.append(j)
        return res

    def interDict(self, elt1, elt2, eltDict):
        """NOT YET IMPLEMENTED: returns True if the images of elt1 and elt2 have a non-trivial intersection in eltDict"""
        pass
        im1 = self.makeDict(self.imageList(elt1, eltDict))
        im2 = self.makeDict(self.imageList(elt2, eltDict))


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


    def maxFree(self, eltList):
        """returns the size of the largest subset of eltList that does not contain a diamond"""
        # start to look at combinations of eltList of size 1 then
        # checking if this subset is diamond free.  if one of them is, increase
        # the size of combinations and check again


if __name__ == '__main__':
    a = ps(4)
    a.diamondFree(a.PowerSet)
    b = a.makeDict(a.imageList([1],a.PowerSet))


