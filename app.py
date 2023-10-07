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
    user_prompt = st.text_input(
        "User's Prompt", 
        value='',
        max_char=100,
        placeholder='Ask me anything... (Shift + Enter = Line Break)',
        label_visibility='visible',
    )
    
if __name__ == '__main__':
    main()