import streamlit as st
import tempfile
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
from dotenv import load_dotenv


def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with CSV #️⃣")
    st.header("Chat with CSV #️⃣")
    user_csv = st.file_uploader("Upload CSV File", type="csv")
    if user_csv is not None:
        with tempfile.NamedTemporaryFile(mode='w+b', suffix=".csv") as f:
            f.write(user_csv.getvalue())
            llm = OpenAI(temperature=0)
            user_input = st.text_input("Ask a question:")
            f.flush()
            agent = create_csv_agent(llm, f.name, verbose=False)
            if user_input:
                response = agent.run(user_input)
                st.write(response)


if __name__ == "__main__":
    main()
