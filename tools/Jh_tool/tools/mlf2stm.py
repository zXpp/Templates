#!/usr/bin/python

"""
Converts a given MLF to an STM file. Optionally, an additional STM can be
provided from which tags can be extracted for a given pair of identifier
and speaker.

@author:    Herman Kamper
@contact:   kamperh@sun.ac.za
@date:      15-08-2011
"""

import os
import re
import sys

SENTENCE_MARKER = "!SENT_START"


#-------------------------------------------------------------------------#
#                            UTILITY FUNCTIONS                            #
#-------------------------------------------------------------------------#

def checkArgv():
    """
    Checks the command line arguments.
    """
    if len(sys.argv) != 3 and len(sys.argv) != 4:
        print "Usage: MLFtoSTM.py <MLF> <STM> [<tags STM>]"
        sys.exit(0)


#-------------------------------------------------------------------------#
#                         IMPLEMENTATION FUNCTIONS                        #
#-------------------------------------------------------------------------#

def readMLF(mlfFN):
    """
    Reads a given MLF and returns a dictionary of the contents.
    
    @type mlfFN:    str
    @param mlfFN:   The filename of the MLF.
    @rtype:         dict
    @return:        For example, dict["safm_2804"] would give a list of
                    tokens for the entry marked as "safm_2804.lab".
    """

    # Read the MLF
    f = open(mlfFN, "r")
    lines = f.readlines()
    f.close()

    # Determine the index of word labels by finding the maximum line length
    wordIndex = -1
    for line in lines:
        line = line.split()
        if wordIndex < len(line) - 1:
            wordIndex = len(line) - 1
        if line == ["."]:
            break
    if wordIndex == -1:
        print "Error: No labels were found."
        sys.exit(1)

    # Move through the MLF content and read the labels
    mlfDict = {}
    for line in lines:
        # Obtain the next line
        line = line.strip()
        if line == "#!MLF!#" or line == ".":
            continue
        
        # Determine the MLF label file
        if line[0] == '"':
            labelFile = re.sub(r'"\*\/|\.lab\"', "", line)
            if labelFile in mlfDict:
                print "Error: Duplicate label file: " + labelFile
                sys.exit(1)
            mlfDict[labelFile] = []
            continue

        # Determine if it is a line without a word label
        line = line.split(" ")
        if len(line) == wordIndex + 1:
            line = line[-1]
        else:
            continue
        
        # Append the label
        if line != SENTENCE_MARKER:
            mlfDict[labelFile].append(line)
    
    # Return the MLF dict
    return mlfDict
    
    
def readTags(stmFN):
    """
    Reads the tags from a given STM file and returns a dictionary. Tags
    are extracted according uniqe identifier and speaker pairs.
    
    @type stmFN:    str
    @param stmFN:   The STM filename.
    @rtype:         dict
    @return:        For example, dict[("safm_7201", "M002")] would give the
                    tags for the identifier "safm_7201" and speaker M002 in
                    a string format.
    """
    tagDict = {}
    f = open(stmFN, "r")
    for entry in f:
        line = entry.split()
        try:
            identifier = line.pop(0)
            channel = line.pop(0)
            speakerID = line.pop(0)
            startTime = float(line.pop(0))
            endTime = float(line.pop(0))
            tags = line.pop(0)
        except ValueError:
            print "Warning: Invalid entry: " + (" ".join(entry.split()[:8]) + " ...")
            continue
        tagDict[(identifier, speakerID)] = tags
    f.close()
    return tagDict


#-------------------------------------------------------------------------#
#                              MAIN FUNCTION                              #
#-------------------------------------------------------------------------#

def main():
    """
    The main function which is run when the script is executed.
    """

    # Check the validity of the command line arguments
    checkArgv()
    mlfFN = sys.argv[1]
    stmFN = sys.argv[2]
    if not os.path.isfile(mlfFN):
        print "Error: File does not exist: " + mlfFN
        sys.exit(1)
    if os.path.isfile(stmFN):
        print "Error: File exists, delete if sure: " + stmFN
        sys.exit(1)
    if len(sys.argv) == 4:
        tagSTMFN = sys.argv[3]
        if not os.path.isfile(tagSTMFN):
            print "Error: File does not exist: " + tagSTMFN
            sys.exit(1)
    else:
        tagSTMFN = None

    # Read the given MLF
    print "Reading MLF: " + mlfFN
    mlfDict = readMLF(mlfFN)
    
    # If the additional STM are provided, read the tags
    if tagSTMFN != None:
        print "Reading STM file giving tags: " + tagSTMFN
        tagDict = readTags(tagSTMFN)
        
    # Write the new STM
    print "Writing STM: " + stmFN
    f = open(stmFN, "w")
    for labelFile in sorted(mlfDict.keys()):
        source, session, speakerID, startFrame, endFrame = labelFile.split("_")
        identifier = source + "_" + session
        startTime = float(startFrame)*10e-3
        endTime = float(endFrame)*10e-3
        if tagSTMFN != None:
            if (identifier, speakerID) in tagDict:
                tags = tagDict[(identifier, speakerID)]
            else:
                print "Error: Tags not defined for pair: (" + identifier + ", " + speakerID + ")" 
                sys.exit(1)
        else:
            tags = "<>"
        f.write("%s 1 %s %.3f %.3f %s" % (identifier, speakerID, startTime, endTime, tags) + " " + " ".join(mlfDict[labelFile]) + "\n")
    f.close()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
