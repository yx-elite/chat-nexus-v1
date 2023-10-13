import streamlit as st
import app_function as af

def main():
    # Load custom css
    #with open('style.css') as f:
    #    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    # Set app info
    st.title('CHAT NEXUS v1.0')
    st.caption('Developed by: Yi Xian (yx-elite)')
    st.write('✨ Features: GPT AI Chatbot & Websearch')

    # Initialize placeholders for prompt and chat
    prompt_placeholder = st.form('chat-form')
    chat_placeholder = st.container()

    with prompt_placeholder:
        # Section header
        st.markdown("**User's Prompt**")
        
        # Set maximum token & temperature
        max_token = st.slider(
            'Maximum Tokens', 
            min_value=100, 
            max_value=1000, 
            value=500, 
            step=100,
            help="The maximum number of tokens to generate in the chat completion. The total length of input tokens \
                and generated tokens is limited by the model's context length. (Default = 500)"
        )
        temperature = st.slider(
            'Temperature',
            min_value=0.0,
            max_value=2.0,
            value=0.8,
            step=0.1,
            format='%.1f',
            help="Lower values like 0.2 will make the output more focused and deterministic, while higher values \
                like 0.8 will make the output more random. We generally recommend altering this or \"Top-p\" but not both. \
                (Default: 0.8)"
        )

        # User prompt input field
        cols_2 = st.columns((6, 1))
        user_prompt = cols_2[0].text_input(
            'User Prompt',
            value='',
            max_chars=100,
            placeholder='Ask me anything... (Press Enter to Submit)',
            label_visibility='collapsed'
        )
        submit_clicked = cols_2[1].form_submit_button('Submit', type='primary')


    # Handle actions upon button clicked    
    if submit_clicked:
        handle_button_click(user_prompt, chat_placeholder, max_token, temperature)


# Button click function
def handle_button_click(user_prompt, chat_placeholder, max_token, temperature):
    with chat_placeholder:
        if 'search' in user_prompt:
            with st.spinner('Nexus AI is now searching the web...'):
                st.write('Searching...')
                print('Searching')
        
        else:
            try:
                with st.spinner('Nexus AI is thinking...'):
                    response = af.chat_connection(user_prompt, max_token, temperature)
                    msg = af.chat_message()
                    st.write(msg)
                    # Display results in terminal
                    prompt_tokens = af.get_prompt_tokens(response)
                    print("Prompt Tokens:", prompt_tokens)
                    print(f'User \t\t: {user_prompt}')
                    print(f'Assistant \t: {response}\n\n')
                
                st.success("Answer is generated successfully")
            
            except Exception as e:
                # Error handling
                st.error(f"An error occurred: {str(e)}")



if __name__ == '__main__':
    main()
