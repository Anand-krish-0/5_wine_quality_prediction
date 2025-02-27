import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# loading the dataset to a pandas dataframe

wine_dataset = pd.read_csv('winequality-red.csv')

def show_explore_page():

    st.title("Explore wine qualities")
    st.success("Quality of Wine")
    fig, ax = plt.subplots()
    # Plot using seaborn countplot
    sns.countplot(x='quality', data=wine_dataset, ax=ax)
    st.pyplot(fig)


    # volatile acidity vs quality
    st.success("Volatile acidity vs Quality")
    plot = plt.figure(figsize=(5,5))
    st.bar_chart(x='quality', y='volatile acidity', data=wine_dataset)


    # citric acid vs quality
    st.success("Citric acid vs Quality")
    plot = plt.figure(figsize=(5,5))
    st.bar_chart(x='quality', y='citric acid', data=wine_dataset)

    # cunstructing a heat map to understand the correlation between the columns

    correlation = wine_dataset.corr()
   
    st.success("Correlation")
    fig1, ax = plt.subplots()
    plt.figure(figsize=(10,10))
    sns.heatmap(correlation, cbar=True, square=True, fmt='.1f', annot=True, annot_kws={'size':8}, cmap='Blues', ax=ax)
    st.pyplot(fig1)

    #plt.figure(figsize=(10,10))
    #sns.heatmap(correlation, cbar=True, square=True, fmt='.1f', annot=True, annot_kws={'size':8}, cmap='Blues')