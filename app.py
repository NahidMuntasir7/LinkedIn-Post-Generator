# Import libraries
import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv


# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


# Initialize Gemini LLM (via LangChain)
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", 
    temperature=0.7,
    api_key=GOOGLE_API_KEY,
)


# Prompt Template
prompt = PromptTemplate(
    input_variables=["topic", "language"],
    template="""
    You are a professional LinkedIn content creator.

    Write a {language} LinkedIn post about the topic: "{topic}".

    Guidelines:
    - Make it engaging, structured, and professional.
    - Use 2–4 short paragraphs.
    - Begin with a hook or unique insight.
    - Maintain a friendly, professional tone.
    - Avoid hashtags unless truly relevant.

    Return only the post content.
    """
)


# Create the chain
linkedin_post_chain = prompt | llm  


# Streamlit UI
st.set_page_config(page_title="LinkedIn Post Generator", page_icon="🤖", layout="centered")

st.title("🤖 LinkedIn Post Generator")
st.write("Generate professional LinkedIn posts  in a variety of languages using AI.")

topic = st.text_input("💡 Enter the topic of your LinkedIn post", placeholder="e.g., Future of AI in Healthcare, Remote Work Productivity Tips, etc.")
language = st.selectbox("🌐 Choose the language",  ["English", "Bengali", "Spanish", "French", "German", "Arabic", "Japanese", "Hindi", "Urdu", "Chinese"])


# Generate button
if st.button("Generate LinkedIn Post"):
    if not topic.strip():
        st.warning("⚠️ Please enter a topic first.")
    else:
        with st.spinner("Generating your LinkedIn post..."):
            try:
                response = linkedin_post_chain.invoke({"topic": topic, "language": language})
                st.session_state["linkedin_post"] = response.content.strip()
                st.success("✅ Post Generated Successfully!")
            except Exception as e:
                st.error(f"Error: {e}")

# Display generated post
if "linkedin_post" in st.session_state:
    st.markdown("##### 📝 Your LinkedIn Post:")
    st.write(st.session_state["linkedin_post"])

    st.download_button(
        label="📥 Download as Text File",
        data=st.session_state["linkedin_post"],
        file_name="linkedin_post.txt",
        mime="text/plain",
    )
st.markdown("---")
st.caption("Built using LangChain, Streamlit, and GitHub Models API")


