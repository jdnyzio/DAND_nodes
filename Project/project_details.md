## How do I Complete this Project?
This project is connected to the <a href="https://www.udacity.com/course/viewer#!/c-ud032-nd" target="_blank">Data Wrangling with MongoDB</a> course, but depending on your background knowledge of data wrangling, you may not need to take the whole thing to complete this project. 

Here's what you should do:

### Step One - Finish Lesson 6 
Make sure all Lesson 6 programming exercises are solved correctly.
### Step Two - Review the Rubric and Sample Project
The <a href="https://docs.google.com/document/d/1TpfNxDzUjhibq9Qb8cOQHtlvZUelft-W0fb7pCTTyYE/pub?embedded=True" target="_blank">**Project Rubric**</a>
 will be used to evaluate your project.  It will need to Meet Specifications for all the criteria listed.  The <a href="https://docs.google.com/document/d/1F0Vs14oNEs2idFJR3C_OPxwS6L0HPliOii-QpbmrMo4/pub?embedded=True" target="_blank">**Sample Project**</a>
 is an example of what your final report could look like. 
### Step Three - Choose Your Map Area
Choose any area of the world from <a href="https://www.openstreetmap.org" target="_blank">**https://www.openstreetmap.org**</a>
, and download a XML OSM dataset. The dataset should be at least **50MB in size (uncompressed)**. We recommend using **one** of following methods of downloading a dataset:

* Download a preselected metro area from <a href="https://mapzen.com/metro-extracts/" target="_blank">**Map Zen**</a> (Note that data obtained from Map Zen is compressed and will usually expand to sizes that meet project requirements.)
* Use the <a href="http://overpass-api.de/query_form.html" target="_blank">**Overpass API**</a>
 to download a custom square area. Explanation of the syntax can  found in the <a href="http://wiki.openstreetmap.org/wiki/Overpass_API" target="_blank">**wiki**</a>
.  In general you will want to use the following query:
<code>
  (node(minimum_latitude, minimum_longitude, 
maximum_latitude, maximum_longitude);<;);out meta;
</code> 
e.g.
<code>
  (node(51.249,7.148,51.251,7.152);<;);out meta;
</code>
the `meta` option is included so the elements contain timestamp and user information.
You can use the Open Street Map <a href="http://www.openstreetmap.org/export#map=5/42.618/-7.559" target="_blank">**Export Tool**</a>
 to find the coordinates of your bounding box.  Note: You will not be able to use the Export Tool to actually download the data, the area required for this project is too large.

### Step Four - Process your Dataset
Thoroughly audit and clean your dataset, converting it from XML to JSON format.  It is recommended that you start with the Lesson 6 exercises and modify them to suit your chosen data set. As you unravel the data, take note of problems encountered along the way as well as issues with the dataset. You are going to need these when you write your project report.  Finally, import the clean JSON file into a MongoDB database and run some queries against it. 
### Step Five - Document your Work 
Create a document (pdf, html) that directly addresses the following sections from the <a href="https://docs.google.com/document/d/1TpfNxDzUjhibq9Qb8cOQHtlvZUelft-W0fb7pCTTyYE/pub?embedded=True" target="_blank">**Project Rubric**</a>
.  

* **Problems encountered in your map**
* **Overview of the Data**
* **Other ideas about the datasets**

Try to include snippets of code and problematic tags (see <a href="https://docs.google.com/document/d/1F0Vs14oNEs2idFJR3C_OPxwS6L0HPliOii-QpbmrMo4/pub?embedded=True" target="_blank">**Sample Project**</a>) and visualizations in your report if they are applicable.