**Getting Started with Python**
------------------------------------------

> [*Running Python locally*](#running-python-locally)
>
> [*IPython Notebook*](#ipython-notebook)
>
> [*Downloading Data Files*](#downloading-data-files)

 Running Python locally
---------------------------

In this course, we'll assume you have the ability to run Python locally.
Whether you already have Python installed on your computer or not, we
recommend downloading and installing Anaconda. This is a scientific
Python installation that comes with a lot of libraries and tools we'll
be using in this course, some of which are otherwise very difficult to
install. To install Anaconda:

1\. Navigate to http://continuum.io/downloads in your broswer.

2\. Download the Python 2.7 installer. Make sure you don't select Python
3.4, as the course will not be compatible with other versions of Python.

* On a PC, click the Windows icon and select "Windows 64-Bit Python 2.7
Graphical Installer". You can also select the 32-bit installer if you
have a 32-bit machine.

* On Mac or Linux, follow the same process but select the appropriate
installer for your platform.

3\. Run the installer and follow the instructions on the screen.

If you already have Anaconda, make sure it is up to date by opening your
Command Prompt or terminal (see below for instructions) and running the
commands:

* \`conda update conda\`

* \`conda update anaconda\`

Since Anaconda can take a few minutes to download and install, you'll be
able to follow along in the next few videos and exercises without it. We
recommend starting the process now so that once you need it, you'll be
ready to go.

IPython Notebook
---------------------

IPython notebooks are a powerful tool for data analysts, allowing you to
combine code, plots, output, and descriptions in one easily readable
document. We've provided starter code for the videos in an IPython
notebook, and we recommend following along there. Whenever Caroline runs
some code, run the same code in your notebook, and complete the
exercises in the marked places. We'll also provide a notebook at the end
of the lesson that contains solutions to all the exercises.

If you haven't used IPython notebook before, you can use the provided
tutorial notebook to get familiar with it. To do this:

1\. Download the tutorial notebook from the Downloadables section or this
link (TODO: link)

2\. Open your Command Prompt (PC) or terminal (Mac or Linux)

* On a PC click the Start button and search for "Command Prompt".

* On a Mac type command + spacebar. Then, type ''terminal" in the
Spotlight Search. You can also search for "terminal" in finder.

3\. Navigate to the directory where you downloaded the IPython notebook
file.

* On a PC you might type: \`cd C:\\Users\\username\\Downloads\\\`,
replacing your username. 
<a href="[*http://www.7tutorials.com/command-prompt-how-use-basic-commands*](http://www.7tutorials.com/command-prompt-how-use-basic-commands)"
target="\_blank"\>Learn more about basic terminal commands</a\>.

* On Mac or Linux you might type: \`cd \~/Downloads\`
* <a href="[*https://www.udacity.com/course/linux-command-line-basics--ud595*](https://www.udacity.com/course/linux-command-line-basics--ud595)"
target="\_blank"\>Learn more about basic terminal commands.</a>

4\. Run the command \`ipython notebook tutorial\_notebook.ipynb\` in your
terminal. \*\*Do not close your terminal or command prompt.\*\*

5\. The notebook should open in your default web browser. Read through
the notebook and follow the instructions in it.

You can follow this same process to open other notebooks, such as the
starter code for this lesson.

Downloading Data Files
-----------------------------

You should also download the data files in from the Downloadables
section. Make sure you save these in the same directory as your IPython
notebook. The files we'll be using in this lesson are
\`enrollments.csv\`, \`daily\_engagement.csv\`, and
\`project\_submissions.csv\`. \`daily\_engagement\_full.csv\` contains
more detailed data than \`daily\_engagement.csv\`, but it's a larger
file (about 500 MB), so downloading and using this file is optional.

You should also download and read \`table\_descriptions.txt\`, which
describes what data is present in each file (or table) and what columns
are present. The data has been anonymized, and contains a random
selection of Data Analyst Nanodegree students who had completed the
first project at the time the data was collected, as well as a random
selection of students who had not.
