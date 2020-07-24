import taichi as ti
import random

ti.init(arch=ti.cpu, print_ir=True)


res = (128, 128)
dx = 1 / 128
inv_dx = 1.0 / dx

m = ti.var(dt=ti.f32)

grid = ti.root.pointer(ti.i, 1)
grid.pointer(ti.i, 128).dense(ti.i, 32).place(m)

@ti.kernel
def act():
    ti.parallelize(2)
    for j in range(100000):
        m[0] += 1

for i in range(100):
    # grid.deactivate_all()
    # act()
    ti.memory_profiler_print()