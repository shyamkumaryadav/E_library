import os

if os.getenv("prod"):
    from .prod import *
else:
    from .dev import *
