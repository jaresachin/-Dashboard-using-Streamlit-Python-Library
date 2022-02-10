import streamlit as st #Web app
import pandas as pd # data manipulation
import plotly.express as px #pip install plotly.express


#https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Orders dashboard",
                   page_icon=":bar_chart:",
                   layout="wide")

#Load data
df=pd.read_excel("Orders.xlsx",sheet_name=1)

#Add Header
#st.title("Orders Dashboard")

#To get color heading using HTML code
html_temp="""
<div style="background-color:orange;padding:10px">
<h4 style="color:white;text-align:center;">Streamlit Orders Dashborad </h4>
</div>
"""
st.markdown(html_temp,unsafe_allow_html=True)



st.write("")   #Add some text/ space


#------SIDEBAR---

st.sidebar.header("Please Filter Here:")
Customer=st.sidebar.multiselect(
    "Select the CustomerID:",
    options=df["CustomerID"].unique(),
    default=df["CustomerID"].unique()
)


#-----To filter according to sidebar---
df_selection=df.query(
    "CustomerID==@Customer"
)

#To get data for barchart
d1 = df_selection[["CustomerID", "PriceTotal", "Number_of_Delivery_days"]]
d2 = d1.groupby(by="CustomerID").sum()[["PriceTotal"]].sort_values(["PriceTotal"], ascending=False).reset_index()
d2["CustomerID"] = d2["CustomerID"].apply(str)
st.markdown("---")  #get line
#Plot 1: Bar Chart
st.write("**Customer Price Total:**")
bar_plot = px.bar(d2, x='CustomerID', y='PriceTotal')
st.plotly_chart(bar_plot)
st.markdown("---")  #get line

st.write("**Data Frame:**")
st.dataframe(df_selection) #data set
