import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title='Plotting Demo')

st.title('Analytics of Gurgaon city :')

#Datasets

new_df=pd.read_csv('Datasets/data_viz1.csv')
feature_text = pickle.load(open('Datasets/feature_text.pkl','rb'))


# 1 Geographic Representation

st.write("## Geographic Representation :")

#st.dataframe(new_df)

for col in ['price','price_per_sqft','built_up_area','latitude','longitude']:
    new_df[col] = pd.to_numeric(new_df[col].astype(str), errors='coerce')

# Select only the 'sector' and the intended numeric columns for group_by
numeric_cols = ['price','price_per_sqft','built_up_area','latitude','longitude']
group_df = new_df[['sector'] + numeric_cols].groupby('sector').mean()

fig = px.scatter_mapbox(group_df, lat="latitude", lon="longitude", color="price_per_sqft", size='built_up_area',
                  color_continuous_scale=px.colors.cyclical.IceFire, zoom=10,
                  mapbox_style="open-street-map",width=1200,height=700,hover_name=group_df.index)

st.plotly_chart(fig,use_container_width=True)


# 2 WordCloud Representation

st.write("## Important Amenities :")

wordcloud = WordCloud(width = 800, height = 800,
                      background_color ='black',
                      stopwords = set(['s']),  # Any stopwords you'd like to exclude
                      min_font_size = 10).generate(feature_text)

fig, ax = plt.subplots(figsize=(8, 8))
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")
fig.tight_layout(pad=0)
st.pyplot(fig)


# 3 Scatterplot Area vs Price

st.header('Area vs Price :')

property_type = st.selectbox('Select Property Type', ['flat','house'])

if property_type == 'flat':
    fig1 = px.scatter(new_df[new_df['property_type']=='flat'], x="built_up_area", y="price", color="bedRoom")

    st.plotly_chart(fig1, use_container_width=True)

else:
    fig1 = px.scatter(new_df[new_df['property_type'] == 'house'], x="built_up_area", y="price", color="bedRoom")

    st.plotly_chart(fig1, use_container_width=True)


# 4 Pie-Chart BHK

st.header('BHK Pie-Chart :')

sector_options = new_df['sector'].unique().tolist()
sector_options.insert(0,'overall')

selected_sector = st.selectbox('Select Sector', sector_options)

if selected_sector == 'overall':

    fig2 = px.pie(new_df, names='bedRoom')

    st.plotly_chart(fig2, use_container_width=True)
else:

    fig2 = px.pie(new_df[new_df['sector'] == selected_sector], names='bedRoom')

    st.plotly_chart(fig2, use_container_width=True)


# 5 Box-plot Bedroom vs price

st.header('BHK Price Range :')

fig3 = px.box(new_df[new_df['bedRoom'] <= 4], x='bedRoom', y='price')
st.plotly_chart(fig3, use_container_width=True)


# 6 Dist-plot Price vs Flat/House

st.header('Price Range of property type :')

fig3 = plt.figure(figsize=(10, 4))
sns.distplot(new_df[new_df['property_type'] == 'house']['price'],label='house')
sns.distplot(new_df[new_df['property_type'] == 'flat']['price'], label='flat')
plt.legend()
st.pyplot(fig3)