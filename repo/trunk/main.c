
#include "compX.h"
#include "compY.h"
#include "compZ.h"

const int COMP_NUM = 3;

int main(void)
{
    for(int i = 0; i < COMP_NUM; i++) 
    {
        CompX_MainFunction();
        CompY_MainFunction();
        CompZ_MainFunction();
    }
}