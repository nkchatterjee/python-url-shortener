In this project I use the pyshorteners library, which implements well-known URL shortening APIs to help users both shorten and expand URLs. This avoids the necessity of installing separate libraries for each provider.

To use a shortening service, you do need to have an account for that service and obtain an access code. You'll create a file called `.env` in your root directory and save the access key in a variable called MY_ACCESS_TOKEN.

For this example, we'll use the bit.ly shortener. If you'd like to substitute another provider, read the [pyshorteners docs](https://pyshorteners.readthedocs.io/en/latest/apis.html) to modify the code in `shorten_url.py`.

If you'd like to use bit.ly, first [make a free account](https://bitly.com/a/sign_in). After doing so, go to the dropdown menu under your name in the right-hand corner. Select Group Settings and click on Advanced Settings. Click on the OAuth link and select Generate Access Token. Copy the token and save it to your `.env` file.

After you've cloned the repository to your local device and installed the dependencies outlined in `requirements.txt`, run the `shorten_url.py` file and respond to the prompts.

This program currently has limited functionality. It doesn't yet include error handling for bad URL inputs. If the URL entered to shorten is a bit.ly link, the program errors out. If the URL entered to length is not saved in bit.ly's API, the program errors out. Therefore, make sure you use valid links. 

Every time you want to either shorten or length a URL, just run the file again.

Thanks and enjoy!