import streamlit as st
import requests

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="INSIGHTDOCS AI",
    layout="centered"
)

# ---------- HEADER ----------
st.markdown(
    """
    <h1 style='text-align: center;'>INSIGHTDOCS.AI</h1>
    <p style='text-align: center; color: grey;'>
    Analyze, summarize and interact with documents intelligently
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# ---------- FILE UPLOAD ----------
st.subheader("Upload Document")

uploaded_file = st.file_uploader(
    "",
    type=["pdf"]
)

if uploaded_file is not None:

    with open("data/uploaded.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    try:
        with st.spinner("Processing document..."):

            response = requests.post(
                "http://127.0.0.1:8000/upload"
            )

            if response.status_code == 200:
                st.success("Document ready.")
            else:
                st.error("Unable to process document.")

    except Exception as e:
        st.error(f"Upload Error: {e}")

st.divider()

# ---------- QUESTION INPUT ----------
st.subheader("Ask Questions")

question = st.text_input(
    "",
    placeholder="What would you like to know about the document?"
)

# ---------- BUTTON ----------
if st.button("Analyze", use_container_width=True):

    if question == "":
        st.warning("Enter a question first.")

    else:
        try:
            with st.spinner("Generating response..."):

                response = requests.post(
                    "http://127.0.0.1:8000/ask",
                    json={"question": question}
                )

                result = response.json()

                st.divider()
                st.subheader("Response")

                if "answer" in result:
                    st.write(result["answer"])
                else:
                    st.write(result)

        except Exception as e:
            st.error(f"Question Error: {e}")