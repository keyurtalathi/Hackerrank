import tornado.ioloop
import tornado.web
import tornado.websocket
import json
from userattempt.models.user_attempt_handler import handle_and_run_code

class WSHandler(tornado.websocket.WebSocketHandler):
  def check_origin(self, origin):
    return True
  def open(self):
    print 'connection opened...'
    self.write_message("The server says: 'Hello'. Connection was accepted.")

  def on_message(self, message):
    data = json.loads(message)
    handle_and_run_code(data, self.write_message)
    # self.write_message(data["name"])
    print 'received:', message

  def on_close(self):
    print 'connection closed...'

