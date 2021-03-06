bl_info = {
    "name" : "Rendered Web Request",
    "blender": (2, 80, 0),
    "category": "Render",
    "author": "Andersmmg",
    "description": "Makes a basic HTTP request when a render is complete"
}

import bpy
from bpy.app.handlers import persistent
from bpy.props import *
from bpy.types import Operator, AddonPreferences
import requests

class RequestAddonPreferences(AddonPreferences):
    bl_idname = __name__

    request_url: StringProperty(
            name="Request URL",
            subtype='NONE',
            description="Use %s to replace with the filename in request\nExample: http://example.com/?filename=%s",
            )

    def draw(self, context):
        layout = self.layout
        layout.label(text="Use %s to replace with the filename in request")
        layout.prop(self, "request_url")
        layout.label(text="Example: http://example.com/?filename=%s")

@persistent
def make_request(dummy):
    user_preferences = bpy.context.preferences
    addon_prefs = user_preferences.addons[__name__].preferences
    
    # Get the name of the blend file
    blend_name = bpy.path.basename(bpy.context.blend_data.filepath)
    
    # Make the request!
    if addon_prefs.request_url != "":
        requests.get(addon_prefs.request_url % (blend_name))
        print("Web request made!")

def register():
    bpy.app.handlers.render_complete.append(make_request)
    bpy.utils.register_class(RequestAddonPreferences)

def unregister():
    bpy.app.handlers.render_complete.remove(make_request)
    bpy.utils.unregister_class(RequestAddonPreferences)

