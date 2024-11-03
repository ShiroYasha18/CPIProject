import openai
import os

openai.api_key = os.environ["OPENAI_API_KEY"]

def get_mood_from_text(paragraph):
    # Define a chat-like conversation with the model
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "You are an AI that helps determine the mood of a given paragraph."
            },
            {
                "role": "user",
                "content": f"Analyze the following paragraph and determine the mood strictly from (Happy, Sad, Energetic, Calm) \n\n{paragraph}"
            }
        ],
        max_tokens=10,
        n=1,
        stop=None,
        temperature=0.5,
    )

    mood = response['choices'][0]['message']['content'].strip()
    return mood

# Example paragraph
paragraph = ("After a long day at the office, I feel "
             "completely drained. My head is pounding from all the endless meetings, and i"
             "t feels like I barely accomplished anything despite all the effort. "
             "The workload just never seems to end, and every task feels like it drags on forever. "
             "I’m so frustrated—there’s this constant pressure to do more, and it’s exhausting. All I want is to escape this feeling and find something that can lift my mood and help me unwind, but right now, I’m too worn out to even think about it..")
mood = get_mood_from_text(paragraph)
print(f"Identified mood: {mood}")
