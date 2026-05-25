from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

# -------- Parse input (matrix / vector / scalar) --------
def parse_input(text):
    try:
        text = text.strip()

        # Matrix (2D) → rows separated by ;
        if ";" in text:
            return np.array([[float(num) for num in row.split(",")] for row in text.split(";")])

        # Vector (1D)
        elif "," in text:
            return np.array(list(map(float, text.split(","))))

        # Scalar
        else:
            return float(text)

    except:
        return None


# -------- Format output nicely --------
def format_result(res):
    try:
        if isinstance(res, np.ndarray):
            return np.array2string(res, precision=2)
        else:
            return str(round(float(res), 4))
    except:
        return str(res)


# -------- Route --------
@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        section = request.form.get("section")
        operation = request.form.get("operation")

        try:
            # ===== MATRIX / GENERAL OPS =====
            if section == "matrix":
                A = parse_input(request.form.get("matrix_a", ""))
                B = parse_input(request.form.get("matrix_b", ""))

                if A is None:
                    result = "Invalid input for A"
                else:
                    if operation == "add":
                        if B is None:
                            result = "Enter second input"
                        else:
                            result = format_result(np.array(A) + np.array(B))

                    elif operation == "multiply":
                        if B is None:
                            result = "Enter second input"
                        else:
                            # dot only if both are arrays
                            if isinstance(A, np.ndarray) and isinstance(B, np.ndarray):
                                result = format_result(np.dot(A, B))
                            else:
                                result = format_result(np.array(A) * np.array(B))

                    elif operation == "det":
                        if not isinstance(A, np.ndarray) or A.ndim != 2 or A.shape[0] != A.shape[1]:
                            result = "Matrix must be square"
                        else:
                            result = format_result(np.linalg.det(A))

                    elif operation == "inv":
                        if not isinstance(A, np.ndarray) or A.ndim != 2 or A.shape[0] != A.shape[1]:
                            result = "Matrix must be square"
                        else:
                            result = format_result(np.linalg.inv(A))

            # ===== STATISTICS =====
            elif section == "stats":
                data = parse_input(request.form.get("data", ""))

                if not isinstance(data, np.ndarray):
                    result = "Enter comma-separated values"
                else:
                    if operation == "mean":
                        result = format_result(np.mean(data))

                    elif operation == "median":
                        result = format_result(np.median(data))

                    elif operation == "std":
                        result = format_result(np.std(data))

                    elif operation == "var":
                        result = format_result(np.var(data))

        except Exception as e:
            result = f"Error: {str(e)}"

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)