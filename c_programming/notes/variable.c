// CC 7th variables notes 
#include <stdio.h>

int main(void){
    int grade; //4 bytes
    float pi = 3.14; //4 bytes
    double long_pi = 3.145926358; //8 bytes of space
    char letter_grade; // 1 byte
    char name[50];
    // user input
    printf("What is your name: \n");
    fgets(name, sizeof(name), stdin);


    printf("What is your grade percentage as a whole number: ");
    scanf("%d", &grade);

    printf("what is your letter grade: ");
    scanf(" %c", &letter_grade);
    while (getchar() != '\n');


    printf("%s did it?\n", name);
    printf("You have a %d, in the class. That is an %c", grade, letter_grade);
    return 0;
}