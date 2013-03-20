# -*- coding: UTF-8 -*-

import os
from bottle import route, run, view, static_file, error
import markdown2

contents     = "contents"

@error(404)
@view('error.tpl')
def error404(error):
    return {"title":"Error 404"}

@error(500)
@view('error.tpl')
def error500(error):
    return {"title":"Error 500"}


@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')

@route('/')
@view('index.tpl')
def index():
  archive = { 'archive' : archive_list()}
  return archive

def archive_list():
    contents_list = []
    title = ""
    date = ""
    author = ""
    ls = os.listdir( contents )
    for entry in ls:
        if ".md" == os.path.splitext( entry )[1]:
          with open(os.path.join(contents, entry),"r") as myfile:
            head=[myfile.next() for x in xrange(3)]
          page = {}
          if head[0].startswith("Title:"):
            page["title"] = head[0].replace("Title:","")
          if head[1].startswith("Date:"):
            page["date"] = head[1].replace("Date:","")
          if head[2].startswith("Author:"):
            page["author"] = head[2].replace("Author:","")
          
          page["file"]= "content/"+ entry
          contents_list.append(page )
    return contents_list

@route('/content/<name>', method='GET')
@view('layout.tpl')
def content_show( name="" ):
    if "" != name:
      markdown_content = ""
      title = ""
      date = ""
      author = ""
      f = open(os.path.join(contents, name),"r")
      lines = f.readlines()
      for line in lines:
        if not line.startswith("Title:") and not line.startswith("Date:") and not line.startswith("Author:") :
          markdown_content += line
        else:
          if line.startswith("Title:"):
            title = line.replace("Title:","")
          elif line.startswith("Date:"):
            date = line.replace("Date:","")
          elif line.startswith("Author:"):
            author = line.replace("Author:","")
          #print line
      f.close()
      print markdown_content
      #html = markdown2.markdown_path(os.path.join(contents, name) )
      html = markdown2.markdown(markdown_content,extras=["wiki-tables"])
      page = {}
      page["title"]= title
      page["content"]= html
      page["date"]= date
      page["author"]= author
      return page
    else:
      return { "success" : False, "error" : "show called without a filename" }

run(host='localhost', port=8080, debug=True)