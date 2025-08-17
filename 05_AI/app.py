import json
import streamlit as st
from gemini_api import get_completion

st.set_page_config(page_title="Scientific Interest Tips", page_icon="🔬", layout="wide")

st.title("🔬 Scientific Interest Explorer")
st.write(
    "Enter your scientific interest and get tailored tips, key areas, projects, and considerations."
)

# Input
interest = st.text_input("🧪 What scientific interest do you want to explore?")

if st.button("Get Tips") and interest.strip():
    with st.spinner("Generating insights..."):
        try:
            response_list = get_completion(interest)
            response_json = eval(response_list)
            print(type(response_json[0]))
            response = response_json[0]
            # Description
            st.subheader("📖 Description")
            st.write(response.get("description", "No description available."))

            # Key Areas
            key_areas = response.get("key_areas", [])
            if key_areas:
                st.subheader("🔑 Key Areas")
                for item in key_areas:
                    with st.expander(item.get("area", "Unnamed Area")):
                        st.write(item.get("details", "No details provided."))

            # Example Projects
            example_projects = response.get("example_projects", [])
            if example_projects:
                st.subheader("🧩 Example Projects")
                for proj in example_projects:
                    st.markdown(f"- {proj}")

            # Important Considerations
            important_considerations = response.get("important_considerations", [])
            if important_considerations:
                st.subheader("⚠️ Important Considerations")
                for c in important_considerations:
                    st.markdown(f"- {c}")

        except Exception as e:
            st.error(f"⚠️ Error: {e}")
