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