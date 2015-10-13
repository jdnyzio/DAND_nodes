**OpenStreetMap Project Details**

> [*How do I Complete this Project?*](#how-do-i-complete-this-project)
>
> [*Step One - Finish the OpenStreetMaps Case
> Study.*](#step-one---finish-the-openstreetmaps-case-study.)
>
> [*Step Two - Review the Rubric and Sample
> Project*](#step-two---review-the-rubric-and-sample-project)
>
> [*Step Three - Choose Your Map
> Area*](#step-three---choose-your-map-area)
>
> [*Step Four - Process your
> Dataset*](#step-four---process-your-dataset)
>
> [*Step Five - Explore your
> Database*](#step-five---explore-your-database)
>
> [*Step Six - Host your map online*](#step-six---host-your-map-online)
>
> [*Step Seven - Document your Work*](#step-seven---document-your-work)
>
> [*Evaluation*](#evaluation)
>
> [*Rubric*](#rubric)
>
> [*Submission*](#submission)


**How do I Complete this Project?**
-----------------------------------

This project is connected to the [Intro to Data Wrangling
](https://www.udacity.com/course/viewer#!/c-ud032-nd)[and](https://www.udacity.com/course/viewer#!/c-ud032-nd)[
SQL for Data
Analysis](https://www.udacity.com/course/viewer#!/c-ud032-nd) courses,
but depending on your background knowledge, you may not need to take all
of this coursework to complete the project.

Here's what you should do:

### **Step One - Finish the OpenStreetMaps Case Study.**

Solve all OpenStreetMap Case Study programming exercises at the end of
[Intro to Data
Wrangling](https://www.udacity.com/course/viewer#!/c-ud032-nd).

Solve the Problem Sets located at the end of each Lesson in [SQL for
Data Analysis](https://www.udacity.com/course/viewer#!/c-ud032-nd).

### **Step Two - Review the Rubric and Sample Project**

The [**Project
Rubric**](https://docs.google.com/document/d/1TpfNxDzUjhibq9Qb8cOQHtlvZUelft-W0fb7pCTTyYE/pub?embedded=True)(TODO)
will be used to evaluate your project. It will need to Meet
Specifications for all the criteria listed. The [**Sample
Project**](https://docs.google.com/document/d/1F0Vs14oNEs2idFJR3C_OPxwS6L0HPliOii-QpbmrMo4/pub?embedded=True)(TODO)
is an example of what your final report could look like.

### **Step Three - Choose Your Map Area**

Choose any area of the world from
[**https://www.openstreetmap.org**](https://www.openstreetmap.org/) ,
and download a XML OSM dataset. The dataset should be at least **50MB in
size (uncompressed)**. We recommend using **one** of following methods
of downloading a dataset:

-   Download a preselected metro area from 
    > [**MapZen**](https://mapzen.com/metro-extracts/) (Note that data
    > obtained from Map Zen is compressed and will usually expand to
    > sizes that meet project requirements.)

-   Use the [**Overpass API**](http://overpass-api.de/query_form.html) to download a custom square area. 
    > Explanation of the syntax can be found in the [**wiki**](http://wiki.openstreetmap.org/wiki/Overpass_API) . 
    > In general you will want to use the following query:
    > (node(minimum\_latitude, minimum\_longitude, maximum\_latitude, maximum\_longitude);\<;);out meta; 
    > e.g.(node(51.249,7.148,51.251,7.152);\<;);out meta; the meta option is
    > included so the elements contain timestamp and user information.
    > You can use the OpenStreetMap [**Export
    > Tool**](http://www.openstreetmap.org/export#map=5/42.618/-7.559)
    > to find the coordinates of your bounding box. Note: You will not
    > be able to use the Export Tool to actually download the data, the
    > area required for this project is too large.

### **Step Four - Process your Dataset**

Thoroughly audit and clean your dataset. It is recommended that you
start with the OpenStreetMap case study exercises and modify them to
suit your chosen data set. As you unravel the data, take note of
problems encountered along the way as well as issues with the dataset.
You are going to need these when you write your project report.

### **Step Five - Explore your Database**

Flatten your clean osm file into a SQLite3 database using the open
source QGIS platform. Explore your data and document the results of your
SQL queries.

### **Step Six - Host your map online**

After running queries against your data, use QGIS to build an
interactive map that you can host online to share with the world!

### **Step Seven - Document your Work**

Create a document (pdf, html) that directly addresses the following
sections from the [**Project
Rubric**](https://docs.google.com/document/d/1TpfNxDzUjhibq9Qb8cOQHtlvZUelft-W0fb7pCTTyYE/pub?embedded=True)

-   **Problems encountered in your map**

-   **Overview of the Data**

-   **Other ideas about the datasets**

Try to include snippets of code and problematic tags (see [***Sample
Project***](https://docs.google.com/document/d/1F0Vs14oNEs2idFJR3C_OPxwS6L0HPliOii-QpbmrMo4/pub?embedded=True))
and visualizations in your report if they are applicable.

**Evaluation**
--------------

A Udacity evaluator will review and check your completion of the
OpenStreetMap Case Study in[ Intro to Data
Wrangling](https://www.udacity.com/course/viewer#!/c-ud032-nd).

Your answers to the questions in the rubric will be used to determine
your understanding of the SQL query language.

Be sure to complete all of questions in the problem set and the rubric
before submitting your project.

**Rubric**
----------

Your project will be evaluated by a Udacity reviewer according to this
[project
rubric](https://docs.google.com/document/d/1TpfNxDzUjhibq9Qb8cOQHtlvZUelft-W0fb7pCTTyYE/pub?embedded=true)(TODO).
Be sure to review it thoroughly before you submit. Your "project meets
specifications" if it meets specifications in all the criteria

**Submission**
--------------

Ready to submit your project? Collect the following files:

1.  A pdf document containing your answers to the rubric questions.
    > This file should document your data wrangling process.

2.  Your Python code for the OpenStreetMap Case Study, 
    > as well as any additional code you used in auditing and cleaning your dataset for
    > the final project.

3.  A text file containing 
    > Link to the map position you wrangled in your project
    > Link to the QGIS cloud hosted map you've created. 
    > Short description of the area and a reason for your choice.

4.  An .osm file containing a sample part of the map region you used
    > (around 1 - 10 MB in size). See instructor notes.

5.  A text file containing a list of 
    > Web sites, books, forums, blog
    > posts, github repositories etc that you referred to or used in
    > this submission (Add N/A if you did not use such resources).

Then go back to your Udacity Home, click on the project, and follow the
instructions to submit:

-   If you want to submit your files through a "Link to Project"
    > Upload your project files onto Github and send us the link.

-   If you instead want to submit your files through "Upload a Zip",
    > Compress your project directory, and submit that zip file.

You should receive a full evaluation of your project within 24 hours of
your original submission.

If you are having any problems submitting your project or wish to check
on the status of your submission, please email us at
dataanalyst-project@udacity.com.
