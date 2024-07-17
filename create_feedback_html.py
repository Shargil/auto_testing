import os

def create_feedback_html(feedback: str, output_file: str):
    # Parse the feedback string into sections
    sections = feedback.split('\n\n')
    
    # Initialize the HTML content
    html_content = """<!DOCTYPE html>
<html lang="he">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>משוב תלמיד</title>
    <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Nunito', sans-serif;
            background-color: #f7f9fc;
            color: #333;
            margin: 0;
            padding: 20px;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            direction: rtl;
        }
        .container {
            max-width: 800px;
            background: #ffffff;
            border-radius: 12px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            padding: 30px;
            margin: 20px;
        }
        .header {
            text-align: center;
            padding: 20px 0;
            background-color: #6c63ff;
            border-radius: 12px 12px 0 0;
            color: white;
            margin: -30px -30px 20px -30px;
        }
        .question {
            background: #f1f3f5;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 20px;
            border-left: 5px solid #6c63ff;
        }
        .score {
            font-size: 1.2em;
            font-weight: 600;
            color: #6c63ff;
            margin-bottom: 10px;
        }
        .feedback {
            font-size: 1em;
            line-height: 1.6;
        }
        .footer {
            text-align: center;
            padding: 20px;
            font-size: 0.9em;
            color: #666;
        }
        .footer a {
            color: #6c63ff;
            text-decoration: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>משוב מבחן</h1>
        </div>
"""

    # Process each section and add it to the HTML content
    for section in sections:
        if not section.strip():
            continue
        
        lines = section.split('\n')
        question = lines[0].strip()[:-1]
        score = lines[1].strip()
        feedback_text = '\n'.join(lines[2:]).strip()

        html_content += f"""
        <div class="question">
            <div class="score">{question}</div>
            <div class="score">{score}</div>
            <div class="feedback">{feedback_text}</div>
        </div>
        """

    # Add footer and close the HTML tags
    html_content += """
        <div class="footer">
            נוצר על ידי Shargil ב 3>
        </div>
    </div>
    <script>
        window.onload = function() {
            window.open(window.location.href, '_blank');
        };
    </script>
</body>
</html>
"""

    # Write the HTML content to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(html_content)
    print(f'HTML file has been created: {output_file}')

if __name__ == "__main__":
    # Example usage
    feedback_string = """שאלה הראשונה:\nציון: 85\nמשוב: יש בך הבנה טובה של הגורמים העיקריים לפרוץ מלחמת העולם השנייה. חשוב לציין יותר בפרט על השלטון של היטלר ועל ההשפעה שלו על פריצת המלחמה. ניתן גם להוסיף פורט ריצ'י, את הדרישות שהוא העלה ואת ההשלכות שלהן.\n\nשאלה השנייה:\nציון: 40\nמשוב: עליך להשלים את התשובה ולתת פירוט על קרב מידוויי, איך הוא היה המכריע ומה היו התוצאות שלו על גרמניה הנאצית.\n\nשאלה השלישית:\nציון: 75\nמשוב: נכון שהבאת גישות מנוגדות, אך חשוב להגיב בצורה מפורטת על השלכותיהן. יש צורך לפרט יותר דוגמאות ממדינות שונות ולנתח עד כמה כל אחת מהגישות תרמה לתוצאות שרשמת בתשובה."""
    create_feedback_html(feedback_string, 'student_feedback.html')
