import openai
import os
import time

# Set your OpenAI API key as an environment variable
os.environ['OPENAI_API_KEY'] = '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'

# Initialize the openai.api object with your API key
openai.api_key = os.environ['OPENAI_API_KEY']

# Set the model and parameters for the conversation
model_engine = "text-davinci-002"
prompt = input("Enter the prompt: ")
temperature = 0.7
max_tokens = 150

# Generate a response from ChatGPT
response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    temperature=temperature,
    max_tokens=max_tokens,
)

# Create a filename based on the current time
filename = f"output_{time.strftime('%Y%m%d-%H%M%S')}.txt"

# Write the response to a file
with open(filename, 'w') as f:
    f.write(response.choices[0].text.strip())

# Print the filename to the console
print(f"Output saved to {filename}")
