import openai


class ChatGPT:

    PROMPT_PREFIX = (
        "Below is the description of GitHub pull requests," +
        "Do not return me any English sentence." +
        "Summarize the following description into a list of points and translate the summary into simplified Chinese. "
        )

    def __init__(self, api_key, model="text-davinci-003", max_token=1024):
        self.api_key = api_key
        self.model = model
        self.set_credentials()
        self.max_token = max_token

    def set_credentials(self):
        openai.api_key = self.api_key

    def summarize(self, summary):
        # Set up the model and prompt
        prompt = f"{self.PROMPT_PREFIX}\n{summary}"

        # Generate a response
        completion = openai.Completion.create(
            engine=self.model,
            prompt=prompt,
            max_tokens=self.max_token,
            n=1,
            stop=None,
            temperature=0.5,
        )
        response = completion.choices[0].text
        return response
