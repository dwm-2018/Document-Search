# Document Search
Calculate fertile land area in square meters, sorted from smallest area to greatest and separated by a 
space, given submitted coordinates of barren land.
## Preparation
Install [Python](https://www.python.org/)  
Pull down the repo.  
Open a mac terminal window or windows command prompt.  
Before running tests or the application, navigate to the root of the Document-Search folder.  
## Running the unit tests 
The following command will execute all of the tests.
```
py -m unittest discover -v
```
## Running the application
```
py run.py
```
At the prompt, enter a term to search for.  
You will be prompted to choose the type of search you wish to use.
## Running the performance tests
```
py run.py -p
```
## Performance test results and analysis
2M searches with random search terms were run against all three search methods. Timing results were
as follows:
```
Simple Search Elapsed Time: 26351ms
Regular Expression Search Elapsed Time: 89231ms
Index Search Elapsed Time: 5808ms
```
The Index Search was significantly faster than the other searches. This is because the search against
the hash index used was an inverse hash. The words of the search files are used as the keys of the hash
index enabling the complexity of the search to be O(1). The regular expression and simple string search 
are required to search the entire list of words every search making those searches O(n).
## Changes to allow for scale - 5000 requests/sec or more
First I would create a FIFO queue to queue the requests and distribute the work across threads/processors. The regex and simple string searches would not 
scale well for volume of data. The more data there is, the worse
those searches would get. The larger the queue grew, the longer the wait time would be as each long running search would
compound the wait time for the following search.  The index search could scale by creating multiple indexes files and searching them 
in parallel. 