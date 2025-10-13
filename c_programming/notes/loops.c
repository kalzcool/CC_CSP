//CC 7th loops/lists notes
#include <stdio.h>

int main(void){

    int nums[] ={1, 64 , 4, 56, 8, 742, 5}; // Arrays
    char candies[][20]= {"kitkat", "Skittles", "nerds", "hersheys", "reese's"}; //first set of [# inside the list]
    //secound [length of strings]

    for(int x =0; x<7; x++){// ++increasing by one
        printf("%d\n", nums[x]);
    }

    for(int i=0; i<5; i++){// i stands for iteration of the loop, one times through
        printf("%s, is my favorite candy\n", candies[i]);
    }
    for(int num =1; num<11; num++){
        printf("%d\n", num);
    }

    int num=0;
    while(num<11){
        printf("%d\n", num);
        num++;
    }

    return 0;
}