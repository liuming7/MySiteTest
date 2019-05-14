"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

import MySiteTest.views
import MySiteTest.datasets
import MySiteTest.visualization

