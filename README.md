# WTAHikeFinder
Takes a list of links to WTA hikes and compiles a spreadsheet filled with data about them torn from the WTA site.
The csv file will be filled with datapoints for the length, the elevation gain, the highest point, the location, the rating out of 5, and the url.

I wrote this because I was having difficulty deciding where to go on a hike one week. I found the search on the WTA website, but didn't want to manually compile the data about them. This way, I can indicriminately paste all of the relevant urls and then sort through the data in excel.

## How to use:
Paste a list of links into a text file nammed "urls.txt" and then launch the python file. Then "out.csv" will be created, filled in with all of the data ripped from the "wta.org" website

## Things to keep in mind:
* All of the urls need to begin with https://www.wta.org as copy+pasted from a browser
* Some WTA pages aren't for trails and thus don't have all of the data points. These pages cannot be parsed by the program and will cause it to crash. I am working on a fix for this.
