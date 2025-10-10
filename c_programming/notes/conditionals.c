// CC 7th conditionals notes
#include <stdio.h> 
#include <string.h>

/*logical opperatiors
&& and
|| or
! not
*/

int main(void){
    int grade;
    char name[50];
    printf("What is your grade percent:\n");
    scanf("%d", &grade); 

    printf("What is your name:\n");
    scanf("%s", &name);

    //printf("%d\n", strcmp(name, "Ms.LaRose"));
    if(strcmp(name, "Ms.LaRose")==0){
        printf("You don't get a grade!\n");
    }else if( grade >= 90){
        printf("You have an A\n");
    }else if(grade >=80){
        printf("You have a B\n");
    }else if(grade >=70){
        printf("You have a C\n");
    }else{
        printf("You are failing:[");
    }
    return 0;
}