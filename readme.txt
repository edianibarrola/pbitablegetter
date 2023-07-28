This code stuff will take the HTML of a PowerBi Dataset Table / grab the table names and columns and export it to a csv file.   
------------------- html to csv -------------------
You must go to power bi on web.
Go to the dataset.   
expand all the tables so the columns are visible.
inspect the browser.
find the table container.   (i use <entitites-list _ngcontent (different for each one) araia-label "Dataset Tables" ...>) 
If you hover over the table you can get to the parent html easier 


right click the table container in the html inspector and click Expand recursive.

copy html element and paste into input.txt file that is pre-made.
(if there are alot of tables, the expand recursive can take like 10-15 seconds, so if you when you paste, it doesnt work, try to copy it again.)

MAKE SURE YOU SAVE THE NEW input.txt   (if there is a white circle next to the name of the file tab up top, it is not saved and it will use whatever was previously there when you run the program)
In the terminal type python pbitableripper.py 

the code will process the html in input.txt and create output.csv 

Download the output.csv because it will be replaced when you run the program again.
When you save it, Rename the CSV to "Workspace name - Dataset name"    (For example CRP - Ambulatory Report)    This is important for merging all the output files later if you do more than one.


------------------- Combine all outputs to new file and add the Dataset Name Column ------------------


if you need to merge multiple output files,  make sure you follow the above naming convention.
then add them to the input folder that is pre-made.   

once they are all in the folder, type
python csvtotable.py   (in terminal)

this will create a merged csv with all the files that you added to the input folder.
Download that new file and you are done.  