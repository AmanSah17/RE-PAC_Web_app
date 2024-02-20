import streamlit as st 

st.set_page_config(page_title="Home",
                   layout='wide',
                   page_icon='./images/Re_pack_logo.jpeg')

st.title("Packaging Material Brand Classification Web - Application")
st.caption('Welcome to RE-PAC an Advanced Web Application designed Which can process the Images and Texts present on Packaging Materials')


#Company Logo
st.image('./images/Re_pack_logo.jpeg',use_column_width=True)

# Content
st.markdown("""
### Our Application Scan and  detects objects (TEXT, LOGO,BARCODE, And Material Images) Present on the Packaging Material
- Our web app utilizes state-of-the-art Convolutional Neural Network(CNN) to accurately detect various objects Present on the Packaging Material. 
            By leveraging deep learning techniques, we can identify objects with high precision, enabling us to analyze images effectively.
### Text and Object Information Extraction

-Once the objects are detected, we extracts text(s), barcode(s), and logo(s) from the images. This information is crucial for further analysis and understanding of the image content. By capturing relevant data, we ensure comprehensive processing of image information.
""")

st.image('./images/text info.png',use_column_width=True)

st.markdown("""
### Brand Recognition using power of CNN & NLP

The extracted text(s), barcode(s), and Brand - Logo(s)  which are Identified By ,
            state of the art YOLO-V5 (CNN-Architecture) and Backed by Natural Language Processing(NLP) Models to classify Real time objects using Machine Vision.""")

st.image("./images/processed.jpg",use_column_width=True)           
#st.image("./images/card_bar_2.png",use_column_width=True)

st.markdown("""
- [Click here for App](/YOLO_for_image/)  

""")