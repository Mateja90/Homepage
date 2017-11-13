#!/usr/bin/env python
import os
import jinja2
import webapp2


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if params is None:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        besedilo="Lorem Ipsum is simply dummy text of the printing and typesetting industry."

        params={"tekst":besedilo}
        return self.render_template("hello.html", params = params)

class OMeniHandler(BaseHandler):
    def get(self):
        besedilo1="It has been proven that comprehensible content, while scanning the design solution of a particular page, undesirable redirects the reader's attention. Since Lorem Ipsum has a relatively even distribution of characters, it successfully replaces temporary, substantively meaningful texts. Many desktop publishing programs and online editors use Lorem Ipsum as the default blank text. Therefore, a web search with the keywords lorem ipsum returns many hits to unfinished websites. Over the years, many versions of this blind text have been created, either unplanned or deliberately, with various humorous and other inputs."
        params={"tekst1":besedilo1}
        return self.render_template("omeni.html", params=params)
class MojiProjektiHandler(BaseHandler):
    def get(self):
        besedilo2="It has been proven that comprehensible content, while scanning the design solution of a particular page, undesirable redirects the reader's attention. Since Lorem Ipsum has a relatively even distribution of characters, it successfully replaces temporary, substantively meaningful texts. Many desktop publishing programs and online editors use Lorem Ipsum as the default blank text. Therefore, a web search with the keywords lorem ipsum returns many hits to unfinished websites. Over the years, many versions of this blind text have been created, either unplanned or deliberately, with various humorous and other inputs."
        params={"tekst2":besedilo2}
        return self.render_template("projekti.html", params=params)
class BlogHandler(BaseHandler):
    def get(self):
        sporocilo = "Na tej strani se nahajajo moji blogi."

        blog_posts = [{"title": "Prvi blog", "text": "test, pa da vidimo"},
                {"title": "Drugi blog", "text": "test, pa da vidimo drugic"},]

        params={"sporocilo2": sporocilo, "blogs": blog_posts}
        return self.render_template("blog.html", params=params)
class KontaktHandler(BaseHandler):
    def get(self):
        podatki="email: ime@gmail.com"
        params={"pod":podatki}
        return self.render_template("kontakt.html", params=params)



app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/omeni', OMeniHandler),
    webapp2.Route('/projekti', MojiProjektiHandler),
    webapp2.Route('/blog', BlogHandler),
    webapp2.Route('/kontakt', KontaktHandler),
], debug=True)
