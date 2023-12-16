glboal_virtual_display = None

def start_virtual_display():
    from pyvirtualdisplay import Display
    global glboal_virtual_display
    if glboal_virtual_display is None:
        print("rl init the display... (if not respond in 5s, please kill this process)")
        glboal_virtual_display = Display(visible=0, size=(1400, 900))
        glboal_virtual_display.start()
        print("rl helper inited")
    else:
        print("virtual display already started")

def stop_virtual_display():
    global glboal_virtual_display
    if glboal_virtual_display is not None:
        glboal_virtual_display.stop()
        glboal_virtual_display = None
    else:
        print("virtual display already stopped")
