import os
from flask import Flask
from redis import Redis

app = Flask(__name__)
redis_host = os.getenv('REDIS_HOST', 'redis')
redis_port = int(os.getenv('REDIS_PORT', 6379))
redis = Redis(host=redis_host, port=redis_port)

@app.route('/')
def greeting():
    return """
    <html>
        <head>
        <title>Ibrahim's Flask + Redis App</title>
        <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #333;
            color: white;
            font-family: Arial, sans-serif;
            text-align: center;
        }
        h1 {
            font-size: 2em;
        }
        </style>
        </head>
        <body>
            <h1>Welcome! You're viewing Ibrahim's Flask + Redis App!</h1>
        </body>
    </html>
    """
    

@app.route('/count')
def count():
    visits = redis.incr("counter")
    return f"""
    <html>
    <head>
        <style>
            body {{
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background-color: #333;  /* dark grey */
                color: white;
                font-family: Arial, sans-serif;
                flex-direction: column;
            }}
            .counter {{
                color: #00ff99;  /* stand-out color */
                font-size: 3em;
                margin-top: 20px;
            }}
            h1 {{
                font-size: 2em;
                margin: 0;
            }}
        </style>
    </head>
    <body>
        <h1>Welcome to Ibrahim's Flask + Redis App!</h1>
        <div class="counter">Visits: {visits}</div>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)