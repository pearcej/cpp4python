Geometry, Shapes, and Stamps
============================
Every shape is a set of coordinates. Within the CTurtle library we have the 
choice of choosing between a select few shapes that we can turn our Turtle into.
To change the appearance of your Turtle, you can use :code:`shape` to set your Turtle to 
one of four default shapes.

Consider the following code:

.. code-block:: cpp

  turtle.shape("square");
  

Polygons, for custom shapes, must have their points defined in counter-clockwise order to appear correctly. This is due to
the mathematics behind filling arbitrary shapes, and is a limitation almost all computer graphics need to abide by. CTurtle
features four default shapes, :code:`triangle`, :code:`indented_triangle`, :code:`square`, and :code:`arrow`. Consider
the construction of their points, and how they could be considered "counter-clockwise". One edge exists between the first
last points for each of these shapes.

======== ===================== ========== ========
triangle   indented_triangle     square    arrow
======== ===================== ========== ========
(0, 0)          (0, 0)          (-5, -5)   (0, 0)
(-5, 5)        (-5, 10)          (-5, 5)  (-5, 5)      
(5, 5)          (0, 8)           (5, 5)   (-3, 5)
  .             (5, 10)          (5, 10)  (-3, 10)
  .               .                .       (3, 10)
  .               .                .       (3, 5)
  .               .                .       (5, 5)
======== ===================== ========== ========

.. figure:: cc_polygon.png
    :align: center

    Figure 1: Indented Triangle Definition

