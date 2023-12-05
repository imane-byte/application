import streamlit as st

def app():
    
    # Home page content
    
    st.markdown("<h1 style='text-align: center;'>DASHBOARD</h1>", unsafe_allow_html=True)

    # Larger image with a caption

    row1_col1, row1_col2 = st.columns(2)
    
    with row1_col1:
        st.image("https://imane-byte.github.io/kkk/GIF/map3.gif")

    with row1_col2:
        st.image("https://imane-byte.github.io/kkk/GIF/map1.gif")
        # Some text content
    st.markdown("""
        <div style='text-align: center; font-size: 16px; font-weight: bold;'>
            Streamlit simplifie la création d'applications géospatiales interactives, 
            offrant une expérience conviviale pour explorer et analyser des données géographiques
        </div>
    """, unsafe_allow_html=True)

    # Additional styled text with separation
    st.markdown("""
        <div style='text-align: center; color: green; font-weight: bold; font-size: 20px;'>
            IMANE JAAFAR / KAOUTAR EL MOUH
        </div>
    """, unsafe_allow_html=True)





if __name__ == "__main__":
    app()
