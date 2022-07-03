from matplotlib import animation
import matplotlib.pyplot as plt
from datetime import datetime
import os
from PIL import Image, ImageFont, ImageDraw
import numpy as np

import pathlib
def save_img(np_array,img_name="your_file")->None:
    from PIL import Image
    im = Image.fromarray(np_array)
    im.save(img_name+"_"+now()+".jpeg")

def VDisplay():
    from pyvirtualdisplay import Display
    virtual_display = Display(visible=0, size=(1400, 900))
    virtual_display.start()

def now()->str:
    """
    get time of now
    """

    now = datetime.now() # current date and time    
    t=now.strftime("%Y%m%d-%H%M%S")
    return t

class envhelper(object):

    def __init__(self) -> None:

        print("rl init the display... (if not respond in 5s, please kill this process)")
        from pyvirtualdisplay import Display
        self.virtual_display = Display(visible=0, size=(1400, 900))
        self.virtual_display.start()
        print("rl helper inited")
        super().__init__()
 
    def recording(self,env,custom_text=None,env_image=None):
        self.frames = [] if getattr(self,"frames",None) is None else getattr(self,"frames",None) 
        if env_image is None:
            img=env.render(mode="rgb_array")
        else:
            img=env_image
        if custom_text is not None:
            Img=Image.fromarray(img)
            draw = ImageDraw.Draw(Img)
            draw.text((0,0), f"{custom_text}", (255,255,0))
            img=np.array(Img)
        
        self.frames.append(img)
        self.env=env

    def save_gif(self, 
    path=None, 
    comment="",
    filename=None,
    times=5,
    name="default",
    refresh=True):
        """
        save frames to gif
        """
        print("saving gif...")
        def _save_frames_as_gif(frames, path='./', filename='gym_animation.gif',times=1):

            
            old_frames=frames.copy()
            frames=[]
            c=0
            for f in old_frames:
                c+=1
                if c==times:
                    frames.append(f)
                    c=0
            #Mess with this to change frame size
            plt.figure(figsize=(frames[0].shape[1] / 72.0, frames[0].shape[0] / 72.0), dpi=72)

            patch = plt.imshow(frames[0])
            plt.axis('off')

            def animate(i):
                patch.set_data(frames[i])

            anim = animation.FuncAnimation(plt.gcf(), animate, frames = len(frames), interval=1000)
            anim.save(path.joinpath(filename), writer='imagemagick', fps=60)
        
        t=now()
        # assert path is None and filename is None, "not support diy path and filename"
        gif_name="{t}{comment}.gif".format(t=t,comment="_{}".format(comment))
        path = pathlib.Path("./runs/") if path is None else pathlib.Path(path)
        os.makedirs(path,exist_ok=True)
        
        try:
            env_name=self.env.spec.id
        except Exception as err:
            print(err)
            env_name=str(self.env).split(" ")[0].replace("<","-").replace(">","-").strip("-")
        dirs = path.joinpath(env_name)
        # try:
        #     dirs = path.joinpath(self.env.spec.id)
        # except:
        #     dirs = path.joinpath(self.env.spec.id)
        # dirs="./runs/{path}{env}/".format(path=path, env=self.env.spec.id)
        os.makedirs(dirs,exist_ok=True)
        _save_frames_as_gif(self.frames,path=dirs,filename=gif_name,times=times)
        print("gif saved to {}{}".format(dirs,gif_name))

        if refresh:
            del self.frames

        self.virtual_display.stop()