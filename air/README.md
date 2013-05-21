Air Quality
===========

The converted data will contain air quality metrics (e.g. carbon monoxid level) from different locations for multiple times (dimensions = locations).

Requirements
------------
 - Python

Usage
-----
Download a data package from [EPA](http://www.epa.gov/ttn/airs/airsaqs/detaildata/downloadaqsdata.htm), extract the txt file and run the following command:

	./convert.py path/to/input.txt path/to/output.txt

To encode the state and county IDs, use the [official encoding tables](http://www.itl.nist.gov/fipspubs/co-codes/states.txt).

