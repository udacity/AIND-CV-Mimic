# Project: Mimic Me!


## Overview

In this project, you will learn to track faces in a video and identify facial expressions using Affectiva. As a fun visualization, you will tag each face with an appropriate emoji next to it. You will then turn this into a game where the player needs to mimic a random emoji displayed by the computer!


## Getting Started

We’ll be using [Affectiva](http://www.affectiva.com/)’s Emotion-as-a-Service API for this project. Visit their [Developer Portal](http://developer.affectiva.com/) and try out some of the sample apps. Affectiva makes it really easy to extract detailed information about faces in an image or video stream. To get a sense for what information you can obtain, check out the [Metrics](http://developer.affectiva.com/metrics/) page.

### Project files

To start working on the project, open the following files in your favorite text editor:

- **mimic.js**: Javascript file with code that connects to the Affectiva API and processes results.
- **index.html**: Dynamic webpage that displays the video feed and results.
- **mimic.css**: Stylesheet file that defines the layout and presentation for HTML elements.

_You only need to implement the TODOs in mimic.js to complete the project. But feel free to modify the HTML and/or CSS file to change the look and feel of your game!_

There are two additional files provided for serving your project as a local web application - you do not need to make any changes to them:

- **serve.py**: A lightweight Python webserver required to serve the webpage over HTTPS, so that we can access the webcam feed.
- **generate-pemfile.sh**: A shell script you’ll need to run once to generate an SSL certificate for the webserver.

### Serving locally over HTTPS

In order to access the webcam stream, modern browsers require you to serve your web app over HTTPS. To run locally, you will need to general an SSL certificate (this is a one-time step):

- Open a terminal or command-prompt, and ensure you are inside the `AIND-CV-Mimic/` directory.
- Run the following shell script: `generate-pemfile.sh`

This creates an SSL certificate file named `my-ssl-cert.pem` that is used to serve over https.

Now you can launch the server using:

```
python serve.py
```

_Note: The `serve.py` script uses Python 3._

Alternately, you can put your HTML, JS and CSS files on an online platform (such as [JSFiddle](https://jsfiddle.net/)) and develop your project there.

### Running and implementing the game

Open a web browser and go to: [https://localhost:4443/](https://localhost:4443/)

- Hit the Start button to initiate face tracking. You may have to give permission for the app to access your webcam.
- Hit the Stop button to stop tracking and Reset to reset the detector (in case it becomes stuck or unstable).
- Modify the Javascript code to implement TODOs as indicated in inline comments. Then refresh the page in your browser (_you may need to do a "hard-refresh" for the changes to show up, e.g. `Cmd+Shift+R` on a Mac), or use an auto-reload solution._
- When you’re done, you can shutdown the server by pressing `Ctrl+C` at the terminal.

_Note: Your browser may notify you that your connection is not secure - that is because the SSL certificate you just created is not signed by an SSL Certificate Authority‎. This is okay, because we are using it only as a workaround to access the webcam. You can suppress the warning or choose "Proceed Anyway" to open the page._


## Tasks

The starter code sends frames from your webcam to Affectiva’s cloud-based API and fetches the results. You can see several metrics being reported, including emotions, expressions and the dominant emoji!

### 1. Display Feature Points

Your first task is to display the feature points on top of the webcam image that are returned along with the metrics.

To do this, open up mimic.js, and implement the `drawFeaturePoints()` function:

```javascript
function drawFeaturePoints(canvas, img, face) {
    ...
}
```

### 2. Show Dominant Emoji

In addition to feature points and metrics that capture facial expressions and emotions, the Affectiva API also reports back what emoji best represents the current emotional state of a face. This is referred to as the _dominant emoji_.

In mimic.js, implement the `drawEmoji()` function to display this emoji on top of the webcam feed, tracking the user's face:

```javascript
function drawEmoji(canvas, img, face) {
    ...
}
```

### 3. Implement Mimic Me!

Now it's your turn to implement the game mechanics and make it as fun as possible! Scroll down to the bottom of mimic.js for more instructions. Feel free to modify the HTML and/or CSS files to change the look and feel of the game as well.


## Extensions

Sky’s the limit on where you can take this project! Feel free to share with your friends and family. You can host it online to make it available to everyone.

Some ideas for extensions:

- Make it a 2 player game, like Guitar Hero, where you compete with someone to mimic as many emojis as you can out of a streaming sequence of them.
- Pair a stream of emojis with a script and have the player read the script, interspersed with emotional expressions that are checked by the computer. Great for some acting practice!


## Affectiva Resources

As you work on your code, you may have to refer to resources in Affectiva's [JS SDK documentation](https://affectiva.readme.io/docs/getting-started-with-the-emotion-sdk-for-javascript).

Other references:

- [Affectiva Developer portal](http://developer.affectiva.com/index.html)
- [Demo](https://jsfiddle.net/affectiva/opyh5e8d/show/) that this project is based on
- Tutorials:
 [Camera stream](https://affectiva.readme.io/docs/analyze-the-camera-stream-3), [video](https://affectiva.readme.io/docs/analyze-a-video-frame-stream-4), [photo](https://affectiva.readme.io/docs/analyze-a-photo-3)


<a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>. Please refer to [Udacity Terms of Service](https://www.udacity.com/legal) for further information.
