import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load your key
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("❌ Error: API Key not found in .env file")
else:
    print(f"✅ Found API Key: {api_key[:5]}...")
    
    # Configure the library
    genai.configure(api_key=api_key)

    print("\n🔍 Asking Google for available models...")
    try:
        # List all models your key can access
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(f"   • {m.name}")
    except Exception as e:
        print(f"\n❌ Error connecting to Google:\n{e}")