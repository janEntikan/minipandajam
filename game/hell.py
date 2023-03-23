from math import sqrt
import struct
from random import uniform
from collections import defaultdict
from panda3d.core import *

POOL = 65534
DIV = 16


class Particle:
    def __init__(self, idx, pos=Vec3(), vel=Vec3()):
        self.idx = idx
        self.pos = pos
        self.velocity = vel


class Particles:
    def __init__(self, texture):
        texture.set_minfilter(SamplerState.FT_nearest)
        texture.set_magfilter(SamplerState.FT_nearest)
        texture.set_wrap_u(SamplerState.WM_repeat)
        texture.set_wrap_v(SamplerState.WM_repeat)

        self.dist = 0.5
        self.texture = texture
        self.current_idx = -1
        self.grid = defaultdict(list)
        self.particles = []
        self.format = GeomVertexFormat.get_v3()
        self.stride = self.format.arrays[0].stride

        self.vert_data = GeomVertexData('vdata', self.format, GeomEnums.UH_static)
        self.vert_data.unclean_set_num_rows(POOL)

        self.prim = GeomPoints(GeomEnums.UH_static)
        self.prim.set_index_type(GeomEnums.NT_uint32)
        self.prim.add_next_vertices(POOL)

        self.writer = GeomVertexWriter(self.vert_data, 'vertex')
        self.geom = Geom(self.vert_data)
        self.geom.add_primitive(self.prim)
        self.geom_node = GeomNode("particles")
        self.geom_node.add_geom(self.geom)
        self.path = path = render.attach_new_node(self.geom_node)
        path.set_render_mode_thickness(0.2)
        path.set_texture(self.texture)
        path.set_tex_gen(TextureStage.get_default(), TexGenAttrib.M_point_sprite)
        path.set_antialias(AntialiasAttrib.M_point)
        path.set_depth_test(True)
        path.set_depth_write(True)
        path.set_transparency(TransparencyAttrib.M_binary)
        path.set_render_mode_perspective(True)

        base.task_mgr.add(self.update_particles)

    @property
    def idx(self):
        self.current_idx += 1
        return self.current_idx

    def is_colliding(self, other, dist=1):
        pos = other.get_pos()
        grid = self.grid[pos.x//DIV, pos.y//DIV, pos.z//DIV]
        for bullet in grid:
            d = sqrt((pos.x-bullet.pos.x)**2+(pos.y-bullet.pos.y)**2)
            print(d)
            if d < dist+self.dist:
                return True

    def make_particle(self, pos, velocity):
        particle = Particle(self.idx, pos, velocity)
        x,y,z = pos.x//DIV,pos.y//DIV,pos.z//DIV
        self.grid[x,y,z].append(particle)
        self.particles.append(particle)

    def update_particles(self, task):
        self.writer.set_row(0)
        for particle in self.particles:
            pos = particle.pos
            x,y,z = pos.x//DIV,pos.y//DIV,pos.z//DIV
            self.grid[x,y,z].remove(particle)
            particle.pos += particle.velocity*game.clock.dt
            pos = particle.pos
            x,y,z = pos.x//DIV,pos.y//DIV,pos.z//DIV
            self.grid[x,y,z].append(particle)
            self.writer.set_data3(*pos)
        return task.cont


if __name__ == "__main__":
    from direct.showbase.ShowBase import ShowBase

    base = ShowBase()
    base.set_frame_rate_meter(True)

    t = loader.load_texture("bullet.png")
    a = loader.load_model("models/smiley").copy_to(render)

    particles = Particles(t)
    particles.path.reparent_to(render)
    for i in range(800):
        v,p = 16, 64
        vel = Vec3(uniform(-v,v),uniform(-v,v),0)
        pos = Vec3(uniform(-p,p),uniform(-p,p),uniform(-p,p))
        particles.make_particle(pos, vel)

    def update(task):
        particles.is_colliding(a, 5)
        return task.cont
    base.task_mgr.add(update)
    base.cam.set_pos(0,0,400)
    base.cam.look_at(render)
    base.run()
