
import tornado.template
from userattempt.controller.user_attempt import WSHandler

application = tornado.web.Application([
  (r'/ws', WSHandler),
])

if __name__ == "__main__":
  application.listen(1234)
  tornado.ioloop.IOLoop.instance().start()

