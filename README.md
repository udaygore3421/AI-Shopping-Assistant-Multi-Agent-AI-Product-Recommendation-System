# 🛍️ AI Shopping Assistant – Multi-Agent AI Product Recommendation System

An AI-powered shopping assistant built using **Python, Streamlit, CrewAI, and Google Gemini**. It uses multiple specialized AI agents to understand user requirements, create personalized shopper profiles, recommend suitable products, and find the best available prices with purchase links.

## 🚀 Project Overview

Choosing the right product online can be time-consuming. Users often need to compare different products, prices, specifications, and features before making a purchase.

The **AI Shopping Assistant** simplifies this process using a multi-agent AI architecture.

Instead of manually researching products, users can describe their requirements in natural language. The AI agents work together to analyze preferences, generate personalized recommendations, and search for suitable deals.

## ✨ Key Features

- **AI Shopper Analysis:** Analyzes user requirements, budget, priorities, and brand preferences.
- **Personalized Recommendations:** Suggests three product options based on the shopper profile.
- **Multi-Agent Architecture:** Uses specialized AI agents for analysis, recommendations, and price hunting.
- **Budget-Based Suggestions:** Provides overall, budget-friendly, and premium product choices.
- **Price Comparison:** Helps identify competitive product prices.
- **Purchase Links:** Provides relevant shopping links.
- **Interactive Chat Interface:** Simple and user-friendly Streamlit interface.
- **Gemini AI Integration:** Uses Google Gemini 2.0 Flash as the language model.

## 🧠 AI Agent Workflow

The project uses three specialized AI agents:

### 1. Analyst Agent
- Understands the user's shopping requirements.
- Identifies the budget range.
- Extracts important product preferences.
- Creates a personalized shopper profile.

### 2. Recommender Agent
- Analyzes the shopper profile.
- Recommends three suitable products.
- Provides estimated prices and key features.
- Explains why each product is a good match.

### 3. Price Hunter Agent
- Searches for competitive product prices.
- Identifies suitable shopping deals.
- Provides product purchase links.

## 🔄 Project Workflow

1. User enters shopping requirements.
2. Analyst Agent creates a shopper profile.
3. User reviews the generated profile.
4. Recommender Agent suggests three products.
5. User reviews the recommendations.
6. Price Hunter Agent searches for prices and purchase links.
7. Results are displayed in the Streamlit chat interface.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application interface |
| CrewAI | Multi-agent AI framework |
| Google Gemini 2.0 Flash | Large Language Model |
| Python-dotenv | Environment variable management |

## 📂 Project Structure

```text
ai-agent/
│
├── app.py
├── crew_setup.py
├── analysis_task.py
├── recommendation_task.py
├── recommender_agent.py
├── requirements.txt
├── .env
└── README.md
```

The agent and task modules are organized separately in the implementation imports and should be included in their respective folders.

## ⚙️ Installation and Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/udaygore3421/ai-agent.git
```

### Step 2: Navigate to the Project Directory

```bash
cd ai-agent
```

### Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Configure Gemini API Key

Create a `.env` file in the project root directory.

Add your Google Gemini API key:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

Get your API key from:

https://aistudio.google.com/apikey

**Important:** Never share your API key or upload your `.env` file to GitHub.

### Step 6: Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

## 💻 Requirements

- Python 3.10 or compatible version supported by your installed CrewAI release.
- Google Gemini API key.
- Internet connection.
- Required Python dependencies.

## 🎯 Example Usage

**User Input:**

"I need a laptop for programming, data analysis, and gaming with a budget of ₹70,000."

**Expected AI Process:**

- Analyst Agent: Understands the budget and requirements.
- Recommender Agent: Suggests three suitable laptops.
- Price Hunter Agent: Finds competitive prices and shopping links.

## 🔮 Future Enhancements

- Real-time product price comparison.
- Integration with Amazon and Flipkart product sources.
- Product ratings and customer review analysis.
- Product filtering by brand, price, and specifications.
- Product recommendation history.
- Improved deal tracking and price alerts.
- User authentication and personalized shopping profiles.

## 👨‍💻 Author

**Uday Gore**

GitHub: https://github.com/udaygore3421

---
⭐ If you find this project useful, consider giving the repository a star!

**Built with Python, CrewAI, Streamlit, and Google Gemini.**
