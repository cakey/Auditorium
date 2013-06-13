# What is this?

The purpose of this is to create 6-10 playlists of separate music genres.

While it is possible to manually create these playlists, it is difficult to categorise the music, and you are likely to end up with uneven size playlists that don't accurately reflect the music collection.

The approach I want to take is to ignore any properties of the music itself (beat/instruments/melody/etc), and focus on using existing crowdsourced genre tags from existing music services. Artists that are similar will share more genre tags than dissimilar artists. By clustering on this, it is hoped that reasonable playlists will be produced!

# Implementation

## Music Sources

Knowledge of your music collection could come from a number of sources, eg lastfm/spotify/local etc.

### iTunes

iTunes uses a their own data format, but a quick google finds a parser. (Well, it's just XML, but I'm lazy...)

## Genre Sources

Using the API of a music service seems like the best idea, for example [last.fm](http://www.last.fm/api/show/artist.getTopTags), but I wanted an excuse to use the services that are attempted to make wikipedia queryable such as [DBpedia](http://dbpedia.org/About) and (similar idea, but not using wikipedia) [freebase](http://www.freebase.com/).  
Services that structure data are very exciting, as it will open up the vast array of information on wikipedia and other sources to applications allowing visualisation and analysis of the data for educational purposes. You could automatically generate a map and timeline of all the major battles and key events of any war, or the major discoveries and people of the industrial revolution or the change over time of popular music genres.

### DBpedia


 # Tools & Libraries

 - [Parser for itunes property lists](https://github.com/ishikawa/python-plist-parser)