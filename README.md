# time-it
Short snippet to log a function's duration and keyword arguments


## Usage exemple
```python
import time
from helpers import log_duration # Assuming the script is located in a helpers file


@log_duration
def sleeper(duration: int):
    print('Good night 😴')
    time.sleep(duration)
    print('Wake up ⏰')
    return 'Done!'

print(sleeper(duration=5))
#  >>>
# Good night 😴
# Wake up ⏰
# 5.00s for sleeper duration: 5
# Done!
```
