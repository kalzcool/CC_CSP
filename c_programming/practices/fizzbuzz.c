//CC 7th fizzbuzz
#include <stdio.h>

int main(void){

    int num= 1;
    while(num<51){
        num++;
        if(num%3 && num%5 ==0){
            printf("Fizzbuzz\n");
        }else if(num%5==0){
            printf("buzz\n");
        }else if(num%3==0){
            printf("fizz\n");
        }else{
            printf("%d\n", num);
        } 
    }


    return 0;
}