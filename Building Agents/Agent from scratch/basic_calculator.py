import operator
import json

def basic_calculator(input_str):
    """
    Perform a numeric operation on two numbers based on the input string.
    
    Parameters:
    input_str (str): A JSON string representing a dictionary with keys "num1", "num2", and "operation".
    Example: '{"num1": 5, "num2": 3, "operation": "add"}' or '{"num1": 99009, "num2": 3303, "operation": "divide"}'
    
    Returns:
    str: The formatted result of the operation.
    
    Raises:
    Exception: If an error occurs during the operation (e.g division by zero).
    ValueError: If an unsupported operation is requested or input is invalid.
    """
    
    # clean and parse the input string
    try:
        # replace the single quotes with double quotes
        input_str_clean = input_str.replace("'", '"')
        # Remove any extraneous characters such as trailing quotes
        input_str_clean = input_str_clean.strip("\"")
        
        input_dict = json.loads(input_str_clean)
        num1 = input_dict["num1"]
        num2 = input_dict["num2"]
        operation = input_dict["operation"]
    except (json.JSONDecodeError, KeyError) as e:
        return str(e), "Invalid input format. Please provide a valid JSON string."
    
    # Define the supported operations
    operations = {
        "add": operator.add,
        "subtract": operator.sub,
        "multiply": operator.mul,
        "divide": operator.truediv,
        "floor_divide": operator.floordiv,
        "modulus": operator.mod,
        "power": operator.pow,
        "lt": operator.lt,
        "le": operator.le,
        "eq": operator.eq,
        "ne": operator.ne,
        "gt": operator.gt,
        "ge": operator.ge
    }
    
    # Check if the operation is supported
    if operation in operation:
        try:
            # Perform the operation
            result = operations[operation](num1, num2)
            result_formatted = f"\n\nThe answer is: {result}.\nCalculated with the basic_calculator."
            return result_formatted
        except Exception as e:
            return "\n\nUnsupported operation. Please provide a valid operation."