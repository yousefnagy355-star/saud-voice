import os
import asyncio
import edge_tts
from flask import Flask, request, send_file

app = Flask(__name__)

@app.route('/speak')
async def speak():
    text = request.args.get('text', 'يا هلا بالحبيب')
    voice = "ar-KW-FahedNeural"
    output_file = "/tmp/voice.mp3"
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_file)
    return send_file(output_file, mimetype="audio/mp3")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
