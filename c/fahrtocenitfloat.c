#include <stdio.h>

int main(){
    float fahr, cel;
    int start, stop, step;

    start = 0;
    stop = 300;
    step = 20;
    fahr = start;

    while (fahr <= stop){
        cel = (fahr - 32.0)*5.0/9.0;
        printf("%3.0f %6.1f\n", fahr, cel);
        fahr += step;
    }
}
