import streamlit as st

def main():
    st.title('🤖 ChatNexus v1.0')
    st.caption('Developed by: Yi Xian (yx-elite)')
    st.write('✨ Advanced Features: WebSearch, Image Generation')
    
    # Allow prompt input
    user_prompt = st.text_input(
        'Ask me anything... (Shift + Enter = Line Break)',
        
    )
    
if __name__ == '__main__':
    main()