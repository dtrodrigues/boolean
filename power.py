#!/usr/bin/env python
#
# power.py
# allows the user to explore the boolean lattice
# Author: Dustin Rodrigues
# Date: Feb 12, 2011

from itertools import combinations
import pdb

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
        """returns True if the list is diamond-free"""
        eltDict = self.makeDict(eltList)

        for elt in eltList:
            bot = elt
            mids = []
            modList = eltList[:]
            modList.remove(elt)
            temp = combinations(modList, 2)

            # removes items that have one mid candidate that is lower or
            # the same level as the bottom

            eltImage = self.imageList(elt, modList)
            for item in temp:
                if (len(item[0]) > len(bot)) and (len(item[1]) > len(bot)):
                    # makes sure both of the mid candidates are in
                    # the image of elt
                    if (item[0] in eltImage) and (item[1] in eltImage):
                        mids.append(item)
           # print mids

            for i in mids:
                modModList = modList[:]
                #print modModList
                #print i[0]
                #print i[1]
                modModList.remove(i[0])
                modModList.remove(i[1])

                #print i[0], i[1], modModList
                if self.interDict(i[0], i[1], modModList):
                    #print 'false'
                    return False
                #else:
                    #print i[0], "has no intersection with", i[1], "in", modModList
        #print 'true'
        return True

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

    def interDict(self, elt1, elt2, elts):
        """returns True if the images of elt1 and elt2 have a non-trivial intersection in elts"""
        #pdb.set_trace()
        im1 = self.imageList(elt1, elts)
        im2 = self.imageList(elt2, elts)

        try:
            im1.remove(elt2)
            im2.remove(elt1)
        except:
            pass

        dict1 = self.makeDict(im1)
        dict2 = self.makeDict(im2)

        keys1 = dict1.keys()
        keys2 = dict2.keys()
        shared = []
        for i in keys1:
            if i in keys2:
                shared.append(i)

        theDict = {}
        for i in shared:
            theDict[i] = []
            for j in dict1[i]:
                theDict[i].append(j)
            for k in dict2[i]:
                theDict[i].append(k)

        for i in theDict:
            for j in theDict[i]:
                if theDict[i].count(j) > 1:
                    return True

        return False


    def imageList(self, elt, elts):
        """takes a list or dict and returns a list of the elements of the image of elt (elements that contain elt)"""
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
        """NOT IMPLEMENTED: returns a list of the elements of the shadow (elements that are contained by elt)"""
        pass

    def induced(self, elt1, elt2):
        """NOT IMPLEMENTED: returns the subposet indued between el1 and elt2 (with elt1 < elt2)"""
        pass


    def maxFree(self, eltList):
        """returns the size of the largest subset of eltList that does not contain a diamond"""
        i=1
        repeat = True
        while repeat:
            repeat = False
            theList = []
            temp = combinations(eltList, i)
            for item in temp:
                theList.append(list(item))

            j = 0
            while j < len(theList):
                if self.diamondFree(theList[j]):
                    success = len(theList[j])
                    j = len(theList)
                    repeat = True
                j += 1
            i += 1
        return success

def main():
    """docstring for main"""
    pass
#    a = ps(3)
#    #a.diamondFree(a.PowerSet)
#    #b = a.makeDict(a.imageList([1],a.PowerSet))
#    print a.maxFree(a.PowerSet)

if __name__ == '__main__':
    main()
    #a = ps(5)
    #a.diamondFree(a.PowerSet)
    #b = a.makeDict(a.imageList([1],a.PowerSet))
    #print a.maxFree(a.PowerSet)
    #print a.diamondFree([[],[2],[3],[1,2],[1,3],[2,3]])
