//CC 7th update budget calc
#include <stdio.h>
#include <math.h>

float get_month(char* monthly){
    float value;
    printf("What is your monthly %s:\n", monthly);
    scanf("%f", value);
    return value;
}

int percentages(int x, int y){
    return x/y *100;
}

int main(void){
    float income = get_month("income"); 
    float rent = get_month("rent");
    float utilities = get_month("utilities");
    float groceries = get_month("groceries");
    float transportation = get_month("transportation");

    float savings = income/ 10;
    float spending = income - (rent + utilities+ groceries + transportation);
    float rp = percentages(rent, income);
    float up = percentages(utilities, income);
    float gp = percentages(groceries, income);
    float tp = percentages(transportation, income);
    float sp = percentages(spending, income);
    float sap = percentages(savings, income);

    printf("Your rent is %f, and it is %f of your income\n", rent,rp);
    printf("Your rent is %f, and it is %f of your income\n", utilities,up);
    printf("Your rent is %f, and it is %f of your income\n", groceries,gp);
    printf("Your rent is %f, and it is %f of your income\n", transportation,tp);
    printf("Your rent is %f, and it is %f of your income\n", savings,sap);
    printf("placeholder, do the spending money here dumba");

    return 0;
}