from flask import Flask, request, render_template, jsonify, send_file, redirect, url_for, flash, session, abort

app = Flask(__name__)




CV_STEPS = {
    'personal_info': {
        'name': 'What is your full name?',
        'email': 'What is your email address?',
        'phone': 'What is your phone number?',
        'location': 'Where are you located?',
        'summary': 'Brief professional summary (2-3 sentences)?',
        'languages': 'Languages you speak? (e.g., English - Native)',
        'hobbies': 'Hobbies and interests?'
    },
    'experience': {
        'experience': 'List your work experiences. For each: Company, Title, Start Date, End Date, Description, Achievements.'
    },
    'education': {
        'education': 'List your education. For each: Institution, Degree, Field, Start Date, End Date.'
    },
    'skills': {
        'technical': 'Technical skills? (e.g., Python, JavaScript)',
        'soft': 'Soft skills? (e.g., Leadership, Communication)',
        'certifications': 'Certifications (if any)?'
    }
}

user_data = {}
step_keys = list(CV_STEPS.keys())
step_index = 0
question_index = 0



@app.route('/chat', methods=['POST'])
def chat():
    global step_index, question_index, user_data

    answer = request.json.get('answer')
    current_step = step_keys[step_index]
    current_questions = list(CV_STEPS[current_step].keys())
    key = current_questions[question_index]
    user_data[key] = answer

    question_index += 1

    if question_index >= len(current_questions):
        step_index += 1
        question_index = 0

    if step_index >= len(step_keys):
        return jsonify({'done': True})

    return jsonify({'question': get_next_question()})


def get_next_question():
    current_step = step_keys[step_index]
    current_questions = list(CV_STEPS[current_step].keys())
    return CV_STEPS[current_step][current_questions[question_index]]

if __name__ == '__main__':
    app.run(debug=True)
