from panda3d.core import NodePath
from panda3d.core import CardMaker
from panda3d.core import SequenceNode
from panda3d.core import TextureStage


cardmaker = CardMaker("sprite")
cardmaker.set_frame(
    (-0.5, 0.5,0),( 0.5, 0.5,0),
    ( 0.5,-0.5,0),(-0.5,-0.5,0))

cardmaker.set_frame(
    (-0.5,-0.5,0),( 0.5,-0.5,0),
    ( 0.5, 0.5,0),(-0.5, 0.5,0),
)


def sheet_uv(node, texture, columns, rows, id):
    w, h = 1/columns, 1/rows
    tile_x, tile_y = int(id%columns), int(id/(columns))
    u, v = (tile_x*w), 1-((tile_y*h)+h)
    node.set_texture(texture)
    node.set_transparency(True)
    node.set_tex_scale(TextureStage.get_default(), w, h)
    node.set_tex_offset(TextureStage.get_default(), (u, v))
    for stage in node.find_all_texture_stages():
        node.set_texture(stage, texture, 1)
        node.set_tex_scale(stage, w, h)
        node.set_tex_offset(stage, (u, v))
    return node

def animated_texture(node, texture, columns, rows, frames, playrate=1):
    sequence = NodePath(SequenceNode('sprite'))
    for frame in frames:
        sheet_uv(node.copy_to(sequence), texture, columns, rows, frame)
    sequence.node().set_frame_rate(5)
    sequence.node().loop(True)
    return sequence

def sheet_card(image, w=1, h=1, frames=[0], playrate=1): # or [id, id, id]
    card = NodePath(cardmaker.generate())
    texture = base.loader.load_texture("assets/images/"+image+".png")
    if w > 1 and h > 1:
        animated_texture(card, texture, w, h, frames, playrate)
    else:
        sheet_uv(card, texture, w, h, frames[0])
    return card
