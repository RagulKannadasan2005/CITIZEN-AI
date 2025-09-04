# Citizen AI - Intelligent Citizen Engagement Platform

## Project Overview

Citizen AI is an intelligent citizen engagement platform designed to revolutionize how governments interact with the public. Leveraging Flask, IBM Granite models, and IBM Watson, Citizen AI provides real-time, AI-driven responses to citizen inquiries regarding government services, policies, and civic issues.

The platform integrates natural language processing (NLP) and sentiment analysis to assess public sentiment, track emerging issues, and generate actionable insights for government agencies. A dynamic analytics dashboard offers real-time visualizations of citizen feedback, helping policymakers enhance service delivery and transparency.

By automating routine interactions and enabling data-driven governance, Citizen AI improves citizen satisfaction, government efficiency, and public trust in digital governance.

## Key Features

### 1. Real-Time Conversational AI Assistant
The primary interface for citizen interaction, allowing users to engage with public services naturally by typing questions or requests. The system captures user input in real-time and immediately sends it to the IBM Granite model, which processes the query and generates a relevant, human-like response.

### 2. Citizen Sentiment Analysis
Analyzes text input from citizen feedback to classify sentiment as Positive, Neutral, or Negative. This helps government agencies quickly identify areas of public satisfaction or concern and make data-driven decisions to improve services.

### 3. Dynamic Dashboard
A central hub for government officials to gain real-time insights into citizen feedback and interactions. It visualizes key data points including overall citizen sentiment and tracks interaction trends over time.

## Technology Stack

- **Backend**: Python Flask
- **AI Models**: IBM Granite models via Hugging Face Transformers
- **Frontend**: HTML, CSS, JavaScript
- **Data Processing**: PyTorch, Transformers library
- **Deployment**: Local development server (can be deployed to cloud platforms)

## Project Structure

```
CITIZEN AI/
│
├── static/
│   ├── Favicon/
│   ├── Images/
│   │   ├── citizen AI 1.jpg
│   │   └── citizen AI.jpg
│   └── styles.css
│
├── Templates/
│   ├── about.html
│   ├── chat.html
│   ├── dashboard.html
│   ├── index.html
│   ├── login.html
│   └── services.html
│
├── app.py
├── requirements.txt
└── README.md
```

## Installation and Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd CITIZEN-AI
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   python app.py
   ```

5. **Access the application**:
   Open your web browser and go to `http://localhost:5000`

## Prerequisites

- Python 3.7+
- Flask
- PyTorch
- Hugging Face Libraries (transformers, accelerate, bitsandbytes)
- Sufficient hardware resources (RAM 16GB+, GPU recommended)

## Usage

1. Navigate to the home page
2. Click "Get Started" to access the login page
3. Log in with any username and password (for demo purposes)
4. Use the chat interface to ask questions about government services
5. Provide feedback for sentiment analysis
6. Report civic concerns
7. View analytics on the dashboard

## Future Enhancements

- Integration with actual IBM Granite models for more accurate responses
- Database integration for persistent storage
- User account management
- Advanced analytics and reporting features
- Multi-language support
- Mobile-responsive design

## Contributing

This project is a demonstration application. Contributions to enhance functionality, improve UI/UX, or add new features are welcome.

## License

This project is for educational and demonstration purposes.