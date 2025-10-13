//CC 7th fizzbuzz
#include <stdio.h>

int main(void){

    int num= 1;
    while(num<51){
        num++;
        if(num%15){
            printf("Fizzbuzz\n");
        }else if(num%5){
            printf("buzz\n");
        }else if(num%3){
            printf("fizz\n");
        }else{
            printf("%d\n", num);
        } 
    }


    return 0;
}