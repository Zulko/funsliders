FunSliders
==========

FunSliders is a simple GUI to manually explore the inputs of a function:

    from funsliders import funsliders
    def volume(x,y,z):
        return x*y*z
    funsliders(volume, [('x',0,5), ('y',1,5,3), ('z',2,5,4)])

.. image:: https://raw.github.com/Zulko/funsliders/master/funsliders_demo.jpeg

A slightly more spectacular example of `funslider` in action is shown in [this video](https://www.youtube.com/watch?v=z82OHpw1-Qo).

Installation
------------

First solution, with pip:

    sudo pip install funsliders

Second solution, unzip everything in a folder and go with

    sudo python setup.py develop

Last solution, since it's a very small module (less than 100 lines) just copy the file `funsliders.py` or its content anywhere you want to use it.


What else there is to know:
---------------------------

The function to explore can be any function with numerical inputs.

One can also define the slider's properties using a dictionnary.
See Matplotlib's sliders for all supported arguments:

    funsliders(volume,[ {'label': 'x', 'valmin':1, 'valmax':5},
                 {'label': 'y', 'valmin':1, 'valmax':5, 'valinit':2},
                 {'label': 'z', 'valmin':1 , 'valmax':5} ])    
    
`funsliders` has two other arguments:
- `autoexec` is True, the function `f` is executed every time
the sliders are changed, using the argument values indicated by the
sliders. If `autoexec` is False, `f` is only run when the user presses `Enter`.
- If `history` is True, the current value of all arguments is printed to
the console every time the function `f` is run.

Licence
--------

I, the copyright holder of this work, hereby release it into the public domain. This applies worldwide.

If this is not legally possible:

I grant any entity the right to use this work for any purpose, without any conditions, unless such conditions are required by law.

Zulko, 2013

