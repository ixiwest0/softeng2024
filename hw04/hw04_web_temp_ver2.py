from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    html_str = """
<!DOCTYPE html>
<html lang="kr">
<head>
    <meta charset="UTF-8">
    <title>온도 변환기</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
    <h2>온도 단위 변환하기</h2>
    <form id="tempForm">
        <label>온도 :
            <input type="text" id="temp_input" name="temp">
        </label>
        <button type="button" onclick="convertTemp('to_f')">화씨로 변환</button>
        <button type="button" onclick="convertTemp('to_c')">섭씨로 변환</button>
    </form>
    <h3 id="result"></h3>

    <script>
        function convertTemp(convertType) {
            var tempValue = document.getElementById("temp_input").value;

            $.ajax({
                url: '/convert_temperature',
                type: 'POST',
                data: {
                    temp: tempValue,
                    convert_type: convertType
                },
                success: function(response) {
                    document.getElementById("result").innerHTML = response.result;
                },
                error: function(error) {
                    alert("에러가 발생했습니다.");
                }
            });
        }
    </script>
</body>
</html>
"""
    return html_str


@app.route("/convert_temperature", methods=["POST"])
def convert_temperature():
    temp = request.form.get('temp')
    convert_type = request.form.get('convert_type')

    try:
        temp = float(temp)
        if convert_type == "to_f":
            result = f"{temp}℃ -> {(temp * 9 / 5) + 32:.2f}℉입니다."
        elif convert_type == "to_c":
            result = f"{temp}℉ -> {(temp - 32) * 5 / 9:.2f}℃입니다."
        else:
            result = "변환 유형을 선택해 주세요."
    except ValueError:
        result = "유효한 숫자를 입력해 주세요."

    return jsonify(result=result)


if __name__ == "__main__":
    app.run(debug=True)
