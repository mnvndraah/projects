#include <stdio.h>
// Centigrade = (5/9)(Farenheit - 32)

int main()
{
    int fahr, centi;
    int low, up, step;
    
    low = 0;
    up = 300;
    step = 20;
    fahr = low;
    
    while (fahr<=up){
        centi = (fahr-32) * 5/9;
        // printf("%d\t%d\n", fahr, centi); NOT RIGHT ORIENTED
        printf("%3d %6d\n", fahr, centi); // RIGHT ORIENTED
        fahr = fahr + step;
    }
}