import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px
import json 
import requests
import numpy as np
import plotly.express as px


dl=r"C:\Users\HP\Desktop\phonepeproject\DataSets\DDW_B18_0800_NIC_FINAL_STATE_RAJASTHAN-2011.csv"
df_list1 = pd.read_csv(dl,encoding='latin1') 

d2=r"DataSets/DDW_B18_1200_NIC_FINAL_STATE_ARUNACHAL_PRADESH-2011.csv"
df_list2 = pd.read_csv(d2,encoding='latin1') 

d3=r"C:\Users\HP\Desktop\phonepeproject\DataSets\DDW_B18_1400_NIC_FINAL_STATE_MANIPUR-2011.csv"
df_list3 = pd.read_csv(d3,encoding='latin1') 

d4=r"C:\Users\HP\Desktop\phonepeproject\DataSets\DDW_B18_1500_NIC_FINAL_STATE_MIZORAM-2011.csv"
df_list4 = pd.read_csv(d4,encoding='latin1') 

d5=r"C:\Users\HP\Desktop\phonepeproject\DataSets\DDW_B18_1900_NIC_FINAL_STATE_WEST_BENGAL-2011.csv"
df_list5 = pd.read_csv(d5,encoding='latin1') 

d6=r"DataSets/DDW_B18sc_0700_NIC_FINAL_STATE_NCT_OF_DELHI-2011.csv"
df_list6 = pd.read_csv(d6,encoding='latin1') 

d7=r"DataSets/DDW_B18sc_1600_NIC_FINAL_STATE_TRIPURA-2011.csv"
df_list7 = pd.read_csv(d7,encoding='latin1') 

d8=r"DataSets/DDW_B18sc_2000_NIC_FINAL_STATE_JHARKHAND-2011.csv"
df_list8 = pd.read_csv(d8,encoding='latin1') 

d9=r"DataSets/DDW_B18sc_2400_NIC_FINAL_STATE_GUJARAT-2011.csv"
df_list9 = pd.read_csv(d9,encoding='latin1') 


d10=r"DataSets/DDW_B18sc_2700_NIC_FINAL_STATE_MAHARASHTRA-2011.csv"
df_list10 = pd.read_csv(d10,encoding='latin1')

d11=r"DataSets/DDW_B18sc_2900_NIC_FINAL_STATE_KARNATAKA-2011.csv"
df_list11 = pd.read_csv(d11,encoding='latin1')

d12=r"DataSets/DDW_B18sc_3000_NIC_FINAL_STATE_GOA-2011.csv"
df_list12 = pd.read_csv(d12,encoding='latin1')

d13=r"DataSets/DDW_B18sc_3200_NIC_FINAL_STATE_KERALA-2011.csv"
df_list13= pd.read_csv(d13,encoding='latin1')

d14=r"DataSets/DDW_B18sc_3300_NIC_FINAL_STATE_TAMIL_NADU-2011.csv"
df_list14= pd.read_csv(d14,encoding='latin1')

d15=r"DataSets/DDW_B18sc_3400_NIC_FINAL_STATE_PUDUCHERRY-2011.csv"
df_list15= pd.read_csv(d15,encoding='latin1')

d16=r"DataSets/DDW_B18st_0200_NIC_FINAL_STATE_HIMACHAL_PRADESH-2011.csv"
df_list16= pd.read_csv(d16,encoding='latin1')

d17=r"DataSets/DDW_B18st_0500_NIC_FINAL_STATE_UTTARAKHAND-2011.csv"
df_list17= pd.read_csv(d17,encoding='latin1')

d18=r"DataSets/DDW_B18st_0900_NIC_FINAL_STATE_UTTAR_PRADESH-2011.csv"
df_list18= pd.read_csv(d18,encoding='latin1')

d19=r"DataSets/DDW_B18st_1000_NIC_FINAL_STATE_BIHAR-2011.csv"
df_list19= pd.read_csv(d19,encoding='latin1')

d20=r"DataSets/DDW_B18st_1100_NIC_FINAL_STATE_SIKKIM-2011.csv"
df_list20= pd.read_csv(d20,encoding='latin1')

d21=r"DataSets/DDW_B18st_1300_NIC_FINAL_STATE_NAGALAND-2011.csv"
df_list21= pd.read_csv(d21,encoding='latin1')

d22=r"DataSets/DDW_B18st_1800_NIC_FINAL_STATE_ASSAM-2011.csv"
df_list22= pd.read_csv(d22,encoding='latin1')

d23=r"DataSets/DDW_B18st_2100_NIC_FINAL_STATE_ODISHA-2011.csv"
df_list23= pd.read_csv(d23,encoding='latin1')

df=pd.concat([df_list1,df_list2,df_list3,df_list4,df_list5,df_list6,df_list7,df_list8,df_list9,df_list10,df_list11,df_list12,df_list13,df_list14,df_list15,df_list16,df_list17,df_list18,df_list19,df_list20,df_list21,df_list22,df_list23],axis=0)

def remove_special_characters(column_name):
    # Replace any non-alphanumeric characters with an empty string
    return ''.join(e for e in column_name if e.isalnum())

# Rename columns using the remove_special_characters function
df.rename(columns=remove_special_characters, inplace=True)

#streamlitpart

st.set_page_config(layout= "wide")
st.title("Industrail Geo Visualization")


with st.sidebar:

    select= option_menu("MAIN MENU",["Home","MAIN WORKERS","MARGINAL WORKERS"])

if select =="HOME":
    
    col1,col2=st.columns(2)
    with col1:
       st.header("Geo Visualization")
       st.subheader("Analysis of workers in different region")

    with col2:
       st.image(r"C:\Users\HP\Desktop\phonepeproject\360_F_306823780_e8NQk2txuotDZPLRB7HN38XkXb9u49hY.jpg")

elif select =="MAIN WORKERS":
    tab1, tab2, tab3= st.tabs(["Main Workers","Main Workers Rural","Main workers Urban"])
    
    with tab1:
        df_1=pd.DataFrame(df,columns=("StateCode", "MainWorkersTotalPersons"))

        fig_1= px.bar(df_1, x="StateCode",y=["MainWorkersTotalPersons"],title=" Main Workers",
                        color_discrete_sequence=px.colors.sequential.Agsunset,height=650,width=1000,hover_name="StateCode")
        st.plotly_chart(fig_1)

        df_2=pd.DataFrame(df,columns=("StateCode", "MainWorkersTotalMales"))

        fig_2= px.bar(df_2, x="StateCode",y=["MainWorkersTotalMales"],title=" Main Male",
                        color_discrete_sequence=px.colors.sequential.YlGnBu_r,height=650,width=1000,hover_name="StateCode")
        st.plotly_chart(fig_2)

        df_3=pd.DataFrame(df,columns=("StateCode", "MainWorkersTotalFemales"))

        fig_3= px.bar(df_3, x="StateCode",y=["MainWorkersTotalFemales"],title=" Main Female",
                        color_discrete_sequence=px.colors.sequential.Magenta_r,height=650,width=1000,hover_name="StateCode")
        st.plotly_chart(fig_3)

    with tab2:
        df_4=pd.DataFrame(df,columns=("StateCode", "MainWorkersRuralPersons"))

        fig_4= px.bar(df_4, x="StateCode",y=["MainWorkersRuralPersons"],title=" Main Workers Rural Total",
                        color_discrete_sequence=px.colors.sequential.Agsunset,height=650,width=1000,hover_name="StateCode")
        st.plotly_chart(fig_4)

        df_5=pd.DataFrame(df,columns=("StateCode", "MainWorkersRuralMales"))

        fig_5= px.bar(df_5, x="StateCode",y=["MainWorkersRuralMales"],title=" Main Workers Rural Male",
                        color_discrete_sequence=px.colors.sequential.YlGnBu_r,height=650,width=1000,hover_name="StateCode")
        st.plotly_chart(fig_5)

        df_6=pd.DataFrame(df,columns=("StateCode", "MainWorkersRuralFemales"))

        fig_6= px.bar(df_6, x="StateCode",y=["MainWorkersRuralFemales"],title=" Main Female",
                        color_discrete_sequence=px.colors.sequential.Magenta_r,height=650,width=1000,hover_name="StateCode")
        st.plotly_chart(fig_6)

    with tab3:
        df_7=pd.DataFrame(df,columns=("StateCode", "MainWorkersUrbanPersons"))

        fig_7= px.bar(df_7, x="StateCode",y=["MainWorkersUrbanPersons"],title=" Main Female",
                        color_discrete_sequence=px.colors.sequential.Magenta_r,height=650,width=1000,hover_name="StateCode")
        st.plotly_chart(fig_7)

        df_8=pd.DataFrame(df,columns=("StateCode", "MainWorkersUrbanMales"))

        fig_8= px.bar(df_8, x="StateCode",y=["MainWorkersUrbanMales"],title=" Main Female",
                        color_discrete_sequence=px.colors.sequential.Pinkyl_r,height=650,width=1000,hover_name="StateCode")
        st.plotly_chart(fig_8)

        df_9=pd.DataFrame(df,columns=("StateCode", "MainWorkersUrbanFemales"))

        fig_9= px.bar(df_9, x="StateCode",y=["MainWorkersUrbanFemales"],title=" Main Female",
                        color_discrete_sequence=px.colors.sequential.Pinkyl_r,height=650,width=1000,hover_name="StateCode")
        st.plotly_chart(fig_9)
