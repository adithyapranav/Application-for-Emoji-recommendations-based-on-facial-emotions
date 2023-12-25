import streamlit as st
from PIL import Image
import numpy as np
import cv2
#import pickle
from ensemble_main import *
from io import BytesIO
import win32clipboard
#from zeroshot import *
st.set_page_config(
	page_title="Emotion Detector",
	page_icon="",
	layout="centered",
)
def send_to_clipboard(image):
    output = BytesIO()
    image.convert('RGB').save(output, 'BMP')
    data = output.getvalue()[14:]
    output.close()

    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()
st.title("WEB APPLICATION FOR EMOJI RECOMMENDATIONS BASED ON FACIAL EMOTIONS")
picture = st.camera_input("Take a picture")
#if picture:
	#print(type(picture))'''
if picture is not None:
	img = Image.open(picture)
	img=img.save("image.jpg")
	val=img_processing(cv2.imread("image.jpg"))
	#st.write(val,type(val))
	#st.image(picture)	
	#val=emotion_pred("image.jpg")
	st.write(val[0])
	if(val is not None):
		if(val[0]=="Happy"):
			img1 = Image.open("1.jpeg")
			but1=st.button("Copy below Emoji",key=1)
			st.image(img1)
			if but1:
				send_to_clipboard(img1)
				st.write("Image Copied to clipboard")
			img2 = Image.open("2.jpeg")
			but2=st.button("Copy below Emoji",key=2)
			st.image(img2)
			if but2:
				send_to_clipboard(img2)
				st.write("Image Copied to clipboard")
			img3 = Image.open("3.jpeg")
			but3=st.button("Copy below Emoji",key=3)
			st.image(img3)
			if but3:
				send_to_clipboard(img3)
				st.write("Image Copied to clipboard")
			img4 = Image.open("4.jpeg")
			but4=st.button("Copy below Emoji",key=4)
			st.image(img4)
			if but4:
				send_to_clipboard(img4)
				st.write("Image Copied to clipboard")
			img5 = Image.open("5.jpeg")
			but5=st.button("Copy below Emoji",key=5)
			st.image(img5)
			if but5:
				send_to_clipboard(img5)
				st.write("Image Copied to clipboard")
		elif(val[0]=="Surprise"):
			img1 = Image.open("6.jpeg")
			but6=st.button("Copy below Emoji",key=6)
			st.image(img1)
			if but6:
				send_to_clipboard(img1)
				st.write("Image Copied to clipboard")
			img2 = Image.open("7.jpeg")
			but7=st.button("Copy below Emoji",key=7)
			st.image(img2)
			if but7:
				send_to_clipboard(img2)
				st.write("Image Copied to clipboard")
			img3 = Image.open("8.jpeg")
			but8=st.button("Copy below Emoji",key=8)
			st.image(img3)
			if but8:
				send_to_clipboard(img3)
				st.write("Image Copied to clipboard")
			img4 = Image.open("9.jpeg")
			but9=st.button("Copy below Emoji",key=9)
			st.image(img4)
			if but9:
				send_to_clipboard(img4)
				st.write("Image Copied to clipboard")
			img5 = Image.open("10.jpeg")
			but10=st.button("Copy below Emoji",key=10)
			st.image(img5)
			if but10:
				send_to_clipboard(img5)
				st.write("Image Copied to clipboard")
		elif(val[0]=="Angry"):
			img1 = Image.open("11.jpeg")
			but11=st.button("Copy below Emoji",key=11)
			st.image(img1)
			if but11:
				send_to_clipboard(img1)
				st.write("Image Copied to clipboard")
			img2 = Image.open("12.jpeg")
			but12=st.button("Copy below Emoji",key=12)
			st.image(img2)
			if but12:
				send_to_clipboard(img2)
				st.write("Image Copied to clipboard")
			img3 = Image.open("13.jpeg")
			but13=st.button("Copy below Emoji",key=13)
			st.image(img3)
			if but13:
				send_to_clipboard(img3)
				st.write("Image Copied to clipboard")
			img4 = Image.open("14.jpeg")
			but14=st.button("Copy below Emoji",key=14)
			st.image(img4)
			if but14:
				send_to_clipboard(img4)
				st.write("Image Copied to clipboard")
			img5 = Image.open("15.jpeg")
			but15=st.button("Copy below Emoji",key=15)
			st.image(img5)
			if but15:
				send_to_clipboard(img5)
				st.write("Image Copied to clipboard")
		elif(val[0]=="Sad"):
			img1 = Image.open("16.jpeg")
			but16=st.button("Copy below Emoji",key=16)
			st.image(img1)
			if but16:
				send_to_clipboard(img1)
				st.write("Image Copied to clipboard")
			img2= Image.open("17.jpeg")
			but17=st.button("Copy below Emoji",key=17)
			st.image(img2)
			if but17:
				send_to_clipboard(img2)
				st.write("Image Copied to clipboard")
			img3 = Image.open("18.jpeg")
			but18=st.button("Copy below Emoji",key=18)
			st.image(img3)
			if but18:
				send_to_clipboard(img3)
				st.write("Image Copied to clipboard")
			img4 = Image.open("19.jpeg")
			but19=st.button("Copy below Emoji",key=19)
			st.image(img4)
			if but19:
				send_to_clipboard(img4)
				st.write("Image Copied to clipboard")
			img5 = Image.open("20.jpeg")
			but20=st.button("Copy below Emoji",key=20)
			st.image(img5)
			if but20:
				send_to_clipboard(img5)
				st.write("Image Copied to clipboard")
		elif(val[0]=="Fear"):
			img1 = Image.open("21.jpeg")
			but21=st.button("Copy below Emoji",key=21)
			st.image(img1)
			if but21:
				send_to_clipboard(img1)
				st.write("Image Copied to clipboard")
			img2 = Image.open("22.jpeg")
			but22=st.button("Copy below Emoji",key=22)
			st.image(img2)
			if but22:
				send_to_clipboard(img2)
				st.write("Image Copied to clipboard")
			img3 = Image.open("23.jpeg")
			but23=st.button("Copy below Emoji",key=23)
			st.image(img3)
			if but23:
				send_to_clipboard(img3)
				st.write("Image Copied to clipboard")
			img4 = Image.open("24.jpeg")
			but24=st.button("Copy below Emoji",key=24)
			st.image(img4)
			if but24:
				send_to_clipboard(img4)
				st.write("Image Copied to clipboard")
			img5 = Image.open("25.jpeg")
			but25=st.button("Copy below Emoji",key=25)
			st.image(img5)
			if but25:
				send_to_clipboard(img5)
				st.write("Image Copied to clipboard")
		elif(val[0]=="Disgust"):
			img1 = Image.open("26.jpeg")
			but26=st.button("Copy below Emoji",key=26)
			st.image(img1)
			if but26:
				send_to_clipboard(img1)
				st.write("Image Copied to clipboard")
			img2 = Image.open("27.jpeg")
			but27=st.button("Copy below Emoji",key=27)
			st.image(img2)
			if but27:
				send_to_clipboard(img2)
				st.write("Image Copied to clipboard")
			img3 = Image.open("28.jpeg")
			but28=st.button("Copy below Emoji",key=28)
			st.image(img3)
			if but28:
				send_to_clipboard(img3)
				st.write("Image Copied to clipboard")
			img4 = Image.open("29.jpeg")
			but29=st.button("Copy below Emoji",key=29)
			st.image(img4)
			if but29:
				send_to_clipboard(img4)
				st.write("Image Copied to clipboard")
			img5 = Image.open("30.jpeg")
			but30=st.button("Copy below Emoji",key=30)
			st.image(img5)
			if but30:
				send_to_clipboard(img5)
				st.write("Image Copied to clipboard")
		else:
			img1 = Image.open("31.jpeg")
			but31=st.button("Copy below Emoji",key=31)
			st.image(img1)
			if but31:
				send_to_clipboard(img1)
				st.write("Image Copied to clipboard")
			img2 = Image.open("32.jpeg")
			but32=st.button("Copy below Emoji",key=32)
			st.image(img2)
			if but32:
				send_to_clipboard(img2)
				st.write("Image Copied to clipboard")
			img3 = Image.open("33.jpeg")
			but33=st.button("Copy below Emoji",key=33)
			st.image(img3)
			if but33:
				send_to_clipboard(img3)
				st.write("Image Copied to clipboard")
			img4 = Image.open("34.jpeg")
			but34=st.button("Copy below Emoji",key=34)
			st.image(img4)
			if but34:
				send_to_clipboard(img4)
				st.write("Image Copied to clipboard")
			img5 = Image.open("35.jpeg")
			but35=st.button("Copy below Emoji",key=35)
			st.image(img5)
			if but35:
				send_to_clipboard(img5)
				st.write("Image Copied to clipboard")
	#img_array = np.array(img)
	#st.write(type(img_array))
	#st.write(img_array.shape)