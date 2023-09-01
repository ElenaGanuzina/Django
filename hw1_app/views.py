import logging
from datetime import datetime
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def main(request):
    html = f"<h1>Welcome to the Linguist's Closet!</h1>" \
           f"<h2>If language is your passion, you're in the right place</h2>" \
           f"<p>I mean all sorts of languages: natural, artificial, programming... Whatever!</p>"

    logger.info(f'Page "main" was visited at {datetime.now()}')
    return HttpResponse(html)


def about(request):
    html = f"<h1>Some info about me.</h1>" \
           f"<h3>My name is Helen and this is my first Django website.</h3>" \
           f"<p>And as you've probably guessed my passion is all kinds of languages.</p>" \
           f"<p>Here are some langs I know more or less tolerably well:</p>" \
           f"<ul>" \
           f"<li>Natural: English, French, Spanish, Japanese, Maori, Arabic, Latin</li>" \
           f"<li>Artificial: Quenia, Sindarin</li>" \
           f"<li>Programming: Python, Java</li>" \
           f"</ul>" \
           f"<h3>And what is your favourite language?</h3>"

    logger.info(f'Page "about" was visited at {datetime.now()}')
    return HttpResponse(html)
