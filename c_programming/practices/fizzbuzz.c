//CC 7th fizzbuzz
#include <stdio.h>

int main(void){

    int num= 1;
    while(num<51){
        num++;
        if(num%3){
            printf("Fizz\n");
        }else if(num%5){
            printf("buzz\n");
        }else if(num%3 && num%5){
            printf("fizzbuzz\n");
        }else{
            printf("%d\n", num);
        } 
    }


    return 0;
}