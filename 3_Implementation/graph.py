import plotly.express as px
import pandas as pd
from ClassRoom import *

my_data = data_for_graph()
PS_list = get_PS()


def radar_graph(ps_number):
    consolidated_data = my_data[ps_number]
    post_test_data = consolidated_data[0]
    post_survey_data = consolidated_data[1]
    pre_test_data = consolidated_data[2]
    pre_survey_data = consolidated_data[3]

    df0 = pd.DataFrame(dict(
        r=post_test_data,
        theta=['L0_1', 'L0_2', 'L0_3', 'L0_4', 'L0_5', 'L0_6']))
    fig0 = px.line_polar(df0, r='r', theta='theta', line_close=True)

    df1 = pd.DataFrame(dict(
        r=post_survey_data,
        theta=['L0_1', 'L0_2', 'L0_3', 'L0_4', 'L0_5', 'L0_6']))
    fig1 = px.line_polar(df1, r='r', theta='theta', line_close=True)

    df2 = pd.DataFrame(dict(
        r=pre_survey_data,
        theta=['L0_1', 'L0_2', 'L0_3', 'L0_4', 'L0_5', 'L0_6']))
    fig2 = px.line_polar(df2, r='r', theta='theta', line_close=True)

    df3 = pd.DataFrame(dict(
        r=pre_test_data,
        theta=['L0_1', 'L0_2', 'L0_3', 'L0_4', 'L0_5', 'L0_6']))
    fig3 = px.line_polar(df3, r='r', theta='theta', line_close=True)

    fig0.show()
    fig0.write_image(f"C:/Users/utkar/Desktop/SDLC/RMap_0_of_{ps_number}.jpeg")
    fig1.show()
    fig1.write_image(f"C:/Users/utkar/Desktop/SDLC/RMap_1_of_{ps_number}.jpeg")
    fig2.show()
    fig2.write_image(f"C:/Users/utkar/Desktop/SDLC/RMap_2_of_{ps_number}.jpeg")
    fig3.show()
    fig3.write_image(f"C:/Users/utkar/Desktop/SDLC/RMap_3_of_{ps_number}.jpeg")
