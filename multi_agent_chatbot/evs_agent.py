from agents import Agent, function_tool


@function_tool
def lookup_evs_topic(topic: str) -> str:
    """Look up a concise fact for a common Environmental Studies topic."""
    facts = {
        "water cycle": (
            "The water cycle moves water through evaporation, condensation, "
            "precipitation, and collection."
        ),
        "pollution": (
            "Pollution is the introduction of harmful substances or energy "
            "into the environment. Common types include air, water, and "
            "land pollution."
        ),
        "recycling": (
            "Recycling processes used materials into new products, reducing "
            "the need for some raw materials and the amount of waste sent "
            "to landfill."
        ),
        "renewable energy": (
            "Renewable energy comes from sources that are naturally "
            "replenished, such as sunlight, wind, and flowing water."
        ),
        "ecosystem": (
            "An ecosystem is a community of living organisms interacting "
            "with one another and with their physical environment."
        ),
        "plants": (
            "Plants use sunlight, water, and carbon dioxide to make food "
            "through photosynthesis; they also release oxygen."
        ),
        "conservation": (
            "Conservation means protecting and using natural resources "
            "responsibly so they remain available in the future."
        ),
    }
    topic_key = topic.strip().lower()
    return facts.get(
        topic_key,
        f"No reference fact is stored for '{topic}'. Explain the topic "
        "using reliable general knowledge, or ask the learner to narrow it.",
    )


evs_agent = Agent(
    name="Environmental Studies Tutor",
    instructions="""
    You are a friendly Environmental Studies (EVS) tutor for school-age
    learners. Explain concepts simply, connect them to everyday life, and
    use the lookup_evs_topic tool for topics in its reference list. For topics
    outside that list, be clear when you are relying on general knowledge and
    avoid inventing facts.
    """,
    tools=[lookup_evs_topic],
)
