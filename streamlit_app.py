import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
import cv2
import numpy as np
import os
from PIL import Image
from st_click_detector import click_detector
from streamlit.components.v1 import html

# Define your javascript
my_js = """
var x = document.getElementById("myAudio");
x.autoplay = true;
x.load();
"""

my_html = f"<script>{my_js}</script>"



path = "/content/sample_data/Untitled Folder 1"

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


class VideoProcessor:

    def recv(self, frame):
      image = frame.to_ndarray(format="bgr24")




       
      return av.VideoFrame.from_ndarray(image, format="bgr24")

# file name with extension
#file_name = os.path.basename('/content/sample_data/Jubin Nautiyal- Mere Ghar Ram Aaye Hain.mp3')

# file name without extension
#qwert=(os.path.splitext(file_name)[0])



#content = """ <a href='#' id='Img1'><img src='httpanidhya2013kvs/images/blob/main/1.jpg?raw=true' 
#></a>   """
#clicked = click_detector(content)
#if clicked=='Img1':
  #st.sidebar.image("/content/sample_data/1.jpg")
  #st.sidebar.subheader(qwert)
 # st.sidebar.audio(audio_bytes, format='audio/ogg')


   
ctx=webrtc_streamer(
      key="example",
      video_processor_factory=VideoProcessor,
      rtc_configuration={  
          "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]

              })
audio_file = open('/content/sample_data/Untitled Folder 1/Jubin Nautiyal- Mere Ghar Ram Aaye Hain.mp3', 'rb')
audio_bytes = audio_file.read()

html_string = """
            <audio controls autoplay>
              
            </audio>
            """


st.markdown(html_string, unsafe_allow_html=True)
