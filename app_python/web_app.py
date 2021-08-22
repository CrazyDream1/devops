import os.path
import cherrypy
import datetime


class HelloWorld:
    @cherrypy.expose
    def index(self):
        timezone = datetime.timezone(datetime.timedelta(hours=3))
        return datetime.datetime.now(tz=timezone).strftime('%Y-%m-%d %H:%M:%S')


tutconf = os.path.join(os.path.dirname(__file__), 'web_app.conf')

if __name__ == '__main__':
    cherrypy.quickstart(HelloWorld(), config=tutconf)
