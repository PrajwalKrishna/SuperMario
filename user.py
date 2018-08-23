def get_key(key):
    for x in _allowed_inputs:
        if key in _allowed_inputs[x]:
            return x
    return False

# Gets a single character from standard input.  Does not echo to the screen.
class _Getch:
    def __init__(self):
        try:
            self.impl = _getChWindows()
        except ImportError:
            self.impl = _getChUnix()

    def __call__(self):
        return self.impl()


class _getChUnix:
    '''class to take input'''

    def __init__(self):
        '''init def to take input'''
        import tty
        import sys

    def __call__(self):
        '''def to call function'''
        import sys
        import tty
        import termios
        fedvar = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fedvar)
        try:
            tty.setraw(sys.stdin.fileno())
            charvar = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fedvar, termios.TCSADRAIN, old_settings)
        return charvar


class _getChWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


_getch = _Getch()


class AlarmException(Exception):
    '''This class executes the alarmexception.'''
    pass


def alarmHandler(signum, frame):
    raise AlarmException


def getInput(timeout=0.4):
    import signal
    signal.signal(signal.SIGALRM, alarmHandler)
    signal.setitimer(signal.ITIMER_REAL, timeout)
    try:
        text = _getch()
        signal.alarm(0)
        return text
    except AlarmException:
        pass
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''
