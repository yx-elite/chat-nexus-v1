import streamlit as st
from app_function import chat_connection


def main():
    # Load custom css
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    # Set app info
    st.title('CHAT NEXUS v1.0')
    st.caption('Developed by: Yi Xian (yx-elite)')
    st.write('✨ Features: GPT AI Chatbot & Websearch')

    # Initialize placeholders for prompt and chat
    prompt_placeholder = st.form('chat-form')
    chat_placeholder = st.container()

    with prompt_placeholder:
        # Section header
        st.markdown("**Set Maximum Token & input User's Prompt to start chatting**")
        max_token = st.slider('Maximum Tokens', min_value=100, max_value=1000, value=500)

        # User prompt input field
        cols = st.columns((6, 1))
        user_prompt = cols[0].text_input(
            'User Prompt',
            value='',
            max_chars=100,
            placeholder='Ask me anything... (Press Enter to Submit)',
            label_visibility='collapsed'
        )
        submit_clicked = cols[1].form_submit_button('Submit', type='primary')

    # Handle actions upon button clicked    
    if submit_clicked:
        handle_button_click(max_token, user_prompt, chat_placeholder)


# Button click function
def handle_button_click(max_token, user_prompt, chat_placeholder):
    with chat_placeholder:
        if 'search' in user_prompt:
            with st.spinner('Nexus AI is now searching the web...'):
                st.write('Searching...')
                print('Searching')
        
        else:
            try:
                with st.spinner('Nexus AI is thinking...'):
                    response = chat_connection(user_prompt, max_token)
                    st.write(response)
                    # Display results in terminal
                    print(f'User \t\t: {user_prompt}')
                    print(f'Assistant \t: {response}\n\n')
                
                st.success("Answer is generated successfully")
            
            except Exception as e:
                # Error handling
                st.error(f"An error occurred: {str(e)}")



if __name__ == '__main__':
    main()
