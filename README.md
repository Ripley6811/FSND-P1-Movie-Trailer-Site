# Project 1: Movie Trailer Website

##Instructions

This website displays a few trailers for movies I've seen or want to see. Hovering over
a movie poster will display a popup description and a link to the "official" website
if available. Click anywhere on the movie tile, poster or description to watch a trailer.
Click the "Official Website" button to open the link in a new browser tab.

[Live view link (gh-pages)](http://ripley6811.github.io/FSND-P1-Movie-Trailer-Site/)


##Changes and additions

- Javascript moved from header template to `script.js`.
- CSS moved from header template to `styles.css`.
- Added description `div` with an optional button for opening another website.
- Added Google Fonts' `"Open Sans Condensed"` for all text.


##File descriptions

####`movie_trailers_list.txt`
- Contains a list of movie trailer data in JSON format with the following keys:

key | value
---|---
`title` | Movie title.
`trailer_url` | Link to Youtube trailer.
`image_url` | Movie poster image.
`website_url` | Official website or link to purchase movie.
`description` | An introductory description of the movie.

####`compile_website.py`
- Creates the static website by parsing the JSON file of trailer information and runs the fresh_tomatoes function.

####`media.py`
- Contains the `MovieTrailer` class for movie trailer info.

####`fresh_tomatoes.py`
- Code for creating a static website for displaying movie trailer images and videos.

####`styles.css`
- CSS styling for this single page website.

####`script.js`
- JavaScript for running this single page website.

####`favicon.ico`
- Small image for browser tab.

####`index.html`
- Compiled single page website. Created with `fresh_tomatoes.py`.


##Resources
[Adding a favicon](http://stackoverflow.com/questions/4888377/how-to-add-a-browser-tab-icon-for-a-website)
- Learn how to add a favicon.

[http://www.favicon.cc/](http://www.favicon.cc/)
- For creating and downloading a simple favicon for the website.

[Google Fonts](https://www.google.com/fonts)
- Selected "Open Sans Condensed" to replace the title font.

[CSS Gradient Generator](http://www.colorzilla.com/gradient-editor/)
- Create color and opacity gradients for a div.

[IMDB](http://www.imdb.com/)
- All synopses were copied from IMDB.

CSS `transition` code copied from an old project of mine.