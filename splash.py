from flask import Flask, render_template_string

app = Flask(__name__)

HTML_SEM_BORDA = """
<!DOCTYPE html>
<html>
<head>
    <title>Farmix Online</title>
    <link rel="icon" href="https://i.ibb.co/BD68Zgp/favicon-portal.png" type="image/x-icon">
    <style>
        html, body {
            margin: 0;
            padding: 0;
            height: 100%;
            overflow: hidden;
            background-color: #204399;
        }

        #streamlit-container {
            display: none;
            width: 100vw;
            height: 100vh;
            border: none;
        }

        #loader {
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
            font-size: 24px;
            font-family: sans-serif;
            color: #ffffff;
            background-color: #204399;
        }
    </style>
</head>
<body>
    <div id="loader"><img src="https://i.ibb.co/wNJrYs66/logo-animation.gif" style="max-width: 300px; height: auto;"></div>
    <iframe id="streamlit-container" src="/app/"></iframe>

    <script>
        const iframe = document.getElementById("streamlit-container");
        iframe.onload = function() {
            document.getElementById("loader").style.display = "none";
            iframe.style.display = "block";
        };
    </script>
</body>
</html>
"""


@app.route('/')
def app_com_preload():
    return render_template_string(HTML_SEM_BORDA)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8503)
