"""
DIGM 131 - Assignment 1: Procedural Scene Builder
==================================================

OBJECTIVE:
    Build a simple 3D scene in Maya using Python scripting.
    You will practice using maya.cmds to create and position geometry,
    and learn to use descriptive variable names.

REQUIREMENTS:
    1. Create a ground plane (a large, flat polygon plane).
    2. Create at least 5 objects in your scene.
    3. Use at least 2 different primitive types (e.g., cubes AND spheres,
       or cylinders AND cones, etc.).
    4. Position every object using descriptive variable names
       (e.g., house_x, tree_height -- NOT x1, h).
    5. Add comments explaining what each section of your code does.

GRADING CRITERIA:
    - [20%] Ground plane is created and scaled appropriately.
    - [30%] At least 5 objects are created using at least 2 primitive types.
    - [25%] All positions/sizes use descriptive variable names.
    - [15%] Code is commented clearly and thoroughly.
    - [10%] Scene is visually coherent (objects are placed intentionally,
            not overlapping randomly).

TIPS:
    - Run this script from Maya's Script Editor (Python tab).
    - Use maya.cmds.polyCube(), maya.cmds.polySphere(), maya.cmds.polyCylinder(),
      maya.cmds.polyCone(), maya.cmds.polyPlane(), etc.
    - Use maya.cmds.move(x, y, z, objectName) to position objects.
    - Use maya.cmds.scale(x, y, z, objectName) to resize objects.
    - Use maya.cmds.rename(oldName, newName) to give objects meaningful names.
"""

import maya.cmds as cmds

# ---------------------------------------------------------------------------
# Clear the scene so we start fresh each time the script runs.
# (This is provided for you -- do not remove.)
# ---------------------------------------------------------------------------
cmds.file(new=True, force=True)

# ---------------------------------------------------------------------------
# Creating ground Plane
# ---------------------------------------------------------------------------
ground_width = 30
ground_height = 30
cmds.polyPlane (name="ground", width=ground_width, height=ground_height)
# ---------------------------------------------------------------------------
# Creating and assigning shader for ground
# ---------------------------------------------------------------------------
ground_shader = cmds.shadingNode("lambert", asShader=True, name="groundMat")
cmds.setAttr(ground_shader+".color", 0.2, 0.25, 0.1, type="double3")
cmds.select("ground")
cmds.hyperShade(assign=ground_shader)
# ---------------------------------------------------------------------------
# Creating house 1 
# ---------------------------------------------------------------------------
house_1_width = 12
house_1_height = 5
house_1_depth = 3
cmds.polyCube (name="house_1", width=house_1_width, height=house_1_height, depth=house_1_depth)
cmds.move(0, house_1_height/2, -house_1_height, "house_1")
# ---------------------------------------------------------------------------
#Creating house 2
# ---------------------------------------------------------------------------
house_2_width = 5
house_2_height = 3
house_2_depth = 3
cmds.polyCube (name="house_2", width=house_2_width, height=house_2_height, depth=house_2_depth)
cmds.move(5, house_2_height/2, 2, "house_2")
cmds.rotate(0, 45, 0, "house_2");
# ---------------------------------------------------------------------------
#Creating house 2
# ---------------------------------------------------------------------------
house_3_width = 7
house_3_height = 3
house_3_depth = 3
cmds.polyCube (name="house_3", width=house_3_width, height=house_3_height, depth=house_3_depth)
cmds.move(-5, house_3_height/2, 3, "house_3")
cmds.rotate(0, 90, 0, "house_3")
# ---------------------------------------------------------------------------
# Creating and assigning shader for house 1 and 3
# ---------------------------------------------------------------------------
house_1_3_shader = cmds.shadingNode("lambert", asShader=True, name="house_1_3Mat")
cmds.setAttr(house_1_3_shader+".color", 0.5, 0.2, 0.1, type="double3")
for house1_3 in ["house_1", "house_3"]:
    cmds.select(house1_3)
    cmds.hyperShade(assign=house_1_3_shader)
# ---------------------------------------------------------------------------
# Creating and assigning shader for house 2
# ---------------------------------------------------------------------------
house_2_shader = cmds.shadingNode("lambert", asShader=True, name="house_2Mat")
cmds.setAttr (house_2_shader+".color", 0.2, 0.1, 0, type="double3")
cmds.select("house_2")
cmds.hyperShade(assign=house_2_shader)

# ---------------------------------------------------------------------------
# Creating tree trunk and leaf for tree 1
# ---------------------------------------------------------------------------
tree_trunk_1_radius=0.25
tree_trunk_1_height=2
tree_trunk_1_position_x=8
tree_trunk_1_position_z=-3
tree_trunk_1_position_y=tree_trunk_1_height/2
cmds.polyCylinder (name="tree_trunk_1", radius=tree_trunk_1_radius, height=tree_trunk_1_height)
cmds. move(tree_trunk_1_position_x, tree_trunk_1_position_y, tree_trunk_1_position_z, "tree_trunk_1")

tree_leaf_1_radius=1
cmds.polySphere (name="tree_leaf_1", radius=tree_leaf_1_radius)
cmds. move (tree_trunk_1_position_x, 3, tree_trunk_1_position_z, "tree_leaf_1")
# ---------------------------------------------------------------------------
# Creating tree trunk and leaf for tree 2
# ---------------------------------------------------------------------------
tree_trunk_2_radius=0.3
tree_trunk_2_height=2.25
tree_trunk_2_position_x=-8
tree_trunk_2_position_y=tree_trunk_2_height/2
tree_trunk_2_position_z=-5
cmds.polyCylinder (name="tree_trunk_2", radius=tree_trunk_2_radius, height=tree_trunk_2_height)
cmds. move(tree_trunk_2_position_x, tree_trunk_2_position_y, tree_trunk_2_position_z, "tree_trunk_2")

tree_leaf_2_radius=1.5
cmds.polySphere (name="tree_leaf_2", radius=tree_leaf_2_radius)
cmds. move (tree_trunk_2_position_x, 3.5, tree_trunk_2_position_z, "tree_leaf_2")
# ---------------------------------------------------------------------------
# Creating and assigning materials for trees
# ---------------------------------------------------------------------------
tree_leaf_shader = cmds.shadingNode("lambert", asShader=True, name="tree_leafMat")
cmds.setAttr (tree_leaf_shader+".color", 0, 0.4, 0, type="double3")
for tree_leaf in ["tree_leaf_1", "tree_leaf_2"]:
    cmds.select (tree_leaf)
    cmds.hyperShade (assign=tree_leaf_shader)

tree_trunk_shader = cmds.shadingNode("lambert", asShader=True, name="tree_trunkMat")
cmds.setAttr (tree_trunk_shader+".color", 0.1, 0.07, 0.01, type="double3")
for tree_trunk in ["tree_trunk_1", "tree_trunk_2"]:
    cmds.select (tree_trunk)
    cmds.hyperShade (assign=tree_trunk_shader)
# ---------------------------------------------------------------------------
# Frame All -- so the whole scene is visible in the viewport.
# (This is provided for you -- do not remove.)
# ---------------------------------------------------------------------------
cmds.viewFit(allObjects=True)
print("Scene built successfully!")
