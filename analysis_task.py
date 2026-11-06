from crewai import Task

def analysis_task(agent, user_input):
    return Task(
        description=f"""
        Analyze the following user input about their preferences and history:
        "{user_input}"

        Your job is to create a **Shopper Profile**.
        
        Requirements:
        1. Extract the Budget range (if mentioned, or infer it).
        2. Identify Key Priorities (e.g., speed vs. battery life, style vs. comfort).
        3. Note any Brand Preferences or "Dealbreakers" based on history.
        4. Determine the "User Persona" (e.g., "Professional Gamer", "Budget Student", "Enterprise User").

        Output Format:
        Return a clean summary of this profile in Bullet Points.
        """,
        expected_output="A structured summary of the user's buyer profile.",
        agent=agent
    )