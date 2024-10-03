
import os

import openai


openai.api_key = os.environ('OPENAI_API_KEY')

def get_mood_from_text(paragraph):
    prompt = f"Analyze the following paragraph and determine the mood (Happy, Sad, Energetic, Calm):\n\n{paragraph}\n\nMood:"

    response = openai.Completion.create(
        engine="gpt-4",
        prompt=prompt,
        max_tokens=10,
        n=1,
        stop=None,
        temperature=0.5,
    )

    mood = response['choices'][0]['text'].strip()
    return mood


paragraph = "I feel so excited today! Everything just seems to be going perfectly."
mood = get_mood_from_text(paragraph)
print(f"Identified mood: {mood}")
