from crewai import Crew, LLM
from agents.analyst_agent import get_analyst
from agents.recommender_agent import get_recommender
from agents.price_agent import get_price_hunter
from tasks.analysis_task import analysis_task
from tasks.recommendation_task import recommendation_task
from tasks.price_task import price_task

from dotenv import load_dotenv
import os
import time

load_dotenv()

# Initialize Gemini with specific configuration
llm = LLM(
    model="gemini/gemini-2.0-flash",
    api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.7
)

# Helper function to handle API limits gracefully
def safe_kickoff(crew):
    try:
        return crew.kickoff()
    except Exception as e:
        error_message = str(e)
        if "429" in error_message or "RESOURCE_EXHAUSTED" in error_message:
            print("⚠️ Hit Rate Limit (429). Sleeping for 30 seconds before retrying...")
            time.sleep(30)
            try:
                return crew.kickoff()
            except Exception as retry_e:
                return f"Error after retry: {str(retry_e)}"
        else:
            return f"Error executing crew: {error_message}"

def run_analysis(user_input):
    print("...Analyst Agent Starting...")
    analyst = get_analyst(llm)
    task = analysis_task(analyst, user_input)
    
    # max_rpm=2 ensures we don't send more than 2 requests per minute
    crew = Crew(agents=[analyst], tasks=[task], verbose=True, max_rpm=2)
    
    result = safe_kickoff(crew)
    return str(result)

def run_recommendation(user_profile):
    print("...Recommender Agent Starting...")
    time.sleep(5) # Safety pause between agents
    
    recommender = get_recommender(llm)
    task = recommendation_task(recommender, user_profile)
    
    # max_rpm=2 ensures we don't send more than 2 requests per minute
    crew = Crew(agents=[recommender], tasks=[task], verbose=True, max_rpm=2)
    
    result = safe_kickoff(crew)
    return str(result)

def run_price_hunt(product_list):
    print("...Price Hunter Agent Starting...")
    time.sleep(5) # Safety pause between agents
    
    price_hunter = get_price_hunter(llm)
    task = price_task(price_hunter, product_list)
    
    # max_rpm=2 ensures we don't send more than 2 requests per minute
    crew = Crew(agents=[price_hunter], tasks=[task], verbose=True, max_rpm=2)
    
    result = safe_kickoff(crew)
    return str(result)