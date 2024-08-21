from flask import Flask, request, render_template
import os
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculator')
def calculator():
    return render_template('calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    value = float(request.form['value'])
    conversion = request.form['conversion']
    scale = int(request.form['scale'])
    
    if conversion == 'cgpa_to_percentage':
        if scale == 10:
            result = value * 9.5
        elif scale == 5:
            result = value * 18.5
    elif conversion == 'percentage_to_cgpa':
        if scale == 10:
            result = value / 9.5
        elif scale == 5:
            result = value / 18.5
    else:
        result = None
    
    return render_template('result.html', result=result)


@app.route('/info')
def info():
    article_id = request.args.get('article')  # Add this line
    article_content = get_article_content(article_id)
    return render_template('info.html', article_content=article_content, article_id=article_id)  # Add article_id here

def get_article_content(article_id):
    articles = {
        '1': {
            'title': 'Understanding CGPA Calculations',
            'content': 'Learn the ins and outs of CGPA calculations and how they impact your overall academic performance.'
        },
        '2': {
            'title': 'Tips for Improving Your CGPA',
            'content': 'Discover effective strategies to boost your CGPA and maximize your academic success.'
        },
        '3': {
            'title': 'CGPA vs Percentage: What\'s the Difference?',
            'content': 'Understand the difference between CGPA and percentage, and how to convert between the two.'
        },
        '4': {
            'title': 'How to Calculate CGPA for Semester Exams',
            'content': 'Learn how to calculate your CGPA for semester exams and understand the importance of regular assessments.'
        },
        '5': {
            'title': 'Common Mistakes to Avoid in CGPA Calculations',
            'content': 'Avoid common mistakes that can affect your CGPA calculations and ensure accurate results.'
        },
        '6': {
            'title': 'Importance of Maintaining a Good CGPA',
            'content': 'Understand the importance of maintaining a good CGPA and how it can impact your future academic and professional prospects.'
        }
    }
    return articles.get(article_id, {'title': 'Article Not Found', 'content': 'The article you are looking for does not exist.'})


@app.route('/articles')
def articles():
    return render_template('articles.html')

@app.route('/article/cgpa_to_percentage')
def article_cgpa_to_percentage():
    return render_template('article_cgpa_to_percentage.html')

@app.route('/article/calculate_points')
def article_calculate_points():
    return render_template('article_calculate_points.html')

@app.route('/article/grading_system')
def article_grading_system():
    return render_template('article_grading_system.html')

@app.route('/article/why_convert')
def article_why_convert():
    return render_template('article_why_convert.html')

@app.route('/article/advantages')
def article_advantages():
    return render_template('article_advantages.html')

@app.route('/article/university_conversion')
def article_university_conversion():
    return render_template('article_university_conversion.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# Add a new route for handling the contact form submission and rendering
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']

    # Save data to CSV
    save_to_csv(name, email, subject, message)

    return render_template('contact_data_receive.html', name=name, email=email, subject=subject, message=message)

def save_to_csv(name, email, subject, message):
    with open('contact_data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, email, subject, message])

# if __name__ == '__main__':
#     app.run(debug=True)

# Some changes
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
