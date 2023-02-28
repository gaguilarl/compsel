

/**
 * This is Comp Z file
 * Version info: 2.1.0
 * 
 */

/**
 * @brief This is trunks version
 * 
 */


const static int version[3] = {2,1,0};

void CompZ_MainFunction(void)
{
    static int callCount = 0;
    printf("I am component Z, my version is %d.%d.%d. Called %d times\n", 
           version[0],
           version[1],
           version[2],
           ++callCount);
}