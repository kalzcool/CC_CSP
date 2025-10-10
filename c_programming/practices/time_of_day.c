//CC 7th time of day
#include <stdio.h>
//Codespaces never lets me  run my code, so I am reveiwing this and hoping it runs properly.
int main(void){
    int time;

    printf("What is the current military time:\n");
    scanf("%d", time);

    if(time >= 5){
        printf("Go to bed please\n");
    }else if(time <=12 && time>= 6){
        printf("Good morning\n");
    }else if(time >=12 && time<=18){
        printf("Good afternoon\n");
    }else if(time >=18 && time <=20){
        printf("Good evening");
    }else{
        printf("Good night")
    }

    return 0;
}