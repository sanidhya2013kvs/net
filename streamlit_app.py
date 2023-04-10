import streamlit as st

import av

import pyshorteners

import os

from st_click_detector import click_detector
import streamlit.components.v1 as components
st.set_page_config(page_title="Geet_sagar",page_icon="🧊")
image="https://github.com/sanidhya2013kvs/net/blob/main/images/ram%20ram%20jai%20raja%20ram.jpg?raw=true"


# Define your javascript
with open('./name_songs.txt') as f:
    content = f.readlines()
with open('./images.txt') as fp:
    strimages=fp.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
#st.write(content)
dict=[]
dict2=[]
for i in content:
    dict.append(i)
dict.sort()
for i in strimages:
    dict2.append(i)
dict2.sort()
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
str_reg="  "
str_start='"""  '
for i in range(len(dict)):
  str_1="<a href='#' "
  str_2= "id="
  str_3=str(i)
  str_4="><img src="
  str_5=dict2[i]
  str_5=str_5[:(len(str_5)-1)]
  type_tiny = pyshorteners.Shortener()
  str_5=short_url = type_tiny.isgd.short(str_5)
  str_6="></a>    "
  final_str=str_1+str_2+str_3+str_4+str_5+str_6
  print(final_str)
  str_reg=str_reg+final_str


str_end='   """'
content=str_reg
print(content)
clicked = click_detector(content)
  
if clicked:
  #placeholder = st.empty()
  print("hello")
  print(clicked)
  i=int(clicked)
  list=diri[i]
  CWF=os.path.join(path,list)
  lost=dict[i]
  str_5=dict2[i]
  str_5=str_5[:(len(str_5)-1)]
  type_tiny = pyshorteners.Shortener()
  str_5=short_url = type_tiny.isgd.short(str_5)
  
  strimg="<img src='"+str_5+"' width=100% height=100%>"
 
  a='<audio controls autoplay><source src="'
  type_tiny = pyshorteners.Shortener()
  short_url = type_tiny.isgd.short(dict[i])  
  w=short_url
  r='"'
  wet='   type="audio/ogg"></audio>'
  string=a+w+r+wet
  #st.markdown(html_string,unsafe_allow_html=True)
  #st.write(string)
  #name=audio_file.name
  qwert=(os.path.splitext(list)[0])
  #st.sidebar.audio(audio_bytes, format='audio/ogg')

  st.sidebar.subheader(diri[i])

  components.html(html_string)
  string=f'{string}'
  with st.empty():
    with st.sidebar:
        my_html = f"{string}"
        my_html2=f"{strimg}"
        components.html(my_html2)
        stringspace="<br>"                                  "</br>"
        
        stringspace=f"{stringspace}"
        components.html(stringspace)
        components.html(my_html)
        

