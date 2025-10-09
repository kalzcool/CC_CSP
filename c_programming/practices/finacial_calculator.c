//CC 7th finacnial calc
#include <stdio.h> 
#include <math.h>

int main(void){
    int monthly_income;
    int monthly_rent;
    int monthly_utilities;
    int monthly_groceries;
    int monthly_transportaion;

    printf("What is your monthly income: \n");
    fscan((int)monthly_income, sizeof(monthly_income), stdin);
    printf("What is your monthly rent: \n");
    fscan((int)monthly_rent, sizeof(monthly_rent), stdin);
    printf("What is your monthly utilites: \n");
    fscan((int)monthly_utilities, sizeof(monthly_utilities), stdin);
    printf("What is your groceries \n");
    fscan((int) monthly_groceries, sizeof(monthly_groceries), stdin);
    printf("What is your transportaion: \n");
    fscan((int)monthly_transportaion, sizeof(monthly_transportaion), stdin);


    printf("Your' monthly rent is %d and it is %d of your income", monthly_rent, (monthly_rent/monthly_income*100));
    printf("Your' monthly utilities are %d and they are %d of your income", monthly_utilities, monthly_utilities/monthly_income*100);
    prinf("Your'  groceries are %d and they are %d of your income", monthly_groceries, monthly_groceries/monthly_income*100);
    printf("Your monthly transportation is %d and it is %d of your income", monthly_transportaion, monthly_transportaion/monthly_income*100);
    printf("You should save %d a month, it is 10 percent of your income",monthly_income/10);
    printf("You have %d of spending money a month.", monthly_income-(monthly_groceries+ monthly_rent + monthly_transportaion+monthly_utilities))


    return 0 ;
}