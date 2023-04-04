import streamlit as st

import av
import cv2

import os

from st_click_detector import click_detector
from streamlit.components.v1 import html

# Define your javascript
my_js = """
var x = document.getElementById("myAudio");
x.autoplay = true;
x.load();
"""

my_html = f"<script>{my_js}</script>"



path = "./songs"

dir = os.listdir(path)
sort=dir.sort()
diri=[]

for titler in dir:
  diri.append(titler)



content = """ <a href='#' id=0><img src=https://github.com/sanidhya2013kvs/images/blob/main/1.jpg?raw=true></a>
<a href='#' id=1><img src=https://github.com/sanidhya2013kvs/images/blob/main/b2.jpg?raw=true></a>
<a href='#' id=2><img src=https://github.com/sanidhya2013kvs/images/blob/main/b3.jpeg?raw=true></a>   """
clicked = click_detector(content)
  
if clicked:
  print("hello")
  print(clicked)
  i=int(clicked)
  list=diri[i]
  CWF=os.path.join(path,list)
  audio_file = open(CWF, 'rb')
  audio_bytes = audio_file.read()
  html_string = """
            <audio controls autoplay="true">
               <source src=CWFtype="audio/mp3">
            </audio>
            """
  html(my_html)

  st.sidebar.markdown(html_string, unsafe_allow_html=True)

  #name=audio_file.name
  qwert=(os.path.splitext(list)[0])
  st.sidebar.audio(audio_bytes, format='audio/ogg')
  st.sidebar.subheader(qwert)






html_string = """
            <audio controls autoplay>
              
            </audio>
            """


#st.markdown(html_string, unsafe_allow_html=True)
