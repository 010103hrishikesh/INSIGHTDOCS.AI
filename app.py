import streamlit as st
import requests
import os

# PAGE CONFIG
st.set_page_config(
    page_title="INSIGHTDOCS.AI",
    layout="centered"
)

# CSS
st.markdown("""
<style>
.title {
    text-align: center;
    font-size: 42px;
    font-weight: 700;
    margin-top: 20px;
}

.subtitle {
    text-align: center;
    color: gray;
    font-size: 17px;
    margin-bottom: 40px;
}

.response-box {
    padding: 20px;
    background-color: #F8F9FA;
    border-radius: 10px;
    border: 1px solid #DDDDDD;
}
</style>
""", unsafe_allow_html=True)

# HEADER
st.markdown(
    """
    <div class="title">INSIGHTDOCS.AI</div>
    <div class="subtitle">
    Upload documents and interact with them using intelligent AI retrieval
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# FILE UPLOAD
st.subheader("Upload Document")

uploaded_file = st.file_uploader(
    "",
    type=["pdf"]
)

if uploaded_file is not None:

    os.makedirs("data", exist_ok=True)

    with open("data/uploaded.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    with st.spinner("Processing document..."):

        response = requests.post(
            "http://127.0.0.1:8000/upload"
        )

        if response.status_code == 200:
            st.success("Document ready")

        else:
            st.error("Unable to process document")

st.divider()

# QUESTION INPUT
st.subheader("Ask Questions")

question = st.text_input(
    "",
    placeholder="Ask anything about your document..."
)

if st.button("Generate Response", use_container_width=True):

    if question == "":
        st.warning("Enter a question first")

    else:
        with st.spinner("Generating response..."):

            response = requests.post(
                "http://127.0.0.1:8000/ask",
                json={"question": question}
            )

            result = response.json()

            st.divider()
            st.subheader("AI Response")

            st.markdown(
                '<div class="response-box">',
                unsafe_allow_html=True
            )

            if "answer" in result:
                st.write(result["answer"])
            else:
                st.write(result)

            st.markdown(
                '</div>',
                unsafe_allow_html=True
            )
