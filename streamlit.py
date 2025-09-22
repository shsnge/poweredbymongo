# streamlit_app.py
import streamlit as st
from agent import memory_agent

st.title("Talk to Agent")
st.write("This app demonstrates a conversational agent.")

# Session state for messages
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

# Input box
user_input = st.text_input("Ask a question:")

if st.button("Submit") and user_input:
    # Add user message
    st.session_state['messages'].append({"role": "user", "content": user_input})
    with st.spinner("Agent is thinking..."):
        response = memory_agent.invoke(
            {"messages": st.session_state['messages']},
            config={"configurable": {"thread_id": "user123"}}
        )
    # ✅ FIX: AIMessage object not subscriptable → use `.get("messages")` properly
    # The response is a dict with 'messages' key
    messages_list = response.get("messages", [])
    if messages_list:
        agent_message = messages_list[-1].content  # get last message content
        st.session_state['messages'].append({"role": "assistant", "content": agent_message})

# Display conversation history
for msg in st.session_state['messages']:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**Agent:** {msg['content']}")
