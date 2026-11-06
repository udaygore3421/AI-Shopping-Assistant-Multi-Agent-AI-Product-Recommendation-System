from crewai import Task

def recommendation_task(agent, user_profile):
    return Task(
        description=f"""
        Based on this User Profile, suggest the best products:
        
        USER PROFILE:
        {user_profile}
        
        REQUIREMENTS:
        1. Suggest exactly 3 distinct options:
           - Option A: The Best Overall Match
           - Option B: The Best Value/Budget Option
           - Option C: The High-Performance/Premium Option
        2. For each product, include:
           - Full Product Name
           - Estimated Price
           - Key Features matching the profile
           - "Why you should buy this" (Reasoning)
        
        OUTPUT FORMAT:
        Return the result in beautiful Markdown format. 
        Use bolding for names and bullet points for features. 
        Do NOT include HTML code, just readable text/tables.
        """,
        expected_output="A Markdown formatted list of 3 product recommendations.",
        agent=agent
    )