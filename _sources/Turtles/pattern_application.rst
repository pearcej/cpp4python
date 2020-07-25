Practical Application - Tessellation
====================================

Art takes a variety of forms, ranging from abstract to realistic,
and consisting of an impossibly wide variety of materials.
Ancient Sumerians would dye and dry small pieces of clay to create mosaics.
These mosaics were often composed of shapes and patterns that would overlap
without any gaps in between them. This art form is known today as tessellation,
which can be observed in any modern building that is composed of bricks,
or any floor covered in ceramic tiles. Mosaics are defined by their interlocking shapes,
however, what these shapes are made of‒ or, the medium‒ varies depending on the artist.

The common mediums for this art form have changed over time,
ranging from pieces of clay to pieces of wood. More recently,
digital mediums have been used as an effective alternative to physical materials.
Turtles are one of many such digital mediums, and are often used to
create images rich in repetitive features. Your task will be to create
a mosaic-like tessellating image using turtles.

Consider the following examples.

.. activecode:: cturtle_practical_example_cpp
    :language: cpp

    #include <CTurtle.hpp>
    namespace ct = cturtle;

    int main() {
        const int SQUARE_SIZE = 35;

        ct::TurtleScreen scr;
        scr.tracer(0);//disable animation
        ct::Turtle turtle(scr);
        turtle.speed(ct::TS_FASTEST);
        turtle.penup();

        for(int i = 0; i < 8; i++){
            turtle.goTo(-scr.window_width()/2,-scr.window_height()/2+ (i*SQUARE_SIZE)+SQUARE_SIZE);

            bool is_blue = i % 2 == 0;//even (true) or odd (false) row?
            
            for(int j = 0; j < 8; j++){
                ct::Color color;

                if(is_blue){
                    color = {"blue"};
                }else{
                    color = {"orange"};
                }

                turtle.begin_fill();
                turtle.fillcolor(color);

                for(int i = 0; i < 4; i++){
                    turtle.forward(SQUARE_SIZE);
                    turtle.right(90);
                }

                turtle.end_fill();

                turtle.forward(SQUARE_SIZE);
                is_blue = !is_blue;//flip-flop between true and false
            }
        }
        
        scr.bye();
        return 0;
    }

.. activecode:: cturtle_practical_example_Python
    :language: Python

    import turtle

    SQUARE_SIZE = 35

    wn = turtle.Screen()
    wn.tracer(0);
    square = turtle.Turtle()
    square.speed(10)
    square.pu()
    square.goto(-turtle.window_width()/2,turtle.window_height()/2);
    square.pd()

    a = 0
    b = 0
    for i in range(8):
        if(b == 0):
            a=1
        else:
            a=0
        for j in range(8):
            square.penup()
            square.goto(-turtle.window_width() / 2 + j * SQUARE_SIZE, (-turtle.window_height() / 2) + i * SQUARE_SIZE + SQUARE_SIZE)
            square.pendown()
            if(a==0):
                square.fillcolor('orange')
                a=1
            else:
                square.fillcolor('blue')
                a=0
            square.begin_fill()
            for k in range(4):
                square.forward(SQUARE_SIZE)
                square.right(90)
            square.end_fill()
        if(b==0):
            b=1
        else:
            b=0
    wn.tracer(1)


You must create a similar image with the following criteria:

- There must not be four edges in your chosen shape, but 3 or 5+ is fine.
- There must be no more than two colors for the shapes in the image.

.. activecode:: cturtle_practical_prompt
    :language: cpp

    #include <CTurtle.hpp>
    namespace ct = cturtle;

    int main() {
        ct::TurtleScreen scr;
        scr.tracer(0);//disable animation
        ct::Turtle turtle(scr);
        
        //Your code here
        
        scr.bye();
        return 0;
    }

