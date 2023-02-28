

/**
 * This is Comp Y file
 * Version info: 3.3.3
 * 
 */

#include <stdio.h>

const static int version[3] = {3,3,3};

void CompY_MainFunction(void)
{
    static int callCount = 0;
    printf("I am component Y, my version is %d.%d.%d. Called %d times\n", 
           version[0],
           version[1],
           version[2],
           ++callCount);
}