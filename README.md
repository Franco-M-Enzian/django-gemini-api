# Django Gemini API Test
Gemini API Keyを取得し、プロンプトを事前に指定することで
runserver後のページにGeminiからの回答が表示される。

プロンプトを変更したい場合、geminiTest/views.pyのgenerate_content関数の引数を変更する。

## SetUp
```
python -m venv venv
```

```
source venv/Scripts/activate
```

```
pip install django
```

```
pip install google-generativeai
```

```
export API_KEY="your gemini api key"
```

```
python manage.py migrate
```

```
python manage.py runserver
```
