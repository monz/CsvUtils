#!/usr/bin/env python
# coding: utf8

from CsvUtil import CsvUtil

class CsvDatainsertion(CsvUtil):
    def __init__(self, csvProc, csvInsertion, colsInsertion, delimiter):
        super(CsvDatainsertion, self).__init__(csvProc, csvInsertion, colsInsertion, delimiter)
        
    def insertData(self):
        try:
            dInsertion = open(self.fIn, 'r')
            dProc = open(self.fOut, 'r')
            normIndex = 0
            
            for line in dProc:
                normIndex = 0
                procLine = (line.split(self.delimiter))
                for i in range(len(procLine)):
                    procLine[i] = procLine[i].strip("\n")
                    if i < (len(procLine) - 1):
                        procLine[i] = procLine[i] + self.delimiter
                insertLine = dInsertion.readline()
                if insertLine:
                    insertLine = insertLine.split(self.delimiter)
                    for col in self.cols:
                        if (col + normIndex) < (len(procLine) ):
                            procLine.insert((col + normIndex), (insertLine[normIndex].strip("\n") + self.delimiter))
                        else:
                            procLine.insert((col + normIndex), self.delimiter +(insertLine[normIndex].strip("\n")))
                        normIndex += 1
                else:
                    continue
                procLine.append("\n")
                self.lines.append(procLine)
                
            dInsertion.close()
            dProc.close()
        except IOError as e:
            print "I/O Error: %s" % (e)
            print "program terminated"
            sys.exit(-1)
        except IndexError as e:
            print "Index Error: %s" % (e)
            print "program terminated"
            sys.exit(-1)
    
    def main(self):
        self.insertData()
        self.saveFile()
        
if __name__ == '__main__':
    import sys
    if len(sys.argv) < 5:
        print ("USAGE: " + sys.argv[0] + " <csvToAlter> <csvInsertion> <\"columns comma separated\"> <separator>")
    else:
        a = CsvDatainsertion(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
        a.main()