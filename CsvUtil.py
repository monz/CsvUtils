#!/usr/bin/env python
# coding: utf8

import sys

class CsvUtil(object):
    def __init__(self, csvOut, csvIn, cols, delimiter):
        self.fOut = csvOut
        self.fIn = csvIn
        self.cols = []
        self.delimiter = delimiter
        self.lines = []
        
        self.splitCols(cols)

    def splitCols(self, cols):
        procCol = cols.split(",")
        try:
            for c in procCol:
                self.cols.append(int(c))
        except ValueError as e:
            print "Value Error: %s" % (e)
            print "program terminated"
            sys.exit(-1)
    
    def saveFile(self):
        try:
            dOut = open(self.fOut, 'w')
            
            for line in self.lines:
                dOut.writelines(line)
            dOut.close()
        except IOError as e:    
            print "I/O Error: %s"  % (e)
            print "program terminated"
            sys.exit(-1)