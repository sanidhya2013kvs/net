import streamlit as st

import av
from streamlit_javascript import st_javascript


import os

from st_click_detector import click_detector
import streamlit.components.v1 as components
# Define your javascript
my_js = """
var x = document.getElementById("myAudio");
x.autoplay = true;
x.load();
alert("This is an alert dialog box");  
"""
#components.html("""<script>
#var x = document.getElementById("audio");
#x.autoplay = true;
#x.load();
#alert("This is an alert dialog box");
#</script>   
# """
#)
my_html = f"<script>{my_js}</script>"
#html(my_html)


path = "./songs"

dir = os.listdir(path)
sort=dir.sort()
diri=[]

for titler in dir:
  diri.append(titler)


return_value = st_javascript("""await fetch("https://reqres.in/api/products/3").then(function(response) {
    return response.json();
}) """)

st.markdown(f"Return value was: {return_value}")
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
