import os.path
import cherrypy
import datetime
import os

class HelloWorld:
    @cherrypy.expose
    def index(self):
        timezone = datetime.timezone(datetime.timedelta(hours=3))
        formated_time = datetime.datetime.now(tz=timezone).strftime('%Y-%m-%d %H:%M:%S')

        with open("./visits/visits.txt", "a") as visit_log:
            visit_log.write(formated_time + "\n")

        return formated_time

    @cherrypy.expose
    def visits(self):
        with open("./visits/visits.txt", "r") as visit_log:
            log = visit_log.read()
            return "<br>".join(log.split('\n'))

tutconf = os.path.join(os.path.dirname(__file__), 'web_app.conf')

if __name__ == '__main__':
    cherrypy.quickstart(HelloWorld(), config=tutconf)
