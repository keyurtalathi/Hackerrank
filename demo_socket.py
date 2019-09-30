
import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.template
import json

class WSHandler(tornado.websocket.WebSocketHandler):
  def check_origin(self, origin):
    return True
  def open(self):
    print 'connection opened...'
    self.write_message("The server says: 'Hello'. Connection was accepted.")

  def on_message(self, message):
    data = json.loads(message)
    self.write_message(data["name"])
    print 'received:', message

  def on_close(self):
    print 'connection closed...'

application = tornado.web.Application([
  (r'/ws', WSHandler),
])

if __name__ == "__main__":
  application.listen(1234)
  tornado.ioloop.IOLoop.instance().start()
