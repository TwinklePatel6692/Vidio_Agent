import streamlit as st
from main import run_pipeline
from core.rag_engine import ask_question

with open("assets/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.set_page_config(
    page_title="AI Video Assistant",
    page_icon="🎥",
    layout="wide"
)

st.title("🎥 AI Video Assistant")
st.markdown("### Summarize Videos & Chat with Content")

# Session state
if "result" not in st.session_state:
    st.session_state.result = None

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")

    source = st.text_input(
        "YouTube URL or File Path"
    )

    language = st.selectbox(
        "Language",
        ["english", "hinglish"]
    )

    process_btn = st.button("🚀 Process Video")

# Main processing
if process_btn:

    with st.spinner("⏳ Processing Video..."):
        result = run_pipeline(source, language)

        st.session_state.result = result

    st.success("✅ Processing Complete!")

# Display Results
if st.session_state.result:

    result = st.session_state.result

    st.header("📌 Title")
    st.info(result["title"])

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "Summary",
            "Actions",
            "Decisions",
            "Questions"
        ]
    )

    with tab1:
        st.write(result["summary"])

    with tab2:
        st.write(result["action_items"])

    with tab3:
        st.write(result["key_decisions"])

    with tab4:
        st.write(result["open_questions"])

    st.divider()

    st.header("💬 Chat with Video")

    question = st.text_input(
        "Ask a question about the video"
    )

    if st.button("Ask"):

        with st.spinner("Thinking..."):

            answer = ask_question(
                result["rag_chain"],
                question
            )

        st.success(answer)