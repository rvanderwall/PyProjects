
import gc

gc.set_debug(gc.DEBUG_STATS)
#gc.set_debug(gc.DEBUG_COLLECTABLE | gc.DEBUG_SAVEALL)

def gc_callback(phase, info):
    print(f"GC phase: {phase} with info: {info}")

gc.callbacks.append(gc_callback)

print("Start")
x = []
print("x allocated")

x.append(x)
print("x appended")

del x
print("x deleted")

gc.collect()

gc.get_threshold()
gc.get_count()

print("GC called")

