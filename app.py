import streamlit as st


def main():
    '''
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    '''
    
    st.title('CHAT NEXUS v 1.0')
    st.caption('Developed by: Yi Xian (yx-elite)')
    st.write('✨ Advanced Features: WebSearch, Image Generation')
    
    # Allow prompt input
    with st.form("User's Prompt"):
        user_prompt = st.text_input(
            "User's Prompt", 
            value='',
            max_chars=100,
            placeholder='Ask me anything... (Shift + Enter = Line Break)',
            label_visibility='visible',
        )
        btn_result = st.form_submit_button('Generate')
        
        # Determine output path
        if btn_result:
            if 'search' in user_prompt:
                with st.spinner('Nexus AI is now searching the web...'):
                    st.write('Searching...')
                    print("Searching")
    
if __name__ == '__main__':
    main()