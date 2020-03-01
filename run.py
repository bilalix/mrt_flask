# -*- coding: utf-8 -*-
"""
    Main portal to the app!
    (LOL I had to add this module docstring for the lint to pass
    Yes, I didn't want to suppress the warning)
"""

from app import app

app.run(host="0.0.0.0", port=8080, debug=True)
