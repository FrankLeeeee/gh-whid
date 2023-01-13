import openai

def set_credentials(api_key):
    openai.api_key = api_key

def summarize(summary):
    # Set up the model and prompt
    model_engine = "text-davinci-003"
    prompt = f"Summarize the following in point form in Chinese. \n{summary}"

    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    response = completion.choices[0].text
    return response
