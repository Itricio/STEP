import streamlit as st
import random
from PIL import Image

header = st.container()
dataset = st.container()
features = st.container()

names = ['Antonio', 'José', 'Manuel', 'Francisco', 'David', 'Juan', 'José Antonio', 'Javier', 'Daniel', 'José Luis', 'Francisco Javier', 'Carlos', 'Jesús', 'Alejandro', 'Miguel', 'José Miguel', 'Rafael', 'Pedro', 'José María', 'Sergio',
'Fernando', 'Jorge', 'Alberto', 'Juan Carlos', 'Álvaro', 'Juan José', 'Adrián', 'Diego', 'Raúl', 'Juan Antonio', 'Iván', 'Enrique', 'Rúben', 'Ramón', 'Óscar', 'Vicente', 'Ándres', 'Juan Manuel', 'Joaquín', 'Santiago', 'Eduardo', 
'Víctor', 'Mario', 'Roberto', 'Jaime', 'Francisco José' ]
cursos = ['1', '2', '3', '4', '5', '6', '7', '8'] 
images = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg', '9.jpg', '10.jpg', '11.jpg', '12.jpg', '13.jpg', '14.jpg', '15.jpg', '16.jpg']
nameChoice = random.choice(names)
cursosChoice = random.choice(cursos)
imageChoice = random.choice(images)
image = Image.open("2.jpg")
resized_image = image.resize((round(image.size[0]*0.5), round(image.size[1]*0.5)))

with header:
    st.title("Identificación STEP")
    st.text("Nombre: " + nameChoice)
    st.text("Curso: " + cursosChoice + "° Básico")
    st.image(resized_image)