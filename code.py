#coding:utf-8
import web
import urllib
import sys,os

urls = (
        '/', 'index',
        '/movie/(.*)', 'movie',
        '/cast/(.*)', 'cast',
        '/casts/(.*)', 'casts',
        '/castA/(.*)', 'castA',
        '/', 'test',
        '/simple', 'simple',
        '/zhongwen/(.*)', 'zhongwen',
        '/param/(.*)', 'param',
)

if sys.getdefaultencoding() != 'utf-8':
        reload(sys)
        sys.setdefaultencoding('utf-8')

casts_url = []
render = web.template.render('templates/')
db = web.database(dbn='sqlite', db='MovieSite3.db3')

class index:
        def GET(self):
        #return "Hello, world! Hello, bill!"
                '''page = ''
                for m in movies:
                        page += '%s (%d)\n' % (m['title'], m['year'])
                return page'''
                movies = db.select('movie')
                #num = len(list(movies))
                #movies = db.select('movie')
                num = db.query('SELECT COUNT(*) AS COUNT FROM movie')[0]['COUNT']
                return render.index(movies, num, None)

        def POST(self):
                data = web.input()
                condition = r'title like "%' + data.title + r'%"'
                movies = db.select('movie', where=condition)
                #num = len(list(movies))
                #movies = db.select('movie', where=condition)
                num = db.query('SELECT COUNT(*) AS COUNT FROM movie WHERE ' + condition)[0]['COUNT']
                return render.index(movies, num, data.title)

class movie:
	def GET(self, movie_id):
		movie_id = int(movie_id)
		movie = db.select('movie', where='id=$movie_id', vars=locals())[0]
		casts = movie.casts.split(',')
		del casts_url[:]
		for cast in casts:
                        casts_url.append(urllib.parse.quote(cast))
		return render.movie(movie, casts_url)

class cast:
	def GET(self, cast):
                h = web.input()
                cast_name = h.cast
                condition = r'casts like "%' + cast_name + r'%"'
                movies = db.select('movie', where=condition)
                num = len(list(movies))
                movies = db.select('movie', where=condition)
                return render.index(movies, num, None)
		#web.header('Content-Type','text/html;charset=utf-8')
		#cast_this = cast_name.encode('utf8')
		#cast_this = cast_name.encode('utf-8').decode('unicode_escape')
		#cast_this = urllib.parse.unquote(cast_name)
		#return render.test(cast_this)

class casts:
	def GET(self, cast):
                condition = r'casts like "%' + cast + r'%"'
                movies = db.select('movie', where=condition)
                num = len(list(movies))
                movies = db.select('movie', where=condition)
                return render.index(movies, num, None)
		#web.header('Content-Type','text/html;charset=utf-8')
		#cast_this = cast.encode('utf8')
		#cast_this = cast.encode('utf-8').decode('unicode_escape')
		#cast_this = urllib.parse.unquote(cast)
		#return render.test(cast_this)

class castA:
	def GET(self, cast):
                h = web.input(cast=None)
                condition = r'casts like "%' + cast + r'%"'
                movies = db.select('movie', where=condition)
                num = len(list(movies))
                movies = db.select('movie', where=condition)
                return render.index(movies, num, None)
		#web.header('Content-Type','text/html;charset=utf-8')
		#cast_this = cast.encode('utf8')
		#cast_this = cast.encode('utf-8').decode('unicode_escape')
		#cast_this = urllib.parse.unquote(cast)
		#return render.test(cast_this)

class simple:
    def GET(self):
        web.header('Content-Type','text/html;charset=UTF-8')
        return 'Hello Word!你好!'

class zhongwen:
        def GET(self, param_name):
                print (param_name)
                return render.test(param_name)
	
class param:
        def GET(self, first):
                h = web.input()
                return render.test(h.first)

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()

movies = [
    {
	'title': 'Forrest Gump',
	'year': 1994,
    },
    {
	'title': 'Titanic',
	'year':	1997,
    },
]
