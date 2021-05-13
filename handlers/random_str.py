import sys
sys.path.append("..")#把当前目录回到上一级
import tornado.web
from models.random_str import RandomstrModel
from tornado.escape import json_encode
import json

class AllHandler(tornado.web.RequestHandler):
    def get(self):
        num1= self.get_argument('num1','3')
        num2= self.get_argument('num2','3')
        req= self.get_argument('req','lnu')
        opt= self.get_argument('opt','')
        num_str = RandomstrModel.sjzf(num1,num2,req,opt)
        if num_str:
            resp = {'code':0,'message':'success','data':num_str}
            #self.write(json_encode(resp))
            self.write(resp)
        else:
            resp = {'code':99,'message':'Input error'}
            self.write(resp)
class NumHandler(tornado.web.RequestHandler):
    def get(self):
        num1= self.get_argument('num1','1')
        num2= self.get_argument('num2','1')
        try :
            num_str = RandomstrModel.numb(num1=num1,num2=num2)
            resp = {'code':0,'message':'success','data':num_str}
            #self.write(json_encode(resp))
            self.write(resp)  
        except:
            resp = {'code':99,'message':'Input error'}
            self.write(resp)
            
class LletHandler(tornado.web.RequestHandler):
    def get(self):
        num1= self.get_argument('num1','1')
        num2= self.get_argument('num2','1')
        try:
            num_str = RandomstrModel.lowl(num1=num1,num2=num2)
            resp = {'code':0,'message':'success','data':num_str}
            #self.write(json_encode(resp))
            self.write(resp)
        except:
            resp = {'code':99,'message':'Input error'}
            self.write(resp)

class UletHandler(tornado.web.RequestHandler):
    def get(self):
        num1= self.get_argument('num1','1')
        num2= self.get_argument('num2','1')
        try:
            num_str = RandomstrModel.uppl(num1=num1,num2=num2)
            resp = {'code':0,'message':'success','data':num_str}
            #self.write(json_encode(resp))
            self.write(resp)
        except:
            resp = {'code':99,'message':'Input error'}
            self.write(resp)

class PuncHandler(tornado.web.RequestHandler):
    def get(self):
        num1= self.get_argument('num1','1')
        num2= self.get_argument('num2','1')
        try:
            num_str = RandomstrModel.punc(num1=num1,num2=num2)
            resp = {'code':0,'message':'success','data':num_str}
            #self.write(json_encode(resp))
            self.write(resp)
        except:
            resp = {'code':99,'message':'Input error'}
            self.write(resp)
            
class HanziHandler(tornado.web.RequestHandler):
    def get(self):
        num1= self.get_argument('num1','1')
        num2= self.get_argument('num2','1')
        try:
            num_str = RandomstrModel.chne(num1=num1,num2=num2)
            print(num_str)
            resp = {'code':0,'message':'success','data':num_str}
            #self.write(json_encode(resp))
            print(resp)
            self.write(resp)
        except:
            resp = {'code':99,'message':'Input error'}
            self.write(resp)
            
class CustomHandler(tornado.web.RequestHandler):

#专门处理get请求  自动触发get。只要是get请求
    def get(self):
        try:
            num_str = RandomstrModel.get_str()
            resp = {'code':0,'message':'success','data':num_str}
            self.write(resp)
        except IndexError:
            resp = {'code':0,'message':'success','data':'default'}
            self.write(resp)
            
    def put(self):
        data = self.get_argument("r_string","")
        if data:
            r_string = self.get_argument("r_string")
            result = RandomstrModel.add_str(r_string)
            resp = {'code':0,'message':'add success','data':r_string}
            self.write(resp)
        else:
            try:
                data = json.loads(self.request.body)
                r_string = data['r_string']
                result = RandomstrModel.add_str(r_string)
                resp = {'code':0,'message':'add success','data':r_string}
                self.write(resp)
            except:
                resp = {'code':99,'message':'Input error'}
                self.write(resp)
           
    def post(self):
        data = self.get_argument("oldstr","")
        if data:
            oldstr = self.get_argument('oldstr')
            newstr = self.get_argument('newstr')
            result = RandomstrModel.update_str(oldstr,newstr)
            if result:
                resp = {'code':0,'message':'update success','data':result}
                self.write(resp)
            else:
                resp = {'status': False,'msg': 'This old string is not in here'}
                self.write(resp)
        else:
            try:
                data = json.loads(self.request.body)
                oldstr = data['oldstr']
                newstr = data['newstr']
                result = RandomstrModel.update_str(oldstr,newstr)
                if result:
                    resp = {'code':0,'message':'update success','data':result}
                    self.write(resp)
                else:
                    resp = {'code':99,'message':'This old string is not in here'}
                    self.write(resp)
            except:
                resp = {'code':99,'message':'Input error'}
                self.write(resp)
                
    def delete(self):
        data = self.get_argument("r_string","")
        if data:
            r_string = self.get_argument("r_string")
            result = RandomstrModel.del_str(r_string)
            resp = {'code':0,'message':'delete success','data':result}
            self.write(resp)
        else:
            try:
                data = json.loads(self.request.body)
                r_string = data['r_string']
                result = RandomstrModel.del_str(r_string)
                resp = {'code':0,'message':'delete success','data':r_string}
                self.write(resp)
            except:
                resp = {'code':99,'message':'Input error'}
                self.write(resp)

class CustomsHandler(tornado.web.RequestHandler):
    def get(self):
        try:
            num_str = RandomstrModel.get_strs()
            resp = {'code':0,'message':'success','data':num_str}
            self.write(resp)
        except IndexError:
            resp = {'code':0,'message':'success','data':'default'}
            self.write(resp)
