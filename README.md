Bottlemark
===========


A simple Python CMS? built with  Bottle web framework and Markdown2

So simple that no database is required.

Just write your content using the Markdown syntax and place your file in contents folder, the file name must use this format: 

yourfilenamehere.md

where .md extension is needed.

Also, the first lines of the file must be:

    Title: The Title of the page
    Date: The date using the format yyyy-MM-dd
    Author: The author name
    
This info is used when transforming to HTML, this info will not be shown using this format on the browser. But you will be able to see it on the web. 

How ?

BottleMark is also using Bottle Templates, for example check the default layout.tpl for contents:


    <!DOCTYPE html>
    <html>
      %include head title=title
      <body>
          
          <div class="container-narrow">
    
            %include header.tpl
            
            <h1>{{!title}}</h1>
            <h4>{{!author}}</h4>
            <h6>{{!date}}</h6>
            <hr/>
            
            {{!content}}
          
            %include footer.tpl
          </div>
        
        
        <script src="/static/bootstrap/js/bootstrap.min.js"></script>
      </body>
    </html>


So, those firsts lines of your .md in the template correspond to

{{!title}}

{{!author}}

{{!date}}

The remaining, the content goes here.

{{!content}}
            

So, lets try it.

First, run the app:

    python app.py
    
This will run as a standalone and lightweight WSGI app.

Then point your browser to http://localhost:8080/

That’s it. 

There will appear the index page showing some samples already available in contents


---------

You can install Bottle and Markdown2 using the provided requirements.txt

    pip install -r requirements.txt
    
