import os

def numCPUs():
    if not hasattr(os, "sysconf"):
        raise RuntimeError("No sysconf detected.")
    return os.sysconf("SC_NPROCESSORS_ONLN")

bind = "0.0.0.0:8737"
workers = 8
backlog = 2048
worker_class = "gevent"
debug = True
daemon = False
pidfile ="/tmp/gunicorn_v0.pid"
logfile ="/tmp/gunicorn_v0.log"
loglevel = 'info'
accesslog = '/tmp/gunicorn-access-v0.log'
timeout = 50
