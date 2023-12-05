import streamlit as st
from streamlit_option_menu import option_menu

import cartography
import HOME
import slider
import splitmap
import attribut
import popup
import requetteAttributaire
import requetteSpaciale
import COGSlider
import COGsplitMap
import Timelapse

st.set_page_config(
    page_title="Application",
)

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        # app = st.sidebar(
        with st.sidebar:
            app = option_menu(
                menu_title='Main-Menu',
                options=['cartography', 'HOME', 'slider', 'Timelapse', 'splitmap', 'attribut', 'popup',
                         'requetteAttributaire', 'requetteSpaciale', 'COGSlider', 'COGsplitMap'],
                icons=['bi bi-globe-europe-africa', 'house-fill', 'bi bi-sliders', 'bi bi-watch', '"bi bi-forward','bi bi-pin-angle-fill','bi bi-chat-fill','bi bi-geo-alt','bi-geo-fill','bi bi-check-square','bi bi-arrow-left-right'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px",
                                 "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                }
            )

        # Custom CSS to set the background color of the entire page
        st.markdown(
            """
            <style>
                body {
                    background-color: black;
                    color: white;
                }
            </style>
            """,
            unsafe_allow_html=True
        )

        if app == "cartography":
            cartography.app()
        if app == "HOME":
            HOME.app()
        if app == "slider":
            slider.main()
        if app == "Timelapse":
            Timelapse.main()
        if app == "splitmap":
            splitmap.main()
        if app == "attribut":
            attribut.app()
        if app == "popup":
            popup.app()
        if app == "requetteAttributaire":
            requetteAttributaire.app()
        if app == "requetteSpaciale":
            requetteSpaciale.app()
        if app == "COGSlider":
            COGSlider.main()
        if app == "COGsplitMap":
            COGsplitMap.main()

MultiApp().run()
