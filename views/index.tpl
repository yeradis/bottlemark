<!DOCTYPE html>
<html>
  %include head title="Welcome"
  <body>
      
      <div class="container-narrow">

      %include header.tpl

      <div class="jumbotron">
        <h1>Super awesome Bottle Mark!</h1>
        <p class="lead">A simple/plain blog powered by python + bottle + markdown2 with wiki-tables extra. Using static *.md files</p>
      </div>

      <hr>

    <ul class="unstyled">
    %for key in archive:
       <li>
        <div class="archive_list_item">
            <div class="dateblock" style="float: left;">
            <div class="month">{{key["date"].split('-')[1] }} </div>
            <div class="day"> {{key["date"].split('-')[2] }} </div>
            <div class="year"> {{key["date"].split('-')[0] }} </div>
          </div> 
          <div class="title">
            <a href="{{key["file"]}}"> <h1>{{key["title"]}}</h1></a>
          </div>
        </div>
      </li>
      <br>
    %end
    </ul>



	  %include footer.tpl
  </div>
    <script src="/static/bootstrap/js/bootstrap.min.js"></script>
  </body>
</html>