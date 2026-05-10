import streamlit as st


def style_background_home():

    st.markdown("""
        <style>

            /* Main Background */
            .stApp {
                background: #5865F2 !important;
                color-scheme: light !important;
            }

            /* Column Card Design */
            .stApp div[data-testid="stColumn"]{
                background-color:#E0E3FF !important;
                padding:2.5rem !important;
                border-radius: 5rem !important;
            }

            /* Force Streamlit Right Menu White */
            [data-testid="stToolbar"] {
                background-color: white !important;
            }

            /* Popup Menu */
            [data-testid="stPopover"] > div {
                background: white !important;
                color: black !important;
                border-radius: 18px !important;
            }

            /* Popup Buttons */
            [data-testid="stPopover"] button {
                background: white !important;
                color: black !important;
                border: none !important;
            }

            /* All popup text */
            [data-testid="stPopover"] * {
                color: black !important;
            }

        </style>
    """, unsafe_allow_html=True)


def style_background_dashboard():

    st.markdown("""
        <style>

            .stApp {
                background: #E0E3FF !important;
                color-scheme: light !important;
            }

            /* Force Streamlit Right Menu White */
            [data-testid="stToolbar"] {
                background-color: white !important;
            }

            /* Popup Menu */
            [data-testid="stPopover"] > div {
                background: white !important;
                color: black !important;
                border-radius: 18px !important;
            }

            /* Popup Buttons */
            [data-testid="stPopover"] button {
                background: white !important;
                color: black !important;
                border: none !important;
            }

            /* All popup text */
            [data-testid="stPopover"] * {
                color: black !important;
            }

        </style>
    """, unsafe_allow_html=True)



def style_base_layout():

    st.markdown("""
        <style>

        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

        /* Hide Streamlit Header/Footer */

        #MainMenu {
            visibility: hidden;
        }

        footer {
            visibility: hidden;
        }

        header {
            visibility: hidden;
        }

        .block-container {
            padding-top: 1.5rem !important;
        }

        /* Fonts */

        h1 {
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 3.5rem !important;
            line-height: 1.1 !important;
            margin-bottom: 0rem !important;
        }

        h2 {
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 2rem !important;
            line-height: 0.9 !important;
            margin-bottom: 0rem !important;
        }

        h3, h4, p {
            font-family: 'Outfit', sans-serif !important;
        }

        /* Default Buttons */

        button {
            border-radius: 1.5rem !important;
            background-color: #5865F2 !important;
            color: white !important;
            padding: 10px 20px !important;
            border: none !important;
            transition: transform 0.25s ease-in-out !important;
        }

        button[kind="secondary"]{
            background-color: #EB459E !important;
        }

        button[kind="tertiary"]{
            background-color: black !important;
        }

        button:hover{
            transform: scale(1.05);
        }

        </style>
    """, unsafe_allow_html=True)