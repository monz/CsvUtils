#!/usr/bin/env python
# coding: utf8

from CsvUtil import CsvUtil

class CsvDatapicker(CsvUtil):
    def __init__(self, csvIn, csvOut, cols, delimiter):
        super(CsvDatapicker, self).__init__(csvOut, csvIn, cols, delimiter)

    def pickData(self):
        try:
            dIn = open(self.fIn, 'r')
            procLine = []
            sumLine = []
            
            for line in dIn:
                #reset
                sumLine = [] 
                # split original line into peaces
                procLine = (line.split(self.delimiter)) 
                # sum up the choosen cols to a new line
                for i, col in enumerate(self.cols):
                    if i < (len(self.cols) - 1):
                        sumLine.append((procLine[col] + self.delimiter))
                    else:
                        sumLine.append(procLine[col])
                # add a newline - to separate the lines - nobody has seen this coming ;)s
                sumLine.append("\n")
                # save in attribute line as list
                self.lines.append(sumLine)
            #print self.lines
            
            dIn.close()
        except IOError as e:
            print "I/O Error: %s" % (e)
            print "program terminated"
            sys.exit(-1)
            
        
    def main(self):
        self.pickData()
        self.saveFile()

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 5:
        print("USAGE: " + sys.argv[0] + " <CSVin> <CSVout> <\"columns comma separated\"> <separator>")
    else:
        a = CsvDatapicker(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
        a.main()