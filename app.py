import streamlit as st


def main():
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
    st.title('CHAT NEXUS v1.0')
    st.caption('Developed by: Yi Xian (yx-elite)')
    st.write('✨ Advanced Features: WebSearch, Image Generation')
    
    # Allow prompt input
    prompt_placeholder = st.form('chat-form')
    with prompt_placeholder:
        st.markdown("**User's Prompt**")
        cols = st.columns((6,1))
        user_prompt = cols[0].text_input(
            "User's Prompt", 
            value='',
            max_chars=100,
            placeholder='Ask me anything... (Press Enter to Submit)',
            key='input',
            label_visibility='collapsed'
        )
        submit_btn = cols[1].form_submit_button(
            'Submit',
            type='primary',
            on_click=lambda: on_click_callback(user_prompt),
        )

def on_click_callback(user_prompt):
    # Process user's prompt
    if 'search' in user_prompt:
        with st.spinner('Nexus AI is now searching the web...'):
            st.write('Searching...')
    
if __name__ == '__main__':
    main()
