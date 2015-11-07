
'''
Driver skeleton

1)
import libraries
import student code and solution code

2) call student code and solution code on test input
   student code and solution code should return a pandas
   frame

3) compare student and solution dataframes:
    1) if dfs equal, return success message
    2) if dfs do not equal, write dfs to csv and return diffs


'''


######################################## 1)
import difflib
import json
import pandas as pd
import numpy as np
import subprocess
import sqlite3
import sys


from query import QUERY as student_code
from solution import QUERY as solution_code

#---------------------------------------------

def sort_data_frame(df):
    return df.sort_index(axis=1)

def assert_frame_equal(df1, df2, **kwds):
    """ Assert that two dataframes are equal, ignoring ordering of columns"""
    from pandas.util.testing import assert_frame_equal
    return assert_frame_equal(df1.sort_index(axis=1), df2.sort_index(axis=1), check_names=False, check_dtype=False, **kwds)


pass_msg = "Good job! Your code worked perfectly.\nOutput by your program below.\n"
fail_msg = "The output by your program does not match the solution ouput."


########################################## 2)
def output(q):
    db = sqlite3.connect("chinook.db")
    c = db.cursor()
    c.execute(q)
    columns = c.description
    result = []
    for value in c.fetchall():
        tmp = {}
        for (index,column) in enumerate(value):
            tmp[columns[index][0]] = column
        result.append(tmp)
    df = pd.DataFrame(result)
    return df

student_df = output(student_code)
solution_df = output(solution_code)
output = dict()

########################################## 3)

if isinstance(student_df, pd.DataFrame):
    try:
        student_copy = student_df.copy()
        student_copy.columns = solution_df.columns
        assert_frame_equal(student_copy, solution_df)
        output['pass'] = True
        output['message'] = pass_msg + "\n\n" + student_df.to_string(justify="right")
    except ValueError:
        '''    
        The student and solution data frames are not equal
        '''
        output['pass'] = False
        output['message'] = fail_msg + \
            "\nThe first output is the solution output.\nThe second output is your output\n\n" + \
            "solution:\n" + \
            solution_df.to_string(justify="right") + \
            "\n\nyour output:\n" + \
            student_df.to_string(justify="right") 
    except AssertionError:
        '''    
        The student and solution data frames are not equal
        '''
        output['pass'] = False
        output['message'] = fail_msg + \
            "\nThe first output is the solution output.\nThe second output is your output\n\n" + \
            "solution:\n" + \
            solution_df.to_string(justify="right") + \
            "\n\nyour output:\n" + \
            student_df.to_string(justify="right")
          
else:
     output['pass'] = False
     output['message'] = "There was an error with your SQL query"
sys.stdout.write(json.dumps(output))