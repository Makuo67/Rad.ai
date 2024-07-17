import streamlit as st
import os
from PIL import Image
import subprocess
import requests

# Define each page as a separate function


def main_page():
    st.title("Medical imaging analyzer")
    st.write("")
    # Add buttons for navigation
    # if st.button("Go to CT Scan Segment",key="button 1"):
    #     # st.session_state.page = "CT Scan Segment"
    #     st.switch_page("pages/unetr.py")

    if st.button("Go to Analyze Response", key="button 2"):
        # st.session_state.page = "Analyze Response"
        command = "python -m streamlit run app.py --server.port 8502"
        result = subprocess.run(command, shell=True,
                                capture_output=True, text=True)

    # Capture and display the output of the external script
        st.write("Output from the external script:")
        st.write(result.stdout)


if __name__ == "__main__":
    main_page()
