from google import genai


def chatbot(text):

    client = genai.Client(api_key="AIzaSyAViOIXp_p23bZfM476fOYe7xyc284zrVc")

    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=text
    )
    return response.text

print('salom, qalesan?')