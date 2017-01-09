from flask import Flask, request, render_template;
app = Flask(__name__)

@app.route("/encode", methods=['GET', 'POST'])
def encode():
  if request.method == 'GET':
    return render_template("encode.html");
  elif request.method == 'POST':
    text = request.form['text'];
    key = request.form['key'];
    intKey = int(key)
    VALID_STRING = 'abcdefghijklmnopqrstuvwxyz'
    encrypt_string = 'abcdefghijklmnopqrstuvwxyz' * 2
    output = ''
    for char in text:
      if char in VALID_STRING:
        index = encrypt_string.index(str(char))
        output += encrypt_string[index + intKey]
      else:
        output += char
    return render_template("encoded.html", key=key, text=text, output=output);
  # else:
   #  return "<h1>Invalid Request</h1>";

#@app.route("/encoded", methods=['GET', 'POST'])


if __name__ == "__main__":
  app.run()
