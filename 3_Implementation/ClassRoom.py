# Importing all the necessary library
import pandas as pd

# Import all the excel files
pre_test = pd.read_excel("pre_test.xlsx")
pre_survey = pd.read_excel("pre_survey.xlsx")
post_test = pd.read_excel("post_test.xlsx")
post_survey = pd.read_excel("post_survey.xlsx")


# Calculating the data which is required for implementation of radar graph
def data_for_graph():
    post_test_LO = []
    post_survey_LO = []
    pre_test_LO = []
    pre_survey_LO = []
    consolidated_LO = []
    data = {}
    for i in range(0, 10):  # iterates throw all the rows
        for j in range(4, 10):  # iterated throw column
            post_test_LO.append(post_test.iloc[i, j])
            post_survey_LO.append(post_survey.iloc[i, j])
            pre_test_LO.append(pre_test.iloc[i, j])
            pre_survey_LO.append(pre_survey.iloc[i, j])
        consolidated_LO.append(pre_survey_LO)  # appended the list into consolidated list
        consolidated_LO.append(pre_test_LO)
        consolidated_LO.append(post_survey_LO)
        consolidated_LO.append(post_test_LO)
        post_test_LO = []
        post_survey_LO = []
        pre_test_LO = []
        pre_survey_LO = []
        data[post_test.iloc[i, 1]] = consolidated_LO
        consolidated_LO = []
    return data  # returning the result in the form of dictionaries


# Function for getting the list of all PS number
def get_PS():
    PS_list = []
    for i in range(0, 10):
        PS_list.append(post_test.iloc[i, 1])
    return PS_list


# average performance of the students in all the module
def avg():
    avg_list = []
    pre_test_avg_list = []
    pre_survey_avg_list = []
    post_survey_avg_list = []
    post_test_avg_list = []
    post_survey_sum = 0
    post_test_sum = 0
    pre_test_sum = 0
    pre_survey_sum = 0
    for i in range(4, 10):
        for j in range(0, 10):
            post_survey_sum += post_survey.iloc[j, i]
            post_test_sum += post_test.iloc[j, i]
            pre_survey_sum += pre_survey.iloc[j, i]
            pre_test_sum += pre_test.iloc[j, i]
        post_survey_avg_list.append(post_survey_sum / 10)
        post_test_avg_list.append(post_test_sum / 10)
        pre_test_avg_list.append(pre_test_sum / 10)
        pre_survey_avg_list.append(pre_survey_sum / 10)

    avg_list.append(pre_survey_avg_list)
    avg_list.append(pre_test_avg_list)
    avg_list.append(post_survey_avg_list)
    avg_list.append(post_test_avg_list)

    return avg_list


# Sum of rows for calculating the average marks of the students
def sum_of_row():
    res = []
    post_survey_sum = 0
    post_test_sum = 0
    pre_test_sum = 0
    pre_survey_sum = 0
    post_survey_row_sum = []
    pre_survey_row_sum = []
    post_test_row_sum = []
    pre_test_row_sum = []
    for i in range(0, 10):
        for j in range(4, 10):
            pre_survey_sum += pre_survey.iloc[i, j]
            pre_test_sum += pre_test.iloc[i, j]
            post_survey_sum += post_survey.iloc[i, j]
            post_test_sum += post_test.iloc[i, j]
        post_survey_row_sum.append(post_survey_sum)
        pre_survey_row_sum.append(pre_survey_sum)
        post_test_row_sum.append(post_test_sum)
        pre_test_row_sum.append(pre_test_sum)
        post_survey_sum = 0
        pre_test_sum = 0
        pre_survey_sum = 0
        post_test_sum = 0
    res.append(pre_survey_row_sum)
    res.append(pre_test_row_sum)
    res.append(post_survey_row_sum)
    res.append(post_test_row_sum)
    return res


# top five performers of the class
def top_five(k):
    top5 = []
    sum_rows = sum_of_row()
    sum_rows = sum_rows[k]
    sum_rows.sort()
    sum_rows.reverse()
    j = 0
    for i in range(len(sum_rows)):
        j = sum_rows[i]
        top5.append(j)
        if i == 4:
            break
    return top5


# Bottom five performer of class
def bottom_five(k):
    bottom5 = []
    sum_rows = sum_of_row()
    sum_rows = sum_rows[k]
    sum_rows.sort()
    j = 0
    for i in range(len(sum_rows)):
        j = sum_rows[i]
        bottom5.append(j)
        if i == 4:
            break
    return bottom5
