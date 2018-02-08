from flask import Flask, jsonify, request
from werkzeug.contrib.fixers import ProxyFix
import os
import logging
import logstash
import sys

 def get_remote_addr(self, forwarded_for):
        """Selects the new remote addr from the given list of ips in
        X-Forwarded-For.  By default the last one is picked. Specify
        num_proxy_servers=2 to pick the second to last one, and so on.
        """
        if self.detect_misconfiguration and not forwarded_for:
            raise Exception("SaferProxyFix did not detect a proxy server. Do not use this fixer if you are not behind a proxy.")
        if self.detect_misconfiguration and len(forwarded_for) < self.num_proxy_servers:
            raise Exception("SaferProxyFix did not detect enough proxy servers. Check your num_proxy_servers setting.")

        if forwarded_for and len(forwarded_for) >= self.num_proxy_servers:
            return forwarded_for[-1 * self.num_proxy_servers]

    def __call__(self, environ, start_response):
        getter = environ.get
        forwarded_proto = getter('HTTP_X_FORWARDED_PROTO', '')
        forwarded_for = getter('HTTP_X_FORWARDED_FOR', '').split(',')
        forwarded_host = getter('HTTP_X_FORWARDED_HOST', '')
        environ.update({
            'werkzeug.proxy_fix.orig_wsgi_url_scheme':  getter('wsgi.url_scheme'),
            'werkzeug.proxy_fix.orig_remote_addr':      getter('REMOTE_ADDR'),
            'werkzeug.proxy_fix.orig_http_host':        getter('HTTP_HOST')
        })
        forwarded_for = [x for x in [x.strip() for x in forwarded_for] if x]
        remote_addr = self.get_remote_addr(forwarded_for)
        if remote_addr is not None:
            environ['REMOTE_ADDR'] = remote_addr
        if forwarded_host:
            environ['HTTP_HOST'] = forwarded_host
        if forwarded_proto:
            environ['wsgi.url_scheme'] = forwarded_proto
        return self.app(environ, start_response)

from saferproxyfix import SaferProxyFix
app.wsgi_app = SaferProxyFix(app.wsgi_app)

#if 'LOG_HOST' not in os.environ:
#    raise(Exception("LOG_HOST NOT DEFINED"))

#host = os.environ['LOG_HOST']

host = google.com

test_logger = logging.getLogger('python-logstash-logger')
test_logger.setLevel(logging.INFO)
test_logger.addHandler(logstash.TCPLogstashHandler(host, 80, version=1))

app = Flask(__name__)

def log_request(req):
    extra = {
        'ip': request.environ.get('X-Forwarded-For', request.remote_addr),
        'url': req.full_path,
    }
    test_logger.info('honeypot: ', extra=extra)

#    data_to_log.update(req.headers)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')

#app.wsgi_app = ProxyFix(app.wsgi_app)

def honey(path):
    log_request(request)
    return jsonify({'result': 'ok'})

if __name__ == '__main__':
app.run(host="0.0.0.0",port=8080)
