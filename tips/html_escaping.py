from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route('/hello')
def hello():

    '''
    The request.args.get("name", "Flask") method retrieves the value of the "name" query parameter from the URL.
    If the "name" parameter is not provided in the URL, it defaults to "Flask".
    Example:
    - If the user visits /hello?name=Alice, name will be "Alice".
    - If the user visits /hello without any parameters, name will be "Flask".
    '''

    name = request.args.get("name", "Flask")

    '''
    The escape() function from the markupsafe module is used to prevent Cross-Site Scripting (XSS) attacks by escaping special characters in the user input.
    Example: 
    If a user provides the name as <script>alert('XSS')</script>, without escaping, this would be rendered as actual HTML/JavaScript in the browser, potentially executing the script.
    By using escape(name), the special characters are converted to their HTML-safe equivalents, rendering the input harmless:
    &lt;script&gt;alert(&#39;XSS&#39;)&lt;/script&gt;
    This ensures that the input is displayed as plain text rather than being executed as code.
    '''

    return f'<p>Hello, {escape(name)}!!!</p>' 