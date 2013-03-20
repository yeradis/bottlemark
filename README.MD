#Bottlemark#

A simple **Python** CMS? built with **[Bottle](http://bottlepy.org/docs/dev/)** web framework and **[Markdown2](https://github.com/trentm/python-markdown2)**

So simple that no database is required.

Just write your content using the [Markdown](http://en.wikipedia.org/wiki/Markdown) syntax and place your file in **contents** folder, the file name must use this format: 

***yourfilenamehere.md*** 

where the **.md** extension is needed.

Your Markdown content will be translated to HTML on demand.

Lets try it.

First, run the core:

    python app.py
    
This will run as a standalone and lightweight WSGI app.

Then point your browser to http://localhost:8080/ 

That’s it.