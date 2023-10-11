#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import plotly.express as px


phone_data_path = r"https://raw.githubusercontent.com/Romanos-Rizk/hazem-msba325/main/phone_price.csv"
company_data_path = r'https://raw.githubusercontent.com/Romanos-Rizk/hazem-msba325/main/map.csv'

st.title("Phone Market Analysis")
st.write("Phone price analysis explores how a phone company's location influences pricing, considering factors like operating costs, market demand, and proximity to suppliers. This geographic presence significantly impacts the pricing strategies, with varying expenses in different areas and influences like regulatory compliance and consumer preferences playing essential roles in determining phone prices.")

phone_df = pd.read_csv(phone_data_path)
company_df = pd.read_csv(company_data_path)

st.header("Phone Prices Distribution")
st.write("The bar chart below illustrates the prices of various phone brands. You can utilize the slider to select a specific price range and discover which phones are available within that budget.")
# Create a slider to select the price range
min_price = min(phone_df['Price'])
max_price = max(phone_df['Price'])
selected_price_range = st.slider("Select Price Range:", min_price, max_price, (min_price, max_price))

# Filter the phone DataFrame based on the selected price range
filtered_phone_df = phone_df[(phone_df['Price'] >= selected_price_range[0]) & (phone_df['Price'] <= selected_price_range[1])]

# Create the bar chart
fig = px.histogram(filtered_phone_df, x="Brand", y="Price", title="Phone Prices Distribution")

# Add callback to update the chart
st.plotly_chart(fig, use_container_width=True)

st.header("Companies Producing Phones Location")
st.write("the map below shows the different locations of the companies.using the slider you can explore the location of each company relate its location potentianl effect on its prices ")

# Create a slider to select the country
selected_country = st.select_slider("Select a Country:", company_df['company'].unique())

# Filter the company DataFrame based on the selected country
filtered_company_df = company_df[company_df['company'] == selected_country]

# Create a map with the selected country
fig = px.scatter_geo(filtered_company_df, lat="latitude", lon="longitude", text="company")
st.plotly_chart(fig, use_container_width=True)


# In[3]:


import os

streamlit_app_code = """
import streamlit as st
import pandas as pd
import plotly.express as px

phone_data_path = r"https://raw.githubusercontent.com/Romanos-Rizk/hazem-msba325/main/phone_price.csv"
company_data_path = r'https://raw.githubusercontent.com/Romanos-Rizk/hazem-msba325/main/map.csv'

st.title("Phone Market Analysis")
st.write("Phone price analysis explores how a phone company's location influences pricing, considering factors like operating costs, market demand, and proximity to suppliers. This geographic presence significantly impacts the pricing strategies, with varying expenses in different areas and influences like regulatory compliance and consumer preferences playing essential roles in determining phone prices.")

phone_df = pd.read_csv(phone_data_path)
company_df = pd.read_csv(company_data_path)

st.header("Phone Prices Distribution")
st.write("The bar chart below illustrates the prices of various phone brands. You can utilize the slider to select a specific price range and discover which phones are available within that budget.")
# Create a slider to select the price range
min_price = min(phone_df['Price'])
max_price = max(phone_df['Price'])
selected_price_range = st.slider("Select Price Range:", min_price, max_price, (min_price, max_price))

# Filter the phone DataFrame based on the selected price range
filtered_phone_df = phone_df[(phone_df['Price'] >= selected_price_range[0]) & (phone_df['Price'] <= selected_price_range[1])]

# Create the bar chart
fig = px.histogram(filtered_phone_df, x="Brand", y="Price", title="Phone Prices Distribution")

# Add callback to update the chart
st.plotly_chart(fig, use_container_width=True)

st.header("Companies Producing Phones Location")
st.write("the map below shows the different locations of the companies.using the slider you can explore the location of each company relate its location potential effect on its prices ")

# Create a slider to select the country
selected_country = st.select_slider("Select a Country:", company_df['company'].unique())

# Filter the company DataFrame based on the selected country
filtered_company_df = company_df[company_df['company'] == selected_country]

# Create a map with the selected country
fig = px.scatter_geo(filtered_company_df, lat="latitude", lon="longitude", text="company")
st.plotly_chart(fig, use_container_width=True)
"""

file_path = "my_streamlit_app.py"
with open(file_path, "w") as file:
    file.write(streamlit_app_code)

print(f"Streamlit app code has been saved to {os.path.abspath(file_path)}")


# In[ ]:


#get_ipython().system('streamlit run my_streamlit_app.py')


# In[ ]:




