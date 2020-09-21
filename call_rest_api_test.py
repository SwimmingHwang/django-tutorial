import requests

target = "http://localhost:8000/questions"
response = requests.get(url=target)

# 응답 데이터가 JSON형식이므로 바로 파이썬 객체로 변환
data = response.json()

questions = []

for question in data:
    # print('q',question)
    questions.append(question['fields']['question_text'])
print(questions)