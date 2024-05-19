#https://www.linkedin.com/jobs/view/3929775175

import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

#Function to get response from Llama 2 model

def getLlamaResponse(input_text, no_words, blog_style):
    #calling the Llama 2 model

    llm=CTransformers(model="D:/Rohan/ML/Models/llama-2-7b-chat.ggmlv3.q8_0.bin",
                      model_type="llama",
                      config={'max_new_tokens':256,
                              'temperature':0.01})
    
    #prompt template
    template="""
    Write a blog for {blog_style} job profile for the topic {input_text} within {no_words} words.
    """
    prompt=PromptTemplate(input_variables=["blog_style", "input_text", "no_words"],
                          template=template)
    #generating the response from the model
    response=llm(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))
    print(response)
    return response


                    

st.set_page_config(page_title="Generate Blogs",
                   page_icon="🤖",
                   layout="centered",
                   initial_sidebar_state="collapsed")

st.header("Generate Blogs 🤖")

input_text=st.text_input("Enter the blog topic: ")

#taking input - number of words and blog style
col1,col2=st.columns([5,5])
with col1:
    no_words=st.text_input("No of words")

with col2:
    blog_style=st.selectbox("Writing the blog for",
                            ("Researcher", "Data Scientist", "Common People"), index=0)

submit=st.button("Generate")

if submit:
    st.write(getLlamaResponse(input_text, no_words, blog_style))

