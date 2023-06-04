import openai

openai.api_key = 'YOUR_API_KEY'


def chat_with_openai(message):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=message,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None,
        timeout=10
    )

    if response.choices:
        return response.choices[0].text.strip()
    else:
        return "Sorry, I couldn't generate a response."


while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break

    response = chat_with_openai(user_input)
    print("AI: " + response)

