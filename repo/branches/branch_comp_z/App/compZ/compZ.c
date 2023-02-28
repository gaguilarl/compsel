
/**
 * This is Comp Z file
 * Version info: 2.1.1
 * 
 */

#include <stdio.h>

const static int version[3] = {2,1,1};

void CompZ_MainFunction(void)
{
    static int callCount = 0;
    printf("I am component Z, my version is %d.%d.%d. Called %d times\n", 
           version[0],
           version[1],
           version[2],
           ++callCount);
    switch(callCount) 
    {
        case 1:
        {
            printf("I am new and improved \n");
            break;
        }
        case 3:
        {
            printf("I do different things \n");
            break;
        }
    }
}