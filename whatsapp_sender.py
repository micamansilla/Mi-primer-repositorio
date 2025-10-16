import streamlit as st
from twilio.rest import Client

st.title("💬 WhatsApp Message Sender")
st.subheader("Este es mi primer proyecto")
st.write("Send WhatsApp messages using Twilio")

# Configuration Section
with st.sidebar:
    st.header("⚙️ Twilio Configuration")
    
    twilio_account_sid = st.text_input(
        "Account SID",
        type="password",
        placeholder="Enter your Twilio Account SID",
        help="Get this from console.twilio.com"
    )
    
    twilio_auth_token = st.text_input(
        "Auth Token",
        type="password",
        placeholder="Enter your Twilio Auth Token",
        help="Get this from console.twilio.com"
    )
    
    st.markdown("---")
    
    if twilio_account_sid and twilio_auth_token:
        st.success("✅ Credentials configured")
    else:
        st.warning("⚠️ Please enter credentials")

# Main Message Section
st.subheader("📱 Send Message :)")

recipient_number = st.text_input(
    "Recipient WhatsApp Number",
    placeholder="+5493516760000",
    help="Include country code (e.g., +54 for AR)."
)

message_text = st.text_area(
    "Message",
    placeholder="Enter your WhatsApp message here...",
    height=150
)

if st.button("📤 Send WhatsApp Message", type="primary"):
    # Validate inputs
    if not twilio_account_sid or not twilio_auth_token:
        st.error("⚠️ Please configure Twilio credentials in the sidebar first!")
    elif not recipient_number or not message_text:
        st.error("⚠️ Please fill in both phone number and message!")
    elif not recipient_number.startswith("+"):
        st.error("⚠️ Phone number must include country code (e.g., +1)")
    else:
        try:
            # Initialize Twilio client
            client = Client(twilio_account_sid, twilio_auth_token)
            
            # Format recipient number for WhatsApp
            whatsapp_to = f"whatsapp:{recipient_number}"
            
            # Send message
            message = client.messages.create(
                body=message_text,
                from_='whatsapp:+14155238886',
                to=whatsapp_to
            )
            
            st.success(f"✅ WhatsApp message sent successfully!")
            
        except Exception as e:
            st.error(f"❌ Error sending message: {str(e)}")

# Instructions
with st.expander("ℹ️ Setup Instructions"):
    st.markdown("""
    ### Twilio WhatsApp Sandbox Setup:
    
    1. **Sign up for Twilio**: Visit [twilio.com/try-twilio](https://www.twilio.com/try-twilio)
    
    2. **Get your credentials**:
       - Go to [console.twilio.com](https://console.twilio.com)
       - Copy your **Account SID** and **Auth Token**
       - Enter them in the sidebar (left side)
    
    3. **Activate WhatsApp Sandbox**:
       - Go to [console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn](https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn)
       - Send the provided code (e.g., "join <your-code>") to **+1 415 523 8886** via WhatsApp
       - This connects your WhatsApp number to the Twilio sandbox
    
    ### Important Notes:
    - **Sandbox Limitation**: Recipients must also join your sandbox by sending the join code
    - **Testing**: Only works with numbers that have joined your sandbox
    - **Production**: For production use, you need to request a Twilio WhatsApp Business Account
    
    ### WhatsApp Sandbox Number:
    - Default: `whatsapp:+14155238886` (Twilio's WhatsApp Sandbox)
    - Recipients must join your sandbox first by texting your unique join code
    
    ### Running this script:
    ```bash
    # Install dependencies
    uv add streamlit twilio
    
    # Run the app
    streamlit run whatsapp_sender.py
    ```
    """)

st.markdown("---")
st.caption("Powered by Mica y Juli Twilio WhatsApp API | Built with Streamlit")