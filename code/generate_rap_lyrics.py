# Python file to generate rap lyrics given [context of rap, duration of rap and number of chorus and verse]

from loguru import logger
import openai
import creds

# Replace 'your-api-key' with your actual OpenAI API key
logger.info("API Creds are Initialized...")
api_key = creds.OPENAI_API_KEY

# Initialize the OpenAI API client
openai.api_key = api_key

# Function to generate text using GPT-3
def generate_text(max_tokens=200):

    logger.info("Hitting API.....")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use the gpt-3.5-turbo engine for text generation
        messages = [
            {"role": "system", "content": "You are a rap-god lyricist. You are gonna help me generate rap lyrics. Please obey my rules. 4 stanza for chorus and 4 stanza for verse" }, 
            {"role": "user", "content" : "Generate me a 1 chorus [4 stanza], 1 verse [4 stanza] Rap Lyrics given some context. The context are ['sad', 'victory', 'rainy']"}
        ],
        max_tokens=max_tokens,
        n = 1,
        stop = ['chorus'],  # You can specify stop sequences if needed
        temperature = 0.8  # Adjust the temperature for controlling randomness
    )
    
    return response['choices'][0]['message']['content']

# Example usage

generated_text = generate_text()
print(generated_text)