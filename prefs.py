#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.



import bpy
from bpy.props import *
#from weed.text_editor_tools import (
#    find_replace
#)

#def register_find_replace(self, context):
#    if self.find_replace_pref:
#        find_replace.register()
#    else:
#        find_replace.unregister()

class SubmoduleGroup(bpy.types.PropertyGroup):

    level = IntProperty()
    name = StringProperty()
    icon = StringProperty()


class WeedPreferences(bpy.types.AddonPreferences):
    bl_idname = "weed"

    # api_nav_props
    anp_path = StringProperty(name='path',
            description='Enter bpy.ops.api_navigator to see the documentation',
            default='bpy')
    anp_old_path = StringProperty(name='old_path', default='')
    anp_filter = StringProperty(name='filter',
            description='Filter the resulting modules', default='')
    icg_filter = StringProperty(name='filter',
            description='Filter the resulting modules', default='')
    icg_old_filter = StringProperty(name='filter',
            description='Filter the resulting modules', default='n')
            # 'n' value just for trigger at first time
    anp_reduce_to = IntProperty(name='Reduce to ',
            description='Display a maximum number of x entries by pages',
            default=10, min=1)
    anp_pages = IntProperty(name='Pages',
            description='Display a Page', default=0, min=0)
    coed_last_text = StringProperty(name='last_text', default='')

    submodules = CollectionProperty(type=SubmoduleGroup)

    # weed_active_toolbox = EnumProperty(
    #     name = 'panel',
    #     default = 'draw_develop_box',
    #     items = [('draw_develop_box', 'Addon develop', '', 'SCRIPT', 0),
    #              ('draw_code_tree_box', 'Code tree', '', 'OOPS', 1),
    #              ('draw_debugger_box', 'Debugger tools', '', 'RECOVER_AUTO', 2)])

    # Features show in Menu
    show_bge_console = BoolProperty(
        name = "Show Bge Console Menu",
        description = "Show Bge Console Menu on Main Weed Menu",
        default = True)
    show_code_editor = BoolProperty(
        name = "Show Code Editor Menu",
        description = "Show Code Editor Menu on Main Weed Menu",
        default = True)
    show_icons_get = BoolProperty(
        name = "Show icons get Menu",
        description = "Show icons get Menu on Main Weed Menu",
        default = True)

    # Code Editor Preferences
    opacity = FloatProperty(
        name = "Panel Background transparency",
        description = "0 - fully opaque, 1 - fully transparent",
        min = 0.0, max = 1.0, default = 0.2)

    show_tabs = BoolProperty(
        name = "Show Tabs in Panel when multiple text blocks",
        description = "Show opened textblock in tabs next to minimap",
        default = True)

    minimap_width = IntProperty(
        name = "Minimap panel width",
        description = "Minimap base width in px",
        min = 25, max = 400, default = 100)

    window_min_width = IntProperty(
        name = "Hide Panel when area width less than",
        description = "Set 0 to deactivate side panel hiding, set huge to disable panel",
        min = 0, max = 4096, default = 600)

    symbol_width = FloatProperty(
        name = "Minimap character width",
        description = "Minimap character width in px",
        min = 1.0, max = 10.0, default = 1.5)

    line_height = IntProperty(
        name = "Minimap line spacing",
        description = "Minimap line spacign in px",
        min = 2, max = 10, default = 4)

    block_trans = FloatProperty(
        name = "Code block markings transparency",
        description = "0 - fully opaque, 1 - fully transparent",
        min = 0.0, max = 1.0, default = 0.6)

    indent_trans = FloatProperty(
        name = "Indentation markings transparency",
        description = "0 - fully opaque, 1 - fully transparent",
        min = 0.0, max = 1.0, default = 0.9)

    show_margin = BoolProperty(
        name = "Activate global Text Margin marker",
        default = True)

    margin_column = IntProperty(
        name = "Margin Column",
        description = "Column number to show marker at",
        min = 0, max = 1024, default = 80)

    #Register Unregister module Find Replace
    find_replace_pref = BoolProperty(#update=register_find_replace,
        name = "Find Replace fix",
        description = "popup version of find replace",
        default = True
    )

#### incorporar preferences del code autocomplete
# class AddonPreferences(bpy.types.AddonPreferences):
#     bl_idname = __name__

    line_amount = IntProperty(name = "Lines", default = 8,
                    min = 1, max = 20,
                    description = "Amount of lines shown in the context box")
    show_dot_files = BoolProperty(name = ' Show hidden files',
                    default = False,
                    description = 'Show hidden files on addon files panel')
    show_dot_addons = BoolProperty(name = 'Show dot Addons',
                    default = False,
                    description = 'Show hidden addons on addon files panel')
    show_code_tree = BoolProperty(name = 'Show Code Tree',
                    default = False,
                    description = 'Show code tree of current file in explorer')
    user_site_packages = BoolProperty(name = 'Browse User Site Packages',
                    default = False,
                    description = 'Browse User Site Packages on addon files panel')

# debugger preferences
    replace_low_level_libs = BoolProperty(name = 'replace low level libs',
                    default = True,
                    description = 'replace low level libs at init')



    def draw(self, context):
        layout = self.layout

        # layout.label(text = "Here you can enable or disable "
        #                     "specific tools, in case they interfere "
        #                     "with others or are just plain annoying")

        split = layout.split(percentage=0.3)

        col = split.column()
        sub = col.column(align=True)

        sub.prop(self, "show_bge_console", toggle=True)
        sub.prop(self, "show_code_editor", toggle=True)
        sub.prop(self, "show_icons_get", toggle=True)

        sub.separator()

        sub.label(text="3D View", icon='VIEW3D')
        sub.label(text="3D View", icon='VIEW3D')
        #sub.label(text="3D View", icon='VIEW3D')
        sub.prop(self, "find_replace_pref", toggle=True)

        # Code Editor Settings
        col = split.column()

        box = col.box()

        box.label(text="Code Editor Settings", icon='WORDWRAP_ON')
        row = box.row()
        sub = row.column(align=True)
        sub.prop(self, "opacity")
        sub.prop(self, "show_tabs", toggle=True)
        sub.prop(self, "window_min_width")
        sub = row.column(align=True)
        sub.prop(self, "minimap_width")
        sub.prop(self, "symbol_width")
        sub.prop(self, "line_height")

        box.separator()

        row = box.row(align=True)
        row.prop(self, "show_margin", toggle=True)
        row.prop(self, "margin_column")

        box.separator()

        row = box.row(align=True)
        row.prop(self, "block_trans")
        row.prop(self, "indent_trans")
#     def draw(self, context):
#         layout = self.layout
#         row = layout.row(align = False)
#         row.prop(self, 'show_dot_files')
#         row.prop(self, 'show_dot_addons')
#         row.prop(self, 'line_amount')



# registro automatico con register_module
# register y unregister comentados

# def register():
#     bpy.utils.register_class(SubmoduleGroup)
#     bpy.utils.register_class(WeedPreferences)


# def unregister():
#     bpy.utils.unregister_class(WeedPreferences)
#     bpy.utils.unregister_class(SubmoduleGroup)