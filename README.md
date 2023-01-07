# InstaLikeChecker

### Who didn't like my post?!

#### my third freelancing project :)

Welcome to our Instagram web crawler! With this Python-based tool, you can easily sign in to your Instagram account and see who has liked a specific post. Simply provide the post URL and the crawler will retrieve a list of all the usernames that have liked it.

This can be a useful tool for tracking engagement on your posts or for seeing who is showing support for your content. We hope you find it useful! If you have any feedback or encounter any issues while using the crawler, please don't hesitate to let us know.

### How to use?
1. Clone or download this repository.
2. Install selenium:
```
pip install selenium
```
3. Write your username and password in [login_data.ini](https://github.com/ChamRun/InstaLikeChecker/blob/main/login_data.ini), and post url and and username in [InstaLikeChecker.py](https://github.com/ChamRun/InstaLikeChecker/blob/main/InstaLikeChecker.py).<br><br>

   If you're using Windows and Firefox or Chrome, go to the 6th step, else:

4. Download your favourite browser driver from:
   + [Chrome](https://chromedriver.chromium.org/downloads)
   + [Firefox](https://github.com/mozilla/geckodriver/releases)
   + [Edge](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
   + [Opera](https://github.com/operasoftware/operachromiumdriver/releases)
   + [Internet Explorer](https://www.selenium.dev/downloads/)

5. Paste driver in your project directory.
 
6. Run [InstaLikeChecker.py](https://github.com/ChamRun/InstaLikeChecker/blob/main/InstaLikeChecker.py).<br><br>


You can learn how to get the XPath [from here](https://stackoverflow.com/a/42194160/14761615).

If you're interested, maybe you would like [this repository](https://github.com/ChamRun/Unrequester) too.
