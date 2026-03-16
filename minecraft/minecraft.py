from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina(title='Minecraft but Python')
player = FirstPersonController()
Sky()

start_position = Vec3(11, 10, 11)
player.position = start_position

normal_fov = 90
zoomed_fov = 45
zoom_speed = 5

boxes = []
for i in range(20):
  for j in range(20):
    box = Button(color=color.white, model='cube', position=(j,0,i),
          texture='/pictures/grass.png', parent=scene, origin_y=0.5)
    boxes.append(box)

def input(key):
  for box in boxes:
    if box.hovered:
      if key == '1':
        new = Button(color=color.white, model='cube', position=box.position + mouse.normal,
                    texture='/pictures/grass.png', parent=scene, origin_y=0.5)
        boxes.append(new)
      if key == '2':
        new = Button(color=color.white, model='cube', position=box.position + mouse.normal,
                    texture='/pictures/sand.png', parent=scene, origin_y=0.5)
        boxes.append(new)
      if key == '3':
        new = Button(color=color.white, model='cube', position=box.position + mouse.normal,
                    texture='/pictures/dirt.png', parent=scene, origin_y=0.5)
        boxes.append(new)
      if key == '4':
        new = Button(color=color.white, model='cube', position=box.position + mouse.normal,
                    texture='/pictures/planks.png', parent=scene, origin_y=0.5)
        boxes.append(new)
      if key == '5':
        new = Button(color=color.white, model='cube', position=box.position + mouse.normal,
                    texture='/pictures/stone.png', parent=scene, origin_y=0.5)
        boxes.append(new)
      if key == '6':
        new = Button(color=color.white, model='cube', position=box.position + mouse.normal,
                    texture='/pictures/cobblestone.png', parent=scene, origin_y=0.5)
        boxes.append(new)
      if key == '7':
        new = Button(color=color.white, model='cube', position=box.position + mouse.normal,
                    texture='/pictures/brick.png', parent=scene, origin_y=0.5)
        boxes.append(new)
      if key == '8':
        new = Button(color=color.white, model='cube', position=box.position + mouse.normal,
                    texture='/pictures/netherrack.png', parent=scene, origin_y=0.5)
        boxes.append(new)
      if key == '9':
        new = Button(color=color.white, model='cube', position=box.position + mouse.normal,
                    texture='/pictures/bedrock.png', parent=scene, origin_y=0.5)
        boxes.append(new)
      if key == 'left mouse down':
        boxes.remove(box)
        destroy(box)

def update():
    if held_keys['right mouse']:
        target_fov = zoomed_fov
    else:
        target_fov = normal_fov
    camera.fov = lerp(camera.fov, target_fov, time.dt * zoom_speed)

    if player.y < -20:
        player.position = start_position

app.run()

# Ctrl + Shift + Alt + Q to close ursina window