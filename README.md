CsvUtils
========

Some useful CSV tools

1. CsvDatapicker - to extract certain columns and save to a new file:

	Usage: CsvDatapicker.py <CSVin> <CSVout> <"columns comma separated"> <separator>
	Example: CsvDatapicker.py csvin.csv csvout.csv 2,3,4,7,9 ,

2. CsvDatainsertion - to insert new columns to a existing file from a insertion file:

	Usage: CsvDatainsertion.py <CSVtoAlter> <CSVinsertion> <"columns insert to - comma separated"> <separator>
	Example: CsvDatainsertion.py existing.csv insertion.csv 0,7 ,
