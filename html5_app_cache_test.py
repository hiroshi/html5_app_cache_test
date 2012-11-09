import webapp2
import jinja2
import os

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainPage(webapp2.RequestHandler):
  def get(self):
      # self.response.headers['Content-Type'] = 'text/plain'
      # self.response.write('Hello, webapp2 World!')
      template = jinja_environment.get_template('index.html')
      self.response.out.write(template.render({}))


app = webapp2.WSGIApplication([('/', MainPage)],
                              debug=True)
