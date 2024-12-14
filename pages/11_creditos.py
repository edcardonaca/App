import numpy as numpy
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import utilidades as util
from PIL import Image
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error, r2_score

# Configuración Apertura
util.Config_pag()

# Llamar el menú
util.generarMenu()

# Redimensionar los logotipos
logo1 = util.resize_image("media/logos/logo1.png", 2.00)
logo2 = util.resize_image("media/logos/logo2.png", 2.00)
logo3 = util.resize_image("media/logos/logo3.png", 2.00)

util.Logos_y_Titulo(logo1, logo2, logo3)

############################################################################################
st.write("---")
st.write("### Fuentes de Información:")
st.write("""
         #### Ministerio de Tecnologías de la Información y las Comunicaciones\n
         https://www.mintic.gov.co/portal/inicio/""")
st.write("""
         #### TALENTO TECH\n
         https://talentotech.gov.co/portal/""")
st.write("""
         #### SINERGOX\n
        https://sinergox.xm.com.co/Paginas/Home.aspx
        """)
st.write("""
         #### NOAA National Oceanic and Atmospheric Administration\n
        https://www.noaa.gov/""")
st.write("---")
