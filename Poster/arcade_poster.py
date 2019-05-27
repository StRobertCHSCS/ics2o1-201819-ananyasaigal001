import arcade


WIDTH = 640
HEIGHT = 480

#x position of car
Car_position_x = 150
delta_x = 1  # change in x
#BUTTON HOTSPOTS
my_button = [45, 140, 30, 30]  # x, y, width, height
show_text = False

def draw_car(x, y):
   """ Draw a car """

   # Car
   arcade.draw_rectangle_filled(205 + x, 350 + y, 85,65, arcade.color.ROYAL_BLUE)
   arcade.draw_rectangle_filled(205 + x, 300 + y, 155,85, arcade.color.ROYAL_BLUE)

   # Wheels
   arcade.draw_circle_filled(150 + x, 250 + y, 25, arcade.color.SMOKY_BLACK)
   arcade.draw_circle_filled(260 + x, 250 + y, 25, arcade.color.SMOKY_BLACK)


def on_update(delta_time):
   global Car_position_x
   Car_position_x += delta_x
   print(Car_position_x)

def on_draw():
   arcade.start_render()

   #Car
   draw_car(Car_position_x , 50)

  # Draw Words...
   arcade.draw_text("How Portable Computing Devices Affect Our Everyday Lives"
                    , 0, 250, arcade.color.BLACK, 19.499)
   arcade.draw_text("GPS help with navigation", 115, 450, arcade.color.BLAST_OFF_BRONZE, 16)
   arcade.draw_text("Laptops help us access information from around the world "
                    , 214, 215, arcade.color.BRILLIANT_ROSE, 13)

  #Draw Cellphone
   arcade.draw_rectangle_filled(20,130, 65, 20, arcade.color.WHITE)
   arcade.draw_rectangle_filled(20, 75, 65, 105, arcade.color.BLACK)
   arcade.draw_rectangle_filled(20, 25, 65, 15, arcade.color.WHITE)
   arcade.draw_circle_filled(20, 132, 5, arcade.color.BLACK)
  #Draw equal sign
   arcade.draw_rectangle_outline(75, 60, 44, 12, arcade.color.SMOKY_BLACK)
   arcade.draw_rectangle_outline(75, 40, 44, 12, arcade.color.SMOKY_BLACK)
   arcade.draw_rectangle_outline(515, 60, 50, 12, arcade.color.SMOKY_BLACK)
   arcade.draw_rectangle_outline(515, 40, 50, 12, arcade.color.SMOKY_BLACK)
   arcade.draw_rectangle_outline(170, 350, 50, 12, arcade.color.SMOKY_BLACK)
   arcade.draw_rectangle_outline(170, 320, 50, 12, arcade.color.SMOKY_BLACK)
   #Draw Computer
   arcade.draw_rectangle_filled(575, 145, 95, 95, arcade.color.DARK_BLUE,365)
   arcade.draw_rectangle_outline(575, 145, 95, 95, arcade.color.GRAY,375,4)
   arcade.draw_rectangle_filled(585, 50, 105, 95, arcade.color.SMOKY_BLACK,365)
   #Button Hotspot
   arcade.draw_xywh_rectangle_filled(my_button[0],
                                     my_button[1],
                                     my_button[2],
                                     my_button[3],
                                     arcade.color.AERO_BLUE)

   if show_text:
     arcade.draw_text("Cell phones can be used to bring the world together", 0, 4, arcade.color.RED_PURPLE, 12)
   # Input Online Images
   texture = arcade.load_texture("IMAGES/GPS.jpg")
   scale = .12
   arcade.draw_texture_rectangle(55, 325, scale * texture.width,
                                 scale * texture.height, texture, 0)
   texture = arcade.load_texture("IMAGES/bringing_the_world_together.jpg")
   scale = .1
   arcade.draw_texture_rectangle(210, 70, scale * texture.width,
                                 scale * texture.height, texture, 0)
   texture = arcade.load_texture("IMAGES/information_from_anywhere_in_the_world.jpg")
   scale = .30
   arcade.draw_texture_rectangle(414, 70, scale * texture.width,
                                 scale * texture.height, texture, 0)
def on_key_press(key, modifiers):
   pass




def on_key_release(key, modifiers):
   pass


def on_mouse_press(x, y, button, modifiers):
  global show_text
  # unpack the button list into readable variables.
  my_button_x, my_button_y, my_button_w, my_button_h = my_button

  # Need to check all four limits of the button.
  if (x > my_button_x and x < my_button_x + my_button_w and
          y > my_button_y and y < my_button_y + my_button_h):
    show_text = True
  else:
    show_text = False

def setup():
   arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
   arcade.set_background_color(arcade.color.BABY_BLUE_EYES)
   arcade.schedule(on_update, 1/60)

   # Override arcade window methods
   window = arcade.get_window()
   window.on_draw = on_draw
   window.on_update = on_update
   window.on_key_press = on_key_press
   window.on_key_release = on_key_release
   window.on_mouse_press = on_mouse_press

   arcade.run()


if __name__ == '__main__':
   setup()
