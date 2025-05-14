def generate_topics_prompt(subject: str, level: str) -> str:
    return f"""
    You are an academic expert. Generate a list of topics for the academic subject "{subject}" based on the user's skill level: {level}.

    Ensure the topics follow a logical academic progression.

    Include 10 to 15 core topics typically taught at this level.

    Do not include descriptions, numbers, or explanations.

    Do not mix levels—only include topics for the specified level.

    Return the result strictly as a plain array of topic titles only.
    Example: ["Topic A", "Topic B", "Topic C", ...]
    """

def generate_content_prompt(subject: str, level: str, topics: list) -> str:
    return f"""
    You are an academic expert. Generate a detailed explaination for the academic subject "{subject}" at the skill level: {level}.

    The detailed lesson explaination should include the following topics: {topics}.

    Ensure the detailed lesson explaination are structured and easy to follow.

    Return the result strictly as a html use bootstarp.
    Generate all the content at once that can be used to learn for every topic.
    do not include any navigation or header or footer.
    """
