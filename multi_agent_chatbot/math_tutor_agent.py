from agents import Agent, function_tool


@function_tool
def calculate_math(
    first_number: float, second_number: float, operation: str
) -> str:
    """Calculate a basic arithmetic operation.

    Args:
        first_number: The first number in the calculation.
        second_number: The second number in the calculation.
        operation: One of add, subtract, multiply, or divide.
    """
    operations = {
        "add": ("+", lambda: first_number + second_number),
        "subtract": ("-", lambda: first_number - second_number),
        "multiply": ("*", lambda: first_number * second_number),
        "divide": ("/", lambda: first_number / second_number),
    }
    selected_operation = operations.get(operation.strip().lower())
    if selected_operation is None:
        return "Unsupported operation. Choose add, subtract, multiply, or divide."

    symbol, calculate = selected_operation
    if symbol == "/" and second_number == 0:
        return "Division by zero is undefined."

    return f"{first_number:g} {symbol} {second_number:g} = {calculate():g}"


math_tutor_agent = Agent(
    name="Math Tutor",
    instructions="""
    You are a patient math tutor for school-age learners.
    Explain the reasoning in clear, age-appropriate steps instead of giving
    only the answer. Use the calculate_math tool to verify basic arithmetic.
    Ask a brief clarifying question when a problem is ambiguous.
    """,
    tools=[calculate_math],
)
