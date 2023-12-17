from flask import Flask, request

app = Flask(__name__)

@app.route('/get_cookies')
def get_cookies():
    # Retrieve all the cookies that are part of the request
    cookies = request.cookies

    return f"Cookies: {cookies}"

if __name__ == '__main__':
    app.run(debug=True)