from flask import Flask, render_template, jsonify

app = Flask(__name__)

healing_data = [
    {"msg": "Picking up the sharpest edges...", "shake": "0.3s"},
    {"msg": "Aligning what was broken...", "shake": "0.3s"},
    {"msg": "The friction is finally fading...", "shake": "0.4s"},
    {"msg": "Almost whole again. Brace yourself.", "shake": "0.8s"}
]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/mend/<int:step>')
def mend(step):
    if step < len(healing_data):
        return jsonify(healing_data[step])
    return jsonify({"done": True})


if __name__ == '__main__':
    app.run(debug=True)
