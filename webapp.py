from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/response")
def render_response():
    color = request.args['color']
    #variable color stores the information about the request sent to the server.
    #args is a MultiDict (like a dictionary but can have multiple values for the same key)
    #he information in args is visible in the url for the page being requested. ex. .../respone?color=orange
    if (color == 'pink'):
        reply = "That's my favorite color, too!"
    else:
        reply = "HAHA!! THAT COLOR IS TRAAAASH!!!! my favorite color is pink haha!!"
    return render_template('response.html', response = reply)
    
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
