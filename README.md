# Data collection
## Requirements 
- numpy
- pandas
- python 3.0+
- gcc 8.2.1 +
- 'time' linux package

## tldr
1. Run automate.py to collect the data by default there are:
          - 1000 random instances of quick sort (O nlogn)
          - 500 sequential-random instances of matrix multiplication (O n^3)
          - 45 instances of fibonacci series generator (O 2^n)
2. Run test.py to print the dataframe on terminal          

## Important commands :
- elf files
  In computing, the Executable and Linkable Format (ELF, formerly named Extensible Linking Format), is a common standard file format for executable files, object code, shared libraries, and core dumps.
  (.exe files in windows is analogous to elf files in linux)

- readelf
  readelf is a unix command that displays information about one or more ELF format object files. The options control what particular information to display.
  `readelf -S a.out`
  "-S" above shows the section data headers which we are using to uniquely identify our file
  to understand these various sections, refer: ![pg 19-21 of this pdf](http://www.skyfree.org/linux/references/ELF_Format.pdf)

