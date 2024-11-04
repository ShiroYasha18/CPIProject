import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def get_mood_from_text(paragraph):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an AI that classifies the emotional tone of a given paragraph. "
                        "Your task is to analyze the provided text and select the mood that best describes it, "
                        "choosing strictly from: Happy, Sad, Energetic, or Calm. "
                        "Provide only one of these four options as your answer."
                    )
                },
                {
                    "role": "user",
                    "content": (
                        "Please analyze the following paragraph and determine the mood. "
                        "Only respond with one word, choosing from: Happy, Sad, Energetic, or Calm.\n\n"
                        f"{paragraph}"
                    )
                }
            ],
            max_tokens=15,
            n=1,
            temperature=0.3,  # Lower temperature to reduce randomness in responses
        )

        mood = response['choices'][0]['message']['content'].strip()

        # Ensure the response is one of the specified moods
        if mood in ["Happy", "Sad", "Energetic", "Calm"]:
            return mood
        else:
            return "Mood could not be determined. Please check the input text."

    except Exception as e:
        return f"An error occurred: {e}"


paragraph = (
    "After a long day at the office, I feel completely drained. My head is pounding from all the endless meetings, "
    "and it feels like I barely accomplished anything despite all the effort. The workload just never seems to end, "
    "and every task feels like it drags on forever. I’m so frustrated—there’s this constant pressure to do more, and "
    "it’s exhausting. All I want is to escape this feeling and find something that can lift my mood and help me unwind, "
    "but right now, I’m too worn out to even think about it."
)

mood = get_mood_from_text(paragraph)
print(f"Identified mood: {mood}")
