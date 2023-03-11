from http.server import BaseHTTPRequestHandler

from io import BytesIO
from matplotlib.figure import Figure
import base64

# Shot chart imports
import arrow
import json
import matplotlib.pyplot as plt
import os
import requests

from datetime import datetime as dt
from hockey_rink import NHLRink
from PIL import Image

from matplotlib import image
from matplotlib import cm
from matplotlib.patches import Circle, Rectangle, Arc, ConnectionPatch
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.path import Path
from matplotlib.patches import PathPatch


class handler(BaseHTTPRequestHandler):
    def generate_image(self):
        # Generate the figure **without using pyplot**.
        fig = Figure()
        ax = fig.subplots()
        ax.plot([1, 2])

        # Save it to a temporary buffer.
        buf = BytesIO()
        fig.savefig(buf, format="png")
        data = base64.b64encode(buf.getbuffer()).decode("ascii")
        b64img = '<img src="data:image/png;base64,{}" />'.format(
            data)
        return b64img

    def do_GET(self):
        data = self.generate_image()

        # Send our response and headers
        self.send_response(200)

        self.send_header('Content-Type', 'text/html')
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()

        self.wfile.write(data.encode())

        return
