# **coding: utf-8**
import time
import hashlib
from cgi import FieldStorage
import urllib

URL = 'https://openapi.ele.me/v2/{}'
ConsumerSecret = '49f06e48f8f45fbb1315697e85c543ec8ad89071'
ConsumerKey = 'YvCEDMOsk2'


class ElmVerify(object):

    def __init__(self, path_url, consumer_key=ConsumerKey, consumer_secret=ConsumerKey):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.timestamp = int(time.time())
        self.path_url = URL.format(path_url)
        self.params = {'consumer_key': self.consumer_key, 'timestamp': self.timestamp}

    def get_url(self):
        params = ('consumer_key=', self.consumer_key, '&sig=', self.gen_sig(), '&timestamp=', str(self.timestamp))
        return self.path_url + ''.join(params)

    def gen_sig(self):
        params = self.concat_params(self.params)

        to_hash = u'{}?{}{}'.format(
            self.path_url, params, self.consumer_secret
        ).encode('utf-8')

        sig = hashlib.new('sha1', to_hash).hexdigest()
        return sig

    @ staticmethod
    def concat_params(params):

        """	将输入参数排序并用&连接"""

        pairs = []
        for key in sorted(params):
            if key == 'sig':
                continue
            val = params[key]

            if not isinstance(val, FieldStorage):
                pairs.append("{}={}".format(key, val))
        return '&'.join(pairs)


if __name__ == '__main__':
    elm_verify = ElmVerify(path_url='restaurant/62028381/')
    print(elm_verify.get_url())
