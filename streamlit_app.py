import streamlit as st

import av



import os

from st_click_detector import click_detector
import streamlit.components.v1 as components
# Define your javascript
with open('./name_songs.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
st.write(content)
dict=[]
for i in content:
    dict.append(i)
dict.sort()
#st.write(dict)

html_string=''' 
<script type="text/javascript">document.getElementById("audio").play();</script> 
'''
#)
#my_html = f"<script>{my_js}</script>"
#html(my_html)


path = "./songs"

dir = os.listdir(path)
sort=dir.sort()
diri=[]

for titler in dir:
  diri.append(titler)

audio='<audio controls autoplay><source src="GFG.ogg" type="audio/ogg"></audio>'
       
   
#return_value = st_javascript(""" var x = document.getElementById("audio");
#x.autoplay = true;
#x.load();
#alert("This is an alert dialog box");  
#}) """)

st.markdown('<script> var x = document.getElementById("audio"); x.autoplay = true; x.load();alert("This is an alert dialog box"); </script>'  ,unsafe_allow_html=True)
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
  lost=dict[i]
  
  
  a='<audio controls autoplay><source src='
  w=lost
  wet='type="audio/ogg"></audio>'
  string=a+w+wet
  #st.markdown(html_string,unsafe_allow_html=True)
  #st.write(string)
  #name=audio_file.name
  qwert=(os.path.splitext(list)[0])
  #st.sidebar.audio(audio_bytes, format='audio/ogg')

  #st.sidebar.subheader(a)

  components.html(html_string)
  string=f'{string}'
  st.sidebar.markdown(string,unsafe_allow_html=True)
 


