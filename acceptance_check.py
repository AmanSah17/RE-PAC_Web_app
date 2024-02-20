import streamlit as st

def main():
    st.set_page_config(page_title="Check Symbols",
                       layout='wide',
                       page_icon='./images/check.jpg')

    st.title("Additional Checks for Accurate Predictions")
    st.markdown("Original  Vs  Processed Images")
    col1, col2 = st.columns(2)
    with col1:
        st.image("./images/resized_image.jpg", width=250)
    with col2:
        st.image("./images/g_map.png", width=250)
    
    st.markdown('<hr>', unsafe_allow_html=True)

    n1,n2,n3 = st.columns(3)
    with n1:
        st.image("./images/onm.jpeg", caption="Company/Logo info present", width=200)
    with n2:
        st.image("./images/process.gif", caption="Packaging Material Area within Acceptable Range", width=200)
    with n3:
        st.image("./images/process.gif", caption="Packaging material Shape Acceptance", width=200)


if __name__ == "__main__":
    main()
