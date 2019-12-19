from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.cache import cache
from django.utils.cache import get_cache_key


class Check_request(MiddlewareMixin):
    import time
    dic = {}
    dic['time'] = time.time() #用于记录这次单次请求的起始时间

    def process_request(self, request):
        id = request.META['REMOTE_ADDR']
        import time
        self.dic.get(id, 0)
        self.first_time = time.time()
        if time.time() - self.dic['time'] > 10:#如果禁止时间超出了10s 就解除禁止
            self.dic[id] = 0
        uid = request.COOKIES.get('e_token','s1')
        if uid == 's1':
            key = get_cache_key(request)
            if cache.has_key(key):
                cache.delete(key)
            return
        else:
            key = get_cache_key(request)
            if cache.has_key(key):
                cache.delete(key)
            return
    def process_response(self, request, response):
        import re
        import time
        target_time = time.time() - self.dic['time']
        environment = request.environ
        # print(environment)
        target = environment['HTTP_USER_AGENT']
        # print(target)
        id = request.META['REMOTE_ADDR']
        re_result = re.findall(r'^Mozilla/|^S', target,re.S|re.M)
        num = self.dic.get(id,0)
        if num < 10:#判断单秒内是否超过10次访问
            if re_result:
                if target_time <= 1:#单击时间小于１秒
                    self.dic[id] = num + 1
                    return response

                else:
                    self.dic[id]=0 #单击时间大于１秒,重新记０
                    self.dic['time'] = self.first_time
                    return response
            else:
                return Http404
        return Http404
