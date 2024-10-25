from django.http import HttpResponse
from config.settings import API_KEY
import google.generativeai as genai


def index(request):
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel("gemini-pro")
    # response = model.generate_content("Djangoの特徴を教えて。")
    response = model.generate_content("何か文字を一文字だけ出力して。")
    return HttpResponse(response.text)
