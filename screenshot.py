import pyscreenshot as ImageGrab
import time
# part of the screen
from pynput import mouse,keyboard


class ScreenShot():
    

    def __init__(self,time):
        self.mouse_position = []
        
        # Collect events until released
        print("请使用鼠标拖拽想要截取的部分！")
        with mouse.Listener(
                on_click=self.on_click) as listener:
            listener.join()

        self.x1 = self.mouse_position[0][0]
        self.y1 = self.mouse_position[0][1]
        self.x2 = self.mouse_position[1][0]
        self.y2 = self.mouse_position[1][1]
        print("鼠标位置截取成功！")
        self.image = ImageGrab.grab(bbox=(self.x1,self.y1,self.x2,self.y2)) 
        print("截图成功！")
        self.image.save('./screenshot/image-%s.png'%time)

    def on_click(self,x, y, button, pressed):
        print('{0} at {1}'.format(
            'Pressed' if pressed else 'Released',
            (x, y)))
        self.mouse_position.append((x,y))
        if not pressed:
            # Stop listener
            return False

class KeyboardListener():
    

    

    def __init__(self):
        self.signal = False
        self.timestamp_win = time.time()
        # Collect events until released
        with keyboard.Listener(
                on_press=self.on_press,
                on_release=self.on_release) as self.listener:
            self.listener.join()

    def on_press(self,key):
        pass
 
    def on_release(self,key):
        # print('{0} released'.format(
        #     key))
        pass
        if key == keyboard.Key.esc:
            # Stop listener
            return False
        if key == keyboard.Key.f4:    
            self.signal = True
            return False

if __name__ == '__main__':
    ss = ScreenShot()