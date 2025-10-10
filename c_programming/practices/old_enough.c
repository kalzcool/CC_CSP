//CC 7th old enough 
#include <stdio.h>

int main(void){

    int age;
    printf("What is your age:\n");
    scanf("%d", &age); 

    if(age >=65){
        printf("You are a senior citizen, you can do everything but you might want to not drive or vote\n");
    }else if(age >=18 && age<= 65){
        printf("You are old enough to vote\n");
    }else if(age >=16 && age<= 18){
        printf("You are old enough to drive\n");
    }else if(age<= 16 && age >=15){
        printf("You are old enough to get a learners permit, wish that was me\n");
    }else{
        printf("You are old enough to go to school\n");
    }

    return 0;
}