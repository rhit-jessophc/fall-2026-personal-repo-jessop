import flask
import threading 
import Exam_1.Python.hadley_blinker as hadley_blinker

app = flask.Flask(__name__, static_url_path="", static_folder="public")
hadleyBlinker = hadley_blinker.HadleyBlinker()

serial_lock = threading.Lock()

@app.get("/")
def handle_naked_domain():
    return flask.redirect("/index.html")

# @app.get("/api/<command>")
# def handle_blinker_commands(command):
#     with serial_lock:
#         response = hadley_blinker.send_command(command)
#     return response

# TODO: add code to reject imputs other than on or off
@app.get("/api/led/<command>")
def handle_blinker_commands_LED_ON_OFF(command):
    if (command.upper() != "ON") and (command.upper() != "OFF"):
        return "Unknown Command"
    with serial_lock:
        response = hadley_blinker.send_command_LED_ON_OFF(command)
    return response

@app.get("/api/flash/<numFlash>/<periodFlash>")
def handle_blinker_commands_FLASH(numFlash, periodFlash):
    if numFlash.isdigit() == False or numFlash.isdigit() == False:
        return "Input Not A Number"
    with serial_lock:
        response = hadley_blinker.send_command_FLASH("FLASH " + numFlash + " " + periodFlash)
    return response


if __name__ == "__main__":
    print("Running flask!")
    hadley_blinker.connect()
    try:
        app.run(host="0.0.0.0", port=8080, use_reloader=False)
    finally:
        print("Disconnecting blinker")
        


    