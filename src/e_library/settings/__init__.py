import os


if os.getenv("shyamkumaryadav"):
    from .prod import *
else:
    from .dev import *
