CSS:
As a quick reference site, I inferred that my users would overwhelmingly trend towards accessing my site on mobile.
This was verified later through "market research" (i.e. asking all my friends in the ballroom community what they thought).
As such, I spent a lot of time on this project, specifically in the CSS, trying to make sure that everything sized correctly and looked nice on a mobile screen.
Where there was a decision to be made between how the site looked on desktop and how the site looked on mobile, I chose to engineer the site to look nicer on mobile every time.
I specifially did NOT create an app. No one likes having to download apps onto their phone for every little thing.
It's not much, but I am fairly proud of the time I put into creating the color scheme, screen placement, and button styles for my website.
At one point there was even a cover image that went behind the text, but I felt that this was against the quick-and-easy-reference theme that my site was going for, so I ended up taking it out.

JINJA:
As there are so, so many different dance figures I wanted to display gifs for, I knew that the site would have to dynamically load a gif based on its name.
This saved me the struggle of needing to create possibly a hundred different html files, one for each dance figure.
Right now, this works because each button sends back datat to the Python app, telling to load a differently-named gif depending on which button was pressed.
I couldn't think of a better system for this than to create a "serial number" or "ID number" system by which to represent all of the dance moves.
The python app then loks for a gif by that name in the "static" folder.
For details on the aning system I used, see "Gif_naming_Notes.txt".
On the technical side, this part is all complete.
As far as dance content is concerned, only Smooth is complete; the remainder of the dance figure buttons link to either a placeholder gif or a "Coming Soon" page.

I realize that it is theoretically possible to store the information about the dances and their figures in a SQL table and generate the 19 different dance figure syllabus pages dynamically, too.
However, I decided against this for two main reasons:
1. What figures are in what dances isn't going to change or need updating.
2. There are only 19 dances, anyway.
So, I thought it would be faster to just hardcode the inforrmation in static html pages rather than devise a system to try and generate them from tables that werewere oging to be static anyway.

This whole process ended up taking WAY longer than I thought it would to implement.
This was due to silly bugs in my code and also because of how Flask handles graphics.
I had set up a very organized system for storing my gifs and images, with many folders.
Imagine the moment when I realized that these all had to be stored within "static"!
Fortunately, someone at the Hackathon asked a similar question, and I was able to resolve this, but not after I had lost a lot of time Googling furiously why nothing would load.