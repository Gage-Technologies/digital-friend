# digital-friend
A VERY rudimentary implementation of a voice-to-voice chatbot. 


## Setup



### Installation

First clone the repository and run

```bash
pip install -r requirements.txt
```

### Tokens

You will need a huggingface access token.

Simply generate a token on the huggingface settings page.

Then create a `.env` file and place it in this variable inside the env

```bash
HUGGINGFACE_LOGIN=your-token-here
```

### Running

After that simply run the main and you're good to go!


## Known Bugs

Sometimes the program will fail to detect your audio device :(

I mad this in conjunction with a video that was posted on youtube so I may have time to look at that later.

For now I would suggest simply wrapping the `playsound("response.mp3")` in a try/except or using another library for the speak file.



## Possible Additions

As I mention in the video, I think it would be cool to have some kind of websearch tied to this porgram.

Although this comes with the territory of making the execution slower.

Definitely something to look inot if you want to play around with this.
