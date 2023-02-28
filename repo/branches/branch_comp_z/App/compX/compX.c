

/**
 * This is Comp X file
 * Version info: 0.1.0
 * 
 */


const static int version[3] = {0,1,0};

void CompX_MainFunction(void)
{
    static int callCount = 0;
    printf("I am component X, my version is %d.%d.%d. Called %d times\n", 
           version[0],
           version[1],
           version[2],
           ++callCount);
}