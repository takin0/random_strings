from handlers.random_str import *
#from handlers.random_str import RandomstrHandler
import tornado.web
import tornado.httpserver
import tornado.ioloop

#定义全局的Handlers
HANDLERS = [
    #可以吧第一个参数看做是正则表达式。匹配接口，
    # 只要匹配成功，则会触发后面的类，会将括号中的参数传给指定的函数
    #http://127.0.0.1:9999/api/user/1
    (r'/all',AllHandler),
    (r'/number',NumHandler),
    (r'/l_letter',LletHandler),
    (r'/u_letter',UletHandler),
    (r'/punc',PuncHandler),
    (r'/hanzi',HanziHandler),
    (r'/custom',CustomHandler),
    (r'/customs',CustomsHandler)
]

def run():

#创建app对象
    app = tornado.web.Application(
    HANDLERS,
    debug = True  #修改后服务自动重启
)
#启用tornado专用的非阻塞单线程app服务
    http_server = tornado.httpserver.HTTPServer(app)
#定义监听的端口。
    port = 9988
    http_server.listen(port)
    print('server id start no port:{}'.format(port))

#启动服务
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    run()
