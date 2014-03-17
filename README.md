legoit
======

### Website to show reddit user /u/icanlegothat awesome creations  

Live at http://legoit.dam.io  

##Installation

To install it, make sure you have Python 3.3 or greater installed (did't test it . Then run
these command in a new virtualenv:

    pip install -r requirements.txt
    python manage.py migrate
    python runserver

And go to http://localhost:8000 as usual, but there will be no content.  
I developed it using the latest django trunk master version (1.7r2) to have migrations, you're free to make it compatible for an earlier version.  

To get the latest reddit comments, you have to run this command:

    python manage.py retrieve_data
  
And wait, it will take approximately 2min

##Contributing

Have fun, don't hesitate to send me pull requests or file an issue. Here is a few things I need to improve:

* Switch to a master/dev branching and continuous integration developement
* Unit and integration testing, especially for the reddit API calls and the comment parsing
* Better parsing of the comments (the current one is really naive)
* Better admin interface to edit the posts
* Using it for another user (like ShittyWaterColor or AWildSketchAppereared)
* Deployement using Heroku
* Error reporting
