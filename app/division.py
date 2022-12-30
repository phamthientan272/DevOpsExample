def divide(number_1, number_2):
    if number_2 == 0:
        return {"error": "Cannot divide by zero"}
    return {"result": number_1 / number_2}