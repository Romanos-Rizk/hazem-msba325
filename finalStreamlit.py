#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import plotly.express as px
#import plotly.graph_objects as go

phone_data_path = r"https://raw.githubusercontent.com/Romanos-Rizk/hazem-msba325/main/phone_price.csv"
company_data_path = r'https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fraw.githubusercontent.com%2FRomanos-Rizk%2Fhazem-msba325%2Fmain%2Fmap.xlsx&wdOrigin=BROWSELINK'

st.title("Phone Market Analysis")


phone_df = pd.read_csv(phone_data_path)


company_df = pd.read_excel(company_data_path)


st.header("Phone Prices Distribution")


fig = px.histogram(phone_df, x="Brand",y="Price", title="Phone Prices Distribution")
st.plotly_chart(fig)


st.header("Companies Producing Phones Location")

fig = px.scatter_geo(company_df, lat="latitude", lon="longitude", text="company")
st.plotly_chart(fig)


st.sidebar.header("Select a Phone to Buy")
selected_phone = st.sidebar.selectbox("Choose a phone:", phone_df['Brand'])
st.write(f"You selected: {selected_phone}")


st.sidebar.header("Explore Price-Demographics Relationship")
demographics_option = st.sidebar.checkbox("Explore price-demographics relationship")
if demographics_option:
    st.write("YYou believe the prices are related to demographics. YOU ARE RIGHT! the location where companies produce phones affects various cost components of production, including labor, taxes, supply chain efficiency, and regulatory compliance. These factors collectively influence the overall production cost and, consequently, the pricing strategy. Companies carefully evaluate these factors to determine the most cost-effective production locations and pricing strategies for their phones in the global market.")
else:
    st.write("You don't believe the prices are related to demographics.")


# In[ ]:


import os

streamlit_app_code = """
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

phone_data_path = r"C:\\Users\\User\\Desktop\\Data visualizaton\\phone_price.csv"
company_data_path = r'C:\\Users\\User\\Desktop\\Data visualizaton\\map.xlsx'

st.title("Phone Market Analysis")

# Load phone data into a DataFrame
phone_df = pd.read_csv(phone_data_path)

# Load company data into a DataFrame
company_df = pd.read_excel(company_data_path)

# Visual 1: Histogram of Phone Prices
st.header("Phone Prices Distribution")

# Use Plotly Express to create a histogram
fig = px.histogram(phone_df, x="Brand",y="Price", title="Phone Prices Distribution")
st.plotly_chart(fig)

# Visual 2: Map of Companies Producing Phones
st.header("Companies Producing Phones Location")

# Use Plotly Express to create a scatter_geo plot
fig = px.scatter_geo(company_df, lat="latitude", lon="longitude", text="company")
st.plotly_chart(fig)

# Interactive 1: Selecting a Phone to Buy
st.sidebar.header("Select a Phone to Buy")
selected_phone = st.sidebar.selectbox("Choose a phone:", phone_df['Brand'])
st.write(f"You selected: {selected_phone}")

# Interactive 2: Explore Relationship Between Prices and Demographics
st.sidebar.header("Explore Price-Demographics Relationship")
demographics_option = st.sidebar.checkbox("Explore price-demographics relationship")
if demographics_option:
    st.write("You believe the prices are related to demographics. YOU ARE RIGHT! the location where companies produce phones affects various cost components of production, including labor, taxes, supply chain efficiency, and regulatory compliance. These factors collectively influence the overall production cost and, consequently, the pricing strategy. Companies carefully evaluate these factors to determine the most cost-effective production locations and pricing strategies for their phones in the global market.")
else:
    st.write("You don't believe the prices are related to demographics.")
"""

file_path = "my_streamlit_app.py"


with open(file_path, "w") as file:
    file.write(streamlit_app_code)


print(f"Streamlit app code has been saved to {os.path.abspath(file_path)}")


# In[ ]:


get_ipython().system('streamlit run my_streamlit_app.py')


# In[ ]:


get_ipython().system('streamlit run my_streamlit_app.py')


# In[ ]:




