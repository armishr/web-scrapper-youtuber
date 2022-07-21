# web-scrapper-youtuber
The main aim of this project was to first collect about 100 links of videos from a youtubers page, then from each link extract ~500 top comments
along with the number of likes in each comment and the meta data of the video like "Likes","Subscriber Count","Comment Count","title" etc.
Originally, this project was supposed to be a part of an NLP project for sentiment analysis but because of not being able to resolve issues
such as typos, large amount of sparse words (even with approx 50,000 comments), people speaking in different languages etc, I could not do
what I originally intended to do, though I may look into doing this again in the future. Nevertheless, the scrapping of comments is still useful
and can give large amounts of dataset with just a minimal amount of input.

The program has two parts: First,it takes in the link of the page where the list of videos are stored. This returns approx ~100 videos though this can be configured.
Then, each link is passed through another program which extracts approx 500 comments. Again, this can be adjusted as well.
I ran this program on videos of Taylor Swift, and have posted the results in this repo. You can view the datasets using Panda dataframes.
