import time
import matplotlib.pyplot as plt

# AI-Generated Solutions
def ai_solution_1(n):
    if n == 0:
        return 1
    return n * ai_solution_1(n - 1)

def ai_solution_2(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Evaluate Solutions
def evaluate_solutions(test_cases, *functions):
    results = []
    for func in functions:
        func_results = {"function": func.__name__, "correctness": 0, "execution_time": 0, "failed_cases": []}
        start_time = time.time()
        for input_val, expected in test_cases:
            try:
                output = func(input_val)
                if output == expected:
                    func_results["correctness"] += 1
                else:
                    func_results["failed_cases"].append((input_val, output, expected))
            except Exception as e:
                func_results["failed_cases"].append((input_val, str(e), expected))
        func_results["execution_time"] = time.time() - start_time
        func_results["correctness"] = (func_results["correctness"] / len(test_cases)) * 100
        results.append(func_results)
    return results

# Summarize Results
def summarize_results(results):
    for result in results:
        print(f"Function: {result['function']}")
        print(f"  - Correctness: {result['correctness']}%")
        print(f"  - Execution Time: {result['execution_time']:.6f} seconds")
        if result["failed_cases"]:
            print("  - Failed Cases:")
            for case in result["failed_cases"]:
                print(f"    Input: {case[0]}, Output: {case[1]}, Expected: {case[2]}")
        print("\n")

# Visualize Results
def visualize_results(results):
    functions = [res["function"] for res in results]
    times = [res["execution_time"] for res in results]
    correctness = [res["correctness"] for res in results]

    plt.bar(functions, times, label="Execution Time (s)")
    plt.title("Solution Performance: Execution Time")
    plt.ylabel("Time (s)")
    plt.show()

    plt.bar(functions, correctness, label="Correctness (%)", color="green")
    plt.title("Solution Performance: Correctness")
    plt.ylabel("Percentage")
    plt.show()

# Chatbot Improvement
def chatbot_response(input_text):
    if "hello" in input_text.lower():
        return "Hi there!"
    return "I'm not sure I understand."

def improve_response(input_text, feedback):
    response = chatbot_response(input_text)
    if feedback == "too generic":
        return f"Improved Response: Let's make '{response}' more engaging."
    return response

# Main Program
if __name__ == "__main__":
    # Test Cases
    test_cases = [
        (0, 1),  # Factorial of 0
        (1, 1),  # Factorial of 1
        (5, 120),  # Factorial of 5
        (10, 3628800),  # Factorial of 10
    ]

    # Evaluate Solutions
    results = evaluate_solutions(test_cases, ai_solution_1, ai_solution_2)

    # Summarize and Visualize Results
    summarize_results(results)
    visualize_results(results)

    # Chatbot Example
    print("\nChatbot Response Example:")
    print(chatbot_response("Hello"))
    print(improve_response("Hello", "too generic"))
