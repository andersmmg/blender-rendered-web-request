# https://github.com/andersmmg/blender-rendered-web-request

bl_info = {
    "name" : "Rendered Web Request",
    "blender": (2, 90, 0),
    "category": "Render",
    "author": "Andersmmg",
    "description": "Makes a basic HTTP request when a render is complete"
}

import bpy
from bpy.app.handlers import persistent
from bpy.props import *
from bpy.types import Operator, AddonPreferences
import requests

@persistent
def make_request(dummy):
    # Get the name of the blend file
    blend_name = bpy.path.basename(bpy.context.blend_data.filepath)
    # Make the request!
    # TODO: Change the url to whatever you want to use
    res = requests.get("http://example.com/?filename="+blend_name)
    print(res.text)

def register():
    bpy.app.handlers.render_complete.append(make_request)

def unregister():
    bpy.app.handlers.render_complete.remove(make_request)

if __name__ == "__main__":
    register()
# You can paste this into the built-in editor to test it
