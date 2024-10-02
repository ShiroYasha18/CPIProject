# Example using OpenAI API (if using GPT-3/4)
import os

import openai

# Set your OpenAI API key
openai.api_key = os.environ('OPENAI_API_KEY')

def get_mood_from_text(paragraph):
    prompt = f"Analyze the following paragraph and determine the mood (Happy, Sad, Energetic, Calm):\n\n{paragraph}\n\nMood:"

    response = openai.Completion.create(
        engine="text-davinci-003",  # Or "gpt-4" if using GPT-4
        prompt=prompt,
        max_tokens=10,
        n=1,
        stop=None,
        temperature=0.5,
    )

    mood = response['choices'][0]['text'].strip()
    return mood

# Example paragraph
paragraph = "I feel so excited today! Everything just seems to be going perfectly."
mood = get_mood_from_text(paragraph)
print(f"Identified mood: {mood}")
