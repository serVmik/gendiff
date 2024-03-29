[![Actions Status](https://github.com/serVmik/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/serVmik/python-project-50/actions) [![Python CI](https://github.com/serVmik/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/serVmik/python-project-50/actions/workflows/pyci.yml)
<a href="https://codeclimate.com/github/serVmik/python-project-50/maintainability"><img src="https://api.codeclimate.com/v1/badges/b7e09e6d677e6b2993bb/maintainability" /></a> <a href="https://codeclimate.com/github/serVmik/python-project-50/test_coverage"><img src="https://api.codeclimate.com/v1/badges/b7e09e6d677e6b2993bb/test_coverage" /></a>


### Description  
This program compares two configuration files.
The result of the file comparison can be output in different formats,
for example: plain ("flat") or json ("JSON format").
The diff is built based on how the content in the second file has changed
relative to the first.
Keys are displayed in alphabetical order.

Use input file formats: json or yaml.  

### "How to install and uninstall gendiff"  
```
git clone https://github.com/serVmik/python-project-50.git
```
$ make install  
$ make build  
$ make package-install  

$ pip uninstall hexlet-code

### How to use gendiff:  
Format "stylish":  
$ gendiff filepath1.json filepath2.json  
$ gendiff filepath1.json filepath2.json --format stylish  
https://asciinema.org/a/bqYVz1M7f8okB1M4BiRb8A8W3  
https://asciinema.org/a/aOLAZw9Qa42CSkNHwaehplKLW  
Format "plain":   
$ gendiff file1.json file2.yaml --format plain  
https://asciinema.org/a/dPYwGufKyZSTsCPwyqM5VFul9  
Format "json":   
$ gendiff file1.json file2.yaml --format json  
https://asciinema.org/a/x1VP4uYbYkXj4WItxy5C76gCB
