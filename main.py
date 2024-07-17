import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from openai import OpenAI
from custom_persona import custom_persona
from create_feedback_html import create_feedback_html

load_dotenv()

client = OpenAI()

app = Flask(__name__)
    
def check_this_submition(new_test):
    result = send_test_to_openai(new_test)
    return result

def send_test_to_openai(new_test):
    completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": custom_persona},
        {"role": "user", "content": new_test}
    ])
    
    response = completion.choices[0].message.content
    return response

def get_answer_from_multi_chouse_question(question):
    answer = ""
    value_id = question["value"][0]
    for option in question["options"]:
        if option["id"] == value_id:
            answer = option["text"]
            break
    if answer == "":
        print("Error: get_answer_from_multi_chouse_question didn't found the option")
        
    return answer

def parse_tally_submission_to_string(questions):
    test_string = ""
    for question in questions:
        
        # Add question to our test_string
        question_text = question["label"]
        test_string += "שאלה: " + question_text + "\n"

        # Add answer to our test_string
        question_type = question["type"]
        if question_type == "TEXTAREA":
            answer = question["value"]
        elif question_type == "MULTIPLE_CHOICE":
            test_string += "שאלה אמריקאית, פה יש רק אופציה של נכון או לא נכון"
            answer = get_answer_from_multi_chouse_question(question)
        else:
            print("New to add support in code for this question_type: " + question_type)
        test_string += "תשובה: " + answer + "\n\n"
    
    return test_string

@app.route('/tally_new_submission', methods=['POST'])
def tally_new_submission():
    created_at = request.json["data"]["createdAt"]
    questions = request.json["data"]["fields"]

    test_string = parse_tally_submission_to_string(questions)
    print(test_string + "\n\n\n\n")
    test_feedback = check_this_submition(test_string)
    print(test_feedback)
    create_feedback_html(test_feedback, "feedback.html")
    
    # Add your custom processing logic here
    return jsonify({'status': 'success'}), 200
    

if __name__ == "__main__":
    app.run(port=5000)
