from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this in production

# In-memory storage for chat history, sentiment, and concerns
chat_history = []
sentiment_data = []
concerns = []

# Simple sentiment analysis function (placeholder)
def analyze_sentiment(text):
    # This is a simplified sentiment analysis
    # In a real application, you would use a proper model
    positive_words = ['good', 'great', 'excellent', 'amazing', 'wonderful', 'fantastic', 'love']
    negative_words = ['bad', 'terrible', 'awful', 'horrible', 'hate', 'dislike', 'worst']
    
    text_lower = text.lower()
    pos_count = sum(1 for word in positive_words if word in text_lower)
    neg_count = sum(1 for word in negative_words if word in text_lower)
    
    if pos_count > neg_count:
        return "Positive"
    elif neg_count > pos_count:
        return "Negative"
    else:
        return "Neutral"

# Placeholder function for AI response generation
def generate_ai_response(question):
    # In a real implementation, this would connect to IBM Granite model
    responses = {
        "hello": "Hello! How can I assist you with government services today?",
        "services": "We offer various services including tax information, public transportation updates, and permit applications.",
        "tax": "For tax-related queries, please visit the official tax department website or contact them directly.",
        "transport": "Public transportation schedules and updates are available on our services page.",
        "default": "Thank you for your question. I'm analyzing your query and will provide assistance shortly. Our team is constantly working to improve responses to citizen inquiries."
    }
    
    # Simple keyword matching for demonstration
    question_lower = question.lower()
    for key, response in responses.items():
        if key in question_lower:
            return response
    return responses["default"]

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/chat')
def chat():
    return render_template('chat.html', chat_history=chat_history)

@app.route('/dashboard')
def dashboard():
    # Aggregate sentiment data
    sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}
    for item in sentiment_data:
        sentiment_counts[item["sentiment"]] += 1
    
    return render_template('dashboard.html', 
                         sentiment_counts=sentiment_counts, 
                         concerns=concerns)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Simple authentication (in production, use proper authentication)
        if username and password:
            session['username'] = username
            return redirect(url_for('chat'))
        else:
            return render_template('login.html', error="Please enter both username and password")
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

# API routes for handling form submissions
@app.route('/ask', methods=['POST'])
def ask_question():
    question = request.form.get('question')
    if question:
        # Generate AI response
        response = generate_ai_response(question)
        
        # Store in chat history
        chat_history.append({"question": question, "response": response})
        
        return render_template('chat.html', 
                             chat_history=chat_history, 
                             question_response=response)
    else:
        return render_template('chat.html', 
                             chat_history=chat_history, 
                             error="Please enter a question")

@app.route('/feedback', methods=['POST'])
def submit_feedback():
    feedback = request.form.get('feedback')
    if feedback:
        # Analyze sentiment
        sentiment = analyze_sentiment(feedback)
        
        # Store sentiment data
        sentiment_data.append({"feedback": feedback, "sentiment": sentiment})
        
        return render_template('chat.html', 
                             chat_history=chat_history,
                             sentiment=sentiment)
    else:
        return render_template('chat.html', 
                             chat_history=chat_history,
                             error="Please enter feedback")

@app.route('/concern', methods=['POST'])
def submit_concern():
    concern = request.form.get('concern')
    if concern:
        # Store concern
        concerns.append({"concern": concern})
        
        return render_template('chat.html', 
                             chat_history=chat_history,
                             concern_submitted=True)
    else:
        return render_template('chat.html', 
                             chat_history=chat_history,
                             error="Please enter a concern")

if __name__ == '__main__':
    app.run(debug=True)