from flask import Flask, request, abort, make_response
# from redis import Redis
from module import bot_callback
# from rq import Queue, Worker
import json
from twitchbot import TwitchBot

# r= Redis()

# q = Queue(connection=r)

# worker = Worker.all(connection=r)

app = Flask(__name__)


def return_success():
    return 'success'
@app.route('/twitchbot-init', methods=['POST'])
def init_bot():
    if request.method == 'POST':
        bid = '254489093'
        data = request.data
        # my_resp = make_response(data)
        # my_resp = my_resp.mimetype='application/json'

        # print(data['challenge'])
        # @after_this_request
        # def make_init_req(request):
        #     new_bot.startTheBot()
        # botInit = q.enqueue(bot_callback, job_timeout=86400)
        botInit = TwitchBot().start_bot()
        return json.dumps({'challenge':str(data)})
@app.route('/twitchbot-start',methods=['POST'])
def webhook():
    if request.method == 'POST':
        return "success"
        new_bot.startTheBot()
        # print(request.json)
        return 'Iniciado!',200
    else:
        abort(400)

@app.route('/twitchbot-stop',methods=['POST'])
def stop_bot():
    if request.method == 'POST':
        # print(request.json)
        kill = new_bot.pauseTheBot()
    else:
        abort(400)
    return new_bot.checkTheBot()

@app.route('/twitchbot-check',methods=['POST'])
def check_bot():
    return new_bot.checkTheBot()

    # @app.route('/force-stop', methods=['POST'])
    # def warning_bot():
    #     warn = 

    # app.run()
if __name__=='__main__':
    app.run(host='143.244.162.80',port=500)
