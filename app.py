from flask import Flask, request, render_template, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    text = request.form['text']
    mp3_path = generate_music_from_text(text)
    return send_file(mp3_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
