# emoji
use emoji in python web.


## How to use

1. copy [emoji.py](emoji/emoji.py) to your project

    import it when use:

    ```python
    from emoji import emoji
    ```

2. add css

    copy [emoji.css](emoji/emoji.css) content to your style.css file.

3. add to the code

    for example, if you want your commet system support emoji. you can do like this:

    a. when someone leave a commet "`:smile:`"

    b. "`:smile:`" will be submitted to your python code when submit the comment

    c. use regex to check the emoji and then use html code replace it

    read [check_emoji.py](emoji/check_emoji.py) for details.
