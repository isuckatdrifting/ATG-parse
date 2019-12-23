# ATG-parse
Python script for converting binary AXI Traffic Generator coe files to hex table.

`addr`, `data`, `ctrl`, and `mask` file directories are loaded via parameters in order.

The result will be printed on terminal. You may manually copy it to a text file for further analysis.

Example Usage -- Binary to Hex Table

`
Python3 bin2hex.py ./src/addr.coe ./src/data.coe ./ctrl.coe ./mask.coe
`