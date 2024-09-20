from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
    html_str = """
<!DOCTYPE html>
<html lang="kr">
<head> 
    <meta charset="UTF-8">
    <title>Temperature Conversion</title>
</head>

<body>
    <form method="GET" action="/temperature">
    <h2>온도 단위 변환하기</h2>
    <label>온도 :
        <input type="text" id="temp_input" name="temp">
    </label>

    <button type="button" onclick="c2f()">화씨로 변환</button>
    <button type="button" onclick="f2c()">섭씨로 변환</button>

    </form>
    <script>
        function c2f(){
            const temp = document.getElementById('temp_input').value;            
            const result = ((parseFloat(temp) * 1.8) + 32).toFixed(2);

            if(isNaN(result))
                alert("잘못입력하셨습니다. 숫자를 입력해주세요")
            else
                alert(temp + "°C => " + result + "°F");
        }

        function f2c(){
            const temp = document.getElementById('temp_input').value;
            const result = ((parseFloat(temp) - 32) / 1.8).toFixed(2);

            if(isNaN(result))
                alert("잘못입력하셨습니다. 숫자를 입력해주세요")
            else
            alert(temp + "°F => " + result + "°C");
        }
    </script>
</body>
</html>
</body>
</html>

"""
    return html_str



app.run(debug=True)
