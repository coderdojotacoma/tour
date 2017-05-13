from mcpi.minecraft import Minecraft
mc = Minecraft.create()

y = 0.0
while y <= 200:
    x = -3.0
    z = 33.2
    blockType = 0
    mc.setBlock(x, y, z, blockType)
    y += 1
