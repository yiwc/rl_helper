from matplotlib import animation
import matplotlib.pyplot as plt
from datetime import datetime
import os

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
 
    def recording(self,env,env_image=None):
        self.frames = [] if getattr(self,"frames",None) is None else getattr(self,"frames",None) 
        if env_image is None:
            self.frames.append(env.render(mode="rgb_array"))
        else:
            self.frames.append(env_image)
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
        
        dirs = path.joinpath(str(self.env).split(" ")[0].replace("<",""))
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