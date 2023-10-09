import streamlit as st

def main():
    # Load custom css
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    # Set app info
    st.title('CHAT NEXUS v1.0')
    st.caption('Developed by: Yi Xian (yx-elite)')
    st.write('✨ Advanced Features: WebSearch, Image Generation')

    # Initialize placeholders for prompt and chat
    prompt_placeholder = st.form('chat-form')
    chat_placeholder = st.container()

    with prompt_placeholder:
        # Section header
        st.markdown("**User's Prompt**")

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
        handle_button_click(user_prompt, chat_placeholder)


# Button click function
def handle_button_click(user_prompt, chat_placeholder):
    with chat_placeholder:
        if 'search' in user_prompt:
            with st.spinner('Nexus AI is now searching the web...'):
                st.write('Searching...')
                print('Searching')

if __name__ == '__main__':
    main()
