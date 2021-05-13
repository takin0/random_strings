#初始化用户列表
import random,string

class RandomstrModel(object):
    custom_str = []

# 获取单个用户,使用类方法
#cls是当前类。类方法不要用类的实例来调用，要用当前类来调用
    @classmethod
    def numb(cls,num1=1,num2=1):
        num1 = int(num1)
        num2 = int(num2)
        if num1 >= num2:
            num = num1
        else:
            num = random.randint(num1,num2)
        digits = ''
        while num > 0:        
            digit = random.randint(0,9)
            num -= 1
            digits = digits + (str(digit))
        return digits

    @classmethod  
    def lowl(cls,num1=1,num2=1):
        num1 = int(num1)
        num2 = int(num2)
        if num1 >= num2:
            num = num1
        else:
            num = random.randint(num1,num2)
        letters= ''
        while num > 0:
            s = string.ascii_lowercase
            letter = random.choice(s)
            num -= 1
            letters = letters + letter
        return letters

    @classmethod  
    def uppl(cls,num1=1,num2=1):
        num1 = int(num1)
        num2 = int(num2)
        if num1 >= num2:
            num = num1
        else:
            num = random.randint(num1,num2)
        letters= ''
        while num > 0:
            s = string.ascii_uppercase
            letter = random.choice(s)
            num -= 1
            letters = letters + letter
        return letters

    @classmethod
    def punc(cls,num1=1,num2=1):
        num1 = int(num1)
        num2 = int(num2)
        if num1 >= num2:
            num = num1
        else:
            num = random.randint(num1,num2)
        puncs = ''
        while num > 0:
            s = string.ascii_uppercase
            s = string.punctuation
            punc = random.choice(s)
            num -= 1
            puncs = puncs + str(punc)
        return puncs

    @classmethod
    def chne(cls,num1=1,num2=1):
        num1 = int(num1)
        num2 = int(num2)
        if num1 >= num2:
            num = num1
        else:
            num = random.randint(num1,num2)
        strs=''
        while num>0:
            head = random.randint(0xb0, 0xf7)
            body = random.randint(0xa1, 0xfe)
            val = f'{head:x} {body:x}'
            num -= 1
            str = bytes.fromhex(val).decode('gb2312',errors = 'ignore')
            strs = strs+str
        return strs
    
    @classmethod
    def sjzf(cls,num1=3,num2=3,req='lnu',opt=''):
        num1 = int(num1)
        num2 = int(num2)
        if num1 >= num2:
            num1,num2 = num2,num1
        if len(req) > num1:
            return None#"Input error, minimum length is less than required type"
        elif ('l' not in req.lower()) and ('n' not in req.lower())and \
                 ('u' not in req.lower())and ('p' not in req.lower()):
            return None#"Input error, required type parameter error，req please input:l n u p"
        else:
            opts = []
            zfc = ''
            if ('n' in req) or ('N' in req):
                zf = cls.numb()
                zfc = zfc + zf
                opts.append("cls.numb()")
            if ('l' in req) or ('L' in req):
                zf = cls.lowl()
                zfc = zfc + zf
                opts.append("cls.lowl()")
            if ('u' in req) or ('U' in req):
                zf = cls.uppl()
                zfc = zfc + zf
                opts.append("cls.uppl()")
            if ('p' in req) or ('P' in req):
                zf = cls.punc()
                zfc = zfc + zf
                opts.append("cls.punc()")
            if ('n' in opt) or ('N' in opt):
                opts.append("cls.numb()")
            if ('l' in opt) or ('L' in opt):
                opts.append("cls.lowl()")
            if ('u' in opt) or ('U' in opt):
                opts.append("cls.uppl()")
            if ('p' in opt) or ('P' in opt):
                opts.append("cls.punc()")
        
            num = random.randint(num1,num2)
            while num > len(req):
                zf = eval(random.choice(opts))
                num -= 1
                zfc = zfc + zf
            zfc_list = list(zfc)
            random.shuffle(zfc_list)
            return ''.join(zfc_list)

    @classmethod
    def get_str(cls):
        random_str = random.choice(cls.custom_str)
        return random_str
            
    @classmethod
    def add_str(cls,r_string):
        if type(r_string)== str:
            cls.custom_str.append(r_string)
        if type(r_string)==list:
            cls.custom_str=cls.custom_str+r_string
        else:
            cls.custom_str.append(str(r_string))
        
    @classmethod
    def update_str(cls,oldstr,newstr):
        if oldstr in cls.custom_str:
            cls.custom_str=cls.custom_str.remove(oldstr)
            cls.custom_str=cls.custom_str.append(newstr)
            return newstr
        else:
            return None

    @classmethod
    def del_str(cls,r_string):
    #如果存在，则删除。如果不存在。则返回none
        if r_string in cls.custom_str:
            cls.custom_str.remove(r_string)
            return r_string
        else:
            return "This string is not in here"
        
    @classmethod
    def get_strs(cls):
        #random_str = random.choice(cls.custom_str)
        return cls.custom_str
