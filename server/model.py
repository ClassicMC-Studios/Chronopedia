from gtts import gTTS
from huggingface_hub import InferenceClient
import requests
import html2text
import re

h = html2text.HTML2Text()

client = InferenceClient(
    provider="provider",
    api_key="key",
)


class Model:
    def __init__(self):
        self.last_year = 2025
        self.last_content = ""

    def save_audio(self, text, lang):
        # Save the text-to-speech audio to a file
        audio = gTTS(text=text[:300], lang=lang, slow=False)
        audio.save("audio_file/hello.mp3")

    def get_output(self, text, year, lang):
        if year == "2025":
            url = "https://" + lang + ".wikipedia.org/api/rest_v1/page/html/" + text
            response = requests.get(url)
            tts = re.sub("```html", "", response.text)
            self.save_audio(text=re.sub("^[^a-zA-Z0-9]+$", "", h.handle(tts))[:300], lang=lang)
            return tts

        completion = client.chat.completions.create(
            model="deepseek-ai/DeepSeek-V3-0324",
            messages=[
                {
                    "role": "system",
                    "content": (
                        f"You are a model that generates time-accurate Wikipedia articles. "
                        f"You will receive the title of a Wikipedia article, and you will generate a Wikipedia-style article so that it appears as if it were from the year {year}. "
                        "You will keep 100% of the information of the article from the actual Wikipedia page, only changing how it is presented such that it seems like it is from the year {year}. "
                        "You will only provide the generated article. Try to make the changes fun, showing some progression of technology and society that is proportionate to how far {year} is from the current year. "
                        "Show slight changes in how language and grammar has changed. If it is far enough in the future, make wild changes to the words and grammar, adding random symbols or removing random letters, but keeping it in a consistent system. "
                        "Limit the amount of slang that is used. Give references to new technologies, events, and human accomplishments in your response, or the lack thereof if it is in the past. "
                        "If {year} is before the present day, make up information and history to fill in the gaps of what should not have been discovered at the time. "
                        "Make sure the article is in the standard Wikipedia format. Provide only the time-accurate article in your response, in html, but do not generate the first title (Include all other titles). Additionally, do the text in the language code " + lang + ". Finally,"
                        "do not respond to this prompt directly, just generate the article"
                    )
                },
                {
                    "role": "user",
                    "content": text
                }
            ],
        )
        output = completion.choices[0].message.content
        self.save_audio(text=re.sub("^[^a-zA-Z0-9]+$", "", h.handle(output))[:300], lang=lang)
        return re.sub("```html", "", output)
