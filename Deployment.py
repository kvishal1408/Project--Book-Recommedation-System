# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 15:35:20 2022

@author: WIN-10
"""

import pickle
import streamlit as st
import numpy as np
    
    
popular_df= pickle.load(open('popular.pkl','rb'))
pivot_table = pickle.load(open('pivot.pkl','rb'))
books= pickle.load(open('books.pkl','rb'))
similarity_scores = pickle.load(open('similarity_score.pkl','rb'))

book_name    = popular_df ['Book-Title'].tolist()
author       = popular_df['Book-Author'].tolist()
ratings      = popular_df['Num-of-ratings'].tolist()
image        = popular_df['Image-URL-M'].tolist()
avg_ratings  = popular_df['Avg-ratings'].tolist()
books_list   = pivot_table.index.values

st.title('Book Recommendation System')
st.sidebar.title("Most Popular Books")
if st.sidebar.button("View"):
    col1,col2=st.columns(2)
    with col1:
        st.text("1"[0])
        st.image(image[0])        
        st.text("Title : "+str(book_name[0]))
        st.text("Author : "+str(author[0]))
        st.text("Total Ratings : "+str(ratings[0]))
        st.text("Average Rating : "+str(round(avg_ratings[0],1)))
    with col1:
        st.text("2"[0])
        st.image(image[1])        
        st.text("Title : "+str(book_name[1]))
        st.text("Author : "+str(author[1]))
        st.text("Total Ratings : "+str(ratings[1]))
        st.text("Average Rating : "+str(round(avg_ratings[1],1)))    
    with col1:
        st.text("3"[0])
        st.image(image[2])        
        st.text("Title : "+str(book_name[2]))
        st.text("Author : "+str(author[2]))
        st.text("Total Ratings : "+str(ratings[2]))
        st.text("Average Rating : "+str(round(avg_ratings[2],1)))
    with col1:
        st.text("4"[0])
        st.image(image[3])        
        st.text("Title : "+str(book_name[3]))
        st.text("Author : "+str(author[3]))
        st.text("Total Ratings : "+str(ratings[3]))
        st.text("Average Rating : "+str(round(avg_ratings[3],1)))
    with col1:
        st.text("5"[0])
        st.image(image[4])        
        st.text("Title : "+str(book_name[4]))
        st.text("Author : "+str(author[4]))
        st.text("Total Ratings : "+str(ratings[4]))
        st.text("Average Rating : "+str(round(avg_ratings[4],1)))
    with col1:
        st.text("6"[0])
        st.image(image[5])        
        st.text("Title : "+str(book_name[5]))
        st.text("Author : "+str(author[5]))
        st.text("Total Ratings : "+str(ratings[5]))
        st.text("Average Rating : "+str(round(avg_ratings[5],1)))
    with col1:
        st.text("7"[0])
        st.image(image[6])        
        st.text("Title : "+str(book_name[6]))
        st.text("Author : "+str(author[6]))
        st.text("Total Ratings : "+str(ratings[6]))
        st.text("Average Rating : "+str(round(avg_ratings[6],1)))    
    with col1:
        st.text("8"[0])
        st.image(image[7])        
        st.text("Title : "+str(book_name[7]))
        st.text("Author : "+str(author[7]))
        st.text("Total Ratings : "+str(ratings[7]))
        st.text("Average Rating : "+str(round(avg_ratings[7],1)))    
    with col1:
        st.text("9"[0])
        st.image(image[8])        
        st.text("Title : "+str(book_name[8]))
        st.text("Author : "+str(author[8]))
        st.text("Total Ratings : "+str(ratings[8]))
        st.text("Average Rating : "+str(round(avg_ratings[8],1)))    
    with col1:
        st.text("10"[0:2])
        st.image(image[9])        
        st.text("Title : "+str(book_name[9]))
        st.text("Author : "+str(author[9]))
        st.text("Total Ratings : "+str(ratings[9]))
        st.text("Average Rating : "+str(round(avg_ratings[9],1)))    
    with col1:
        st.text("11"[0:2])
        st.image(image[10])        
        st.text("Title : "+str(book_name[10]))
        st.text("Author : "+str(author[10]))
        st.text("Total Ratings : "+str(ratings[10]))
        st.text("Average Rating : "+str(round(avg_ratings[10],1)))
    with col1:
        st.text("12"[0:2])
        st.image(image[11])        
        st.text("Title : "+str(book_name[11]))
        st.text("Author : "+str(author[11]))
        st.text("Total Ratings : "+str(ratings[11]))
        st.text("Average Rating : "+str(round(avg_ratings[11],1)))    
    with col1:
        st.text("13"[0:2])
        st.image(image[12])        
        st.text("Title : "+str(book_name[12]))
        st.text("Author : "+str(author[12]))
        st.text("Total Ratings : "+str(ratings[12]))
        st.text("Average Rating : "+str(round(avg_ratings[12],1)))
    with col1:
        st.text("14"[0:2])
        st.image(image[13])        
        st.text("Title : "+str(book_name[13]))
        st.text("Author : "+str(author[13]))
        st.text("Total Ratings : "+str(ratings[13]))
        st.text("Average Rating : "+str(round(avg_ratings[13],1)))
    with col1:
        st.text("15"[0:2])
        st.image(image[14])        
        st.text("Title : "+str(book_name[14]))
        st.text("Author : "+str(author[14]))
        st.text("Total Ratings : "+str(ratings[14]))
        st.text("Average Rating : "+str(round(avg_ratings[14],1)))
    with col1:
        st.text("16"[0:2])
        st.image(image[15])        
        st.text("Title : "+str(book_name[15]))
        st.text("Author : "+str(author[15]))
        st.text("Total Ratings : "+str(ratings[15]))
        st.text("Average Rating : "+str(round(avg_ratings[15],1)))
    with col1:
        st.text("17"[0:2])
        st.image(image[16])        
        st.text("Title : "+str(book_name[16]))
        st.text("Author : "+str(author[16]))
        st.text("Total Ratings : "+str(ratings[16]))
        st.text("Average Rating : "+str(round(avg_ratings[16],1)))    
    with col1:
        st.text("18"[0:2])
        st.image(image[17])        
        st.text("Title : "+str(book_name[17]))
        st.text("Author : "+str(author[17]))
        st.text("Total Ratings : "+str(ratings[17]))
        st.text("Average Rating : "+str(round(avg_ratings[17],1)))    
    with col1:
        st.text("19"[0:2])
        st.image(image[18])        
        st.text("Title : "+str(book_name[18]))
        st.text("Author : "+str(author[18]))
        st.text("Total Ratings : "+str(ratings[18]))
        st.text("Average Rating : "+str(round(avg_ratings[18],1)))    
    with col1:
        st.text("20"[0:2])
        st.image(image[19])        
        st.text("Title : "+str(book_name[19]))
        st.text("Author : "+str(author[19]))
        st.text("Total Ratings : "+str(ratings[19]))
        st.text("Average Rating : "+str(round(avg_ratings[19],1)))
    with col1:
        st.text("21"[0:2])
        st.image(image[20])        
        st.text("Title : "+str(book_name[20]))
        st.text("Author : "+str(author[20]))
        st.text("Total Ratings : "+str(ratings[20]))
        st.text("Average Rating : "+str(round(avg_ratings[20],1)))
    with col1:
        st.text("22"[0:2])
        st.image(image[21])        
        st.text("Title : "+str(book_name[21]))
        st.text("Author : "+str(author[21]))
        st.text("Total Ratings : "+str(ratings[21]))
        st.text("Average Rating : "+str(round(avg_ratings[21],1)))    
    with col1:
        st.text("23"[0:2])
        st.image(image[22])        
        st.text("Title : "+str(book_name[22]))
        st.text("Author : "+str(author[22]))
        st.text("Total Ratings : "+str(ratings[22]))
        st.text("Average Rating : "+str(round(avg_ratings[22],1)))
    with col1:
        st.text("24"[0:2])
        st.image(image[23])        
        st.text("Title : "+str(book_name[23]))
        st.text("Author : "+str(author[23]))
        st.text("Total Ratings : "+str(ratings[23]))
        st.text("Average Rating : "+str(round(avg_ratings[23],1)))
    with col1:
        st.text("25"[0:2])
        st.image(image[24])        
        st.text("Title : "+str(book_name[24]))
        st.text("Author : "+str(author[24]))
        st.text("Total Ratings : "+str(ratings[24]))
        st.text("Average Rating : "+str(round(avg_ratings[24],1)))
    with col1:
        st.text("26"[0:2])
        st.image(image[25])        
        st.text("Title : "+str(book_name[25]))
        st.text("Author : "+str(author[25]))
        st.text("Total Ratings : "+str(ratings[25]))
        st.text("Average Rating : "+str(round(avg_ratings[25],1)))
    with col1:
        st.text("27"[0:2])
        st.image(image[26])        
        st.text("Title : "+str(book_name[26]))
        st.text("Author : "+str(author[26]))
        st.text("Total Ratings : "+str(ratings[26]))
        st.text("Average Rating : "+str(round(avg_ratings[26],1)))    
    with col1:
        st.text("28"[0:2])
        st.image(image[27])        
        st.text("Title : "+str(book_name[27]))
        st.text("Author : "+str(author[27]))
        st.text("Total Ratings : "+str(ratings[27]))
        st.text("Average Rating : "+str(round(avg_ratings[27],1)))    
    with col1:
        st.text("29"[0:2])
        st.image(image[28])        
        st.text("Title : "+str(book_name[28]))
        st.text("Author : "+str(author[28]))
        st.text("Total Ratings : "+str(ratings[28]))
        st.text("Average Rating : "+str(round(avg_ratings[28],1)))    
    with col1:
        st.text("30"[0:2])
        st.image(image[29])        
        st.text("Title : "+str(book_name[29]))
        st.text("Author : "+str(author[29]))
        st.text("Total Ratings : "+str(ratings[29]))
        st.text("Average Rating : "+str(round(avg_ratings[29],1)))
    with col1:
        st.text("31"[0:2])
        st.image(image[30])        
        st.text("Title : "+str(book_name[30]))
        st.text("Author : "+str(author[30]))
        st.text("Total Ratings : "+str(ratings[30]))
        st.text("Average Rating : "+str(round(avg_ratings[30],1)))
    with col1:
        st.text("32"[0:2])
        st.image(image[31])        
        st.text("Title : "+str(book_name[31]))
        st.text("Author : "+str(author[31]))
        st.text("Total Ratings : "+str(ratings[31]))
        st.text("Average Rating : "+str(round(avg_ratings[31],1)))    
    with col1:
        st.text("33"[0:2])
        st.image(image[32])        
        st.text("Title : "+str(book_name[32]))
        st.text("Author : "+str(author[32]))
        st.text("Total Ratings : "+str(ratings[32]))
        st.text("Average Rating : "+str(round(avg_ratings[32],1)))
    with col1:
        st.text("34"[0:2])
        st.image(image[33])        
        st.text("Title : "+str(book_name[33]))
        st.text("Author : "+str(author[33]))
        st.text("Total Ratings : "+str(ratings[33]))
        st.text("Average Rating : "+str(round(avg_ratings[33],1)))
    with col1:
        st.text("35"[0:2])
        st.image(image[34])        
        st.text("Title : "+str(book_name[34]))
        st.text("Author : "+str(author[34]))
        st.text("Total Ratings : "+str(ratings[34]))
        st.text("Average Rating : "+str(round(avg_ratings[34],1)))
    with col1:
        st.text("36"[0:2])
        st.image(image[35])        
        st.text("Title : "+str(book_name[35]))
        st.text("Author : "+str(author[35]))
        st.text("Total Ratings : "+str(ratings[35]))
        st.text("Average Rating : "+str(round(avg_ratings[35],1)))
    with col1:
        st.text("37"[0:2])
        st.image(image[36])        
        st.text("Title : "+str(book_name[36]))
        st.text("Author : "+str(author[36]))
        st.text("Total Ratings : "+str(ratings[36]))
        st.text("Average Rating : "+str(round(avg_ratings[36],1)))    
    with col1:
        st.text("38"[0:2])
        st.image(image[37])        
        st.text("Title : "+str(book_name[37]))
        st.text("Author : "+str(author[37]))
        st.text("Total Ratings : "+str(ratings[37]))
        st.text("Average Rating : "+str(round(avg_ratings[37],1)))    
    with col1:
        st.text("39"[0:2])
        st.image(image[38])        
        st.text("Title : "+str(book_name[38]))
        st.text("Author : "+str(author[38]))
        st.text("Total Ratings : "+str(ratings[38]))
        st.text("Average Rating : "+str(round(avg_ratings[38],1)))    
    with col1:
        st.text("40"[0:2])
        st.image(image[39])        
        st.text("Title : "+str(book_name[39]))
        st.text("Author : "+str(author[39]))
        st.text("Total Ratings : "+str(ratings[39]))
        st.text("Average Rating : "+str(round(avg_ratings[39],1)))    
    with col1:
        st.text("41"[0:2])
        st.image(image[40])        
        st.text("Title : "+str(book_name[40]))
        st.text("Author : "+str(author[40]))
        st.text("Total Ratings : "+str(ratings[40]))
        st.text("Average Rating : "+str(round(avg_ratings[40],1)))
    with col1:
        st.text("42"[0:2])
        st.image(image[41])        
        st.text("Title : "+str(book_name[41]))
        st.text("Author : "+str(author[41]))
        st.text("Total Ratings : "+str(ratings[41]))
        st.text("Average Rating : "+str(round(avg_ratings[41],1)))    
    with col1:
        st.text("43"[0:2])
        st.image(image[42])        
        st.text("Title : "+str(book_name[42]))
        st.text("Author : "+str(author[42]))
        st.text("Total Ratings : "+str(ratings[42]))
        st.text("Average Rating : "+str(round(avg_ratings[42],1)))
    with col1:
        st.text("44"[0:2])
        st.image(image[43])        
        st.text("Title : "+str(book_name[43]))
        st.text("Author : "+str(author[43]))
        st.text("Total Ratings : "+str(ratings[43]))
        st.text("Average Rating : "+str(round(avg_ratings[43],1)))
    with col1:
        st.text("45"[0:2])
        st.image(image[44])        
        st.text("Title : "+str(book_name[44]))
        st.text("Author : "+str(author[44]))
        st.text("Total Ratings : "+str(ratings[44]))
        st.text("Average Rating : "+str(round(avg_ratings[44],1)))
    with col1:
        st.text("46"[0:2])
        st.image(image[45])        
        st.text("Title : "+str(book_name[45]))
        st.text("Author : "+str(author[45]))
        st.text("Total Ratings : "+str(ratings[45]))
        st.text("Average Rating : "+str(round(avg_ratings[45],1)))
    with col1:
        st.text("47"[0:2])
        st.image(image[46])        
        st.text("Title : "+str(book_name[46]))
        st.text("Author : "+str(author[46]))
        st.text("Total Ratings : "+str(ratings[46]))
        st.text("Average Rating : "+str(round(avg_ratings[46],1)))    
    with col1:
        st.text("48"[0:2])
        st.image(image[47])        
        st.text("Title : "+str(book_name[47]))
        st.text("Author : "+str(author[47]))
        st.text("Total Ratings : "+str(ratings[47]))
        st.text("Average Rating : "+str(round(avg_ratings[47],1)))    
    with col1:
        st.text("49"[0:2])
        st.image(image[48])        
        st.text("Title : "+str(book_name[48]))
        st.text("Author : "+str(author[48]))
        st.text("Total Ratings : "+str(ratings[48]))
        st.text("Average Rating : "+str(round(avg_ratings[48],1)))    
    with col1:
        st.text("50"[0:2])
        st.image(image[49])        
        st.text("Title : "+str(book_name[49]))
        st.text("Author : "+str(author[49]))
        st.text("Total Ratings : "+str(ratings[49]))
        st.text("Average Rating : "+str(round(avg_ratings[49],1)))


def recommend_book(book):
    
    index = np.where(pivot_table.index==book)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])),key=lambda x:x[1],reverse=True)[1:6]
    
    data = []    
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pivot_table.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        
        data.append(item)        
    return data


st.sidebar.title("Recommend Books")        
selected_book = st.sidebar.selectbox("Enter Book Name",books_list)
if st.sidebar.button('Recommend'):
    boooks = recommend_book(selected_book)
    col1,col2 = st.columns(2)
    
    with col1:
       st.text("1"[0]) 
       st.image(boooks[0][2])
       st.text("Title : "+str(boooks[0][0]))
       st.text("Author : "+str(boooks[0][1]))
       
    with col1:
       st.text("2"[0])
       st.image(boooks[1][2])
       st.text("Title : "+str(boooks[1][0]))
       st.text("Author : "+str(boooks[1][1]))
      
    with col1:
       st.text("3"[0])
       st.image(boooks[2][2])
       st.text("Title : "+str(boooks[2][0]))
       st.text("Author : "+str(boooks[2][1]))
       
    with col1:
       st.text("4"[0]) 
       st.image(boooks[3][2])
       st.text("Title : "+str(boooks[3][0]))
       st.text("Author : "+str(boooks[3][1]))
       
    with col1:
       st.text("5"[0])
       st.image(boooks[4][2])
       st.text("Title : "+str(boooks[4][0]))
       st.text("Author : "+str(boooks[4][1]))
      
    


   
   

