import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def funsliders(f, sliders_properties, autoexec = False, history=True):
    """
    A light GUI to manually explore and tune the outputs of 
    a function. `slider_properties` is a list of elements like this:
    ('label', min_value, max_value [, initial value] )
    
    >>> def volume(x,y,z):
	>>>	    return x*y*z
    >>> funslider(volume,[ ('x',0,5), ('y',1,5,3),('z',2,5,4)])
	
    Alternatively one can define the slider's using a dictionnary.
    See Matplotlib's sliders for all supported arguments:
    
    >>> funslider(volume,[{'label': 'x', 'valmin':1, 'valmax':5},
                    {'label': 'y', 'valmin':1, 'valmax':5, 'valinit':2},
                          {'label': 'z', 'valmin':1 , 'valmax':5} ])
        
        
    If `autoexec` is True, the function `f` is executed every time
    the slider is changed, using the argument values indicated by the
    sliders. If `autoexec` is False, `f` is only run when 'Enter'
    is pressed.
    
    If `history` is True, the current value of all arguments is printed
    to the console every time the function `f` is run.
        
    """
        
    nVars = len(sliders_properties)
    slider_width = 0.5/(nVars)
    print slider_width
    
    # CREATE THE CANVAS
    
    figure,ax = plt.subplots(1)
    figure.canvas.set_window_title( "Inputs for '%s'"%(f.func_name) )
    
    # choose an appropriate height
    
    width,height = figure.get_size_inches()
    height = min(0.5*nVars,8)
    figure.set_size_inches(width,height,forward = True)
    
    
    # hide the axis
    ax.set_frame_on(False)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    

    # CREATE THE SLIDERS
    
    sliders = []
    
    for i, properties in enumerate(sliders_properties):
        
        ax = plt.axes([0.1 , 0.95-0.9*(i+1)*slider_width,
                       0.8 , 0.8* slider_width])
        if not isinstance(properties,dict):
            properties =dict(zip(['label','valmin', 'valmax', 'valinit'],
                             properties))
        sliders.append( Slider(ax=ax, **properties) )
    
    
    # CREATE THE CALLBACK FUNCTIONS
    
    def on_changed(event) : 
        if history:
            print dict( (s.label.get_text(), s.val) for s in sliders)
        res = f(*(s.val for s in sliders))
        
        if res is not None:
            
            print res
    
    def on_key_press(event):
        
        if event.key is 'enter':
            
            on_changed(event)   
    
    figure.canvas.mpl_connect('key_press_event', on_key_press)
    
    # AUTOMATIC UPDATE ?
    
    if not autoexec:
        
        for s in sliders :
            
            s.on_changed(on_changed)
    
    
    # DISPLAY THE SLIDERS
    
    plt.show()



if __name__ == "__main__":
    
    def volume(x,y,z):
			return x*y*z
    funslider(volume,[('x',0,5), ('y',1,5,3),('z',2,5,4)])
    
    
