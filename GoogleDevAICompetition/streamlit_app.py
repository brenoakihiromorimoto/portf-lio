#Import Libraries
import streamlit as st
import pandas as pd
import numpy as np
import google.generativeai as genai
import json
import time
import re

#
if "options_sciences" not in st.session_state:
    st.session_state.options_sciences = "None"

if "options_industries" not in st.session_state:
    st.session_state.options_industries = "None"

if "solutions" not in st.session_state:
    st.session_state.solutions = "None"

def clean_text(text):
    # Remove special caracters to User could read more easly.
    text = re.sub(r'[^a-zA-Z0-9\s://.;-]', '', text)
    text = text.strip()
    return text

#Generate a strutured solution.
def generate_matrix_baseline(
        num_col=3, 
        num_rows=3, 
        product='Solar Panel', 
        sciences="None", 
        industry="None"
        ):
    
    genai.configure(api_key=API_KEY)

    # Using `response_mime_type` with `response_schema` requires a Gemini 1.5 Pro model
    model = genai.GenerativeModel(
      'gemini-1.5-pro'
    )

    prompt = f"""
    Generate {num_col} Critical Functions and {num_rows} Features for each Critical Function of {product} on {industry}.
    Adapt features of {sciences}. Maximum 3 words.
    Using this Python Dictionary schema:
      {{
        "Crtical Function 01": [List of Features 01],
        "Crtical Function 02": [List of Features 02],
        "Crtical Function 03": [List of Features 03],
        "Crtical Function 04": [List of Features 04],
        "Crtical Function 05": [List of Features 05]
      }}
      Important: the output needs to be in Python Dictionary format. Rename Critical Function with suggestions. Maximum 3 words per description.
    """

    response_prep_01 = model.generate_content(prompt)
    response_prep_02 = response_prep_01.text.strip().replace("\n", "").replace("python", "").replace("```", "")
    st.session_state['table'] = response_prep_02

def generate_solutions_baseline():
    genai.configure(api_key='AIzaSyDiQBWIfHTto65mCYu0EUxPhlBlfVxBp-I')

    # Using `response_mime_type` with `response_schema` requires a Gemini 1.5 Pro model
    model = genai.GenerativeModel(
      'gemini-1.5-pro'
    )

    prompt = f"""
    Generate 1 suggestion of solutions with data bellow.
    {st.session_state['table']}

    Important: you need to apply morphological analysis. Follow template bellow with maximum 50 words.

    Template of output:
    Problem: [Describe problem of somebody]
    Solution: [Title]
    How it works: [explain your morphological analysis. Maximum 150 words]
    References: [Get 3 references from Web to explain how it works. Maximum 10 words]
    - Reference 01:
    - Reference 02:
    - Reference 03:
    """

    response_prep_01 = model.generate_content(prompt)
    response_prep_02 = response_prep_01.text.strip().replace("\n", "").replace("python", "").replace("```", "")
    df_response = response_prep_02
    st.session_state['solutions'] = df_response

with st.sidebar:    
    st.session_state.options_science = st.multiselect(
    "Give me your research areas to adapt your product",
    ["Agricultural Technology (AgTech)", "Blockchain Technology", "Biotechnology", 
     "Biomedical Engineering", "Cybersecurity", "Climate Change and Sustainability", 
     "Genomics and Bioinformatics", "Nanotechnology", "Artificial Intelligence and Machine Learning", 
     "Quantum Computing", "Renewable Energy", "Environmental Science", 
     "Astrophysics and Space Exploration", "Materials Science", 
     "Neuroscience", "Robotics", "Pharmaceutical Sciences", "Human-Computer Interaction", 
     "Smart Cities and Urban Planning", "Energy Storage Technologies"]
    )

    st.session_state.options_industries = st.multiselect(
    "What industry is related to your product?",
    ["E-commerce", "Education Technology (EdTech)", "Tourism and Hospitality", "Fintech", "Supply Chain Management", 
     "Supply Chain Management", "Healthcare Management", "Marketing Technology (MarTech)", 
     "Human Resources Tech (HRTech)", "Real Estate Technology (PropTech)", 
     "Agriculture", "Food Tech", "Entertainment and Media", "Cybersecurity", "Insurance Technology (InsurTech)",
     "Gaming and eSports", "Waste Management", 'Fitness and Wellness']
    )

    def first_matrix():
        #Step 01: generate strutured reasoning.
        generate_matrix_baseline(
            num_col=5, 
            num_rows=5, 
            product=st.session_state.input,
            sciences=st.session_state.options_science, 
            industry=st.session_state.options_industries
            )
        #Step 02: generate a text with more meaningful solutions
        generate_solutions_baseline()

    input = st.text_input('Input any idea or theme, It will be adapted anyway:', 
                          key='input', placeholder='eg. Solar Energy')
    
    button_generate = st.button("Generate new solution", type="primary", on_click=first_matrix)

with st.container(border=True):
    solutions = st.session_state.solutions

    header = clean_text(solutions.split('Problem:')[1].split("How it works:")[0].split("Solution:")[0])
    #header = solutions

    subheader = clean_text(solutions.split('Problem:')[1].split("How it works:")[0].split("Solution:")[1])

    st.header("Problem: " + header, divider=True)
    st.subheader("Solution: " + subheader, divider=True)

    text = clean_text(solutions.split('Problem:')[1].split("How it works:")[1].split("- Reference 01:")[0])
    st.write(text)

    st.text("References:")

    references = [i.strip() for i in clean_text(solutions.split('- Reference 01:')[1]).split('- ') if i!=""]
    
    st.write(references[0])
    st.write(references[1].replace("Reference 02:", ""))
    st.write(references[2].replace("Reference 03:", ""))