#include "main.h"

function start(){
    pointer_to_int p;
    num g = 0;
    p = &g;
    show("Write a Text");
    input_int(g);
    show("Hello world");
    cmp(1 is_equal 1 and 2 is_equal 2){
        show("32");
        when(num x is 3; x Greater 10; x inc){
            show("Test");
            newLine();
        }
    }
    rtn 0;
}