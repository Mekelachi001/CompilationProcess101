// Needed libraries
#include <stdio.h>
#include <unistd.h>
#include <windows.h>



//  Random definition or macro
#define function int
#define num int
#define rtn return
#define cmp if
#define show printf
#define start main
#define is_equal ==
#define is_not !=
#define Greater <
#define less >
#define and &&
#define or ||
#define is =
#define not !
#define when for
#define inc ++
#define empty void
#define pointer_to_int int* 
#define pointer_to_float float*
#define Pointer_to_char char*
#define amp &
#define input scanf
#define dec float 
#define long_dec double
#define not_cmp else
#define comp else if




// Function for random library 

empty wait(){
    sleep(2);
}
empty input_int(num num1){
    scanf("%d", &num1);
}

empty newLine(){
    printf("\n");
}

dec pow_of(num _value_, num _pow_of){
    when(num o is 0; o less _pow_of; o inc ){
        _value_ is _value_ *_value_;
    }
    rtn _value_;
}
