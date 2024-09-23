/***********************************************************************
// AP Workshop 1 p1: tester program
//
// File main.c
// Version 1.0
// Date Fall 2024
// Author Ruslan Parkhomenko
// Description
//
// This file will be replaced by another tester program during the
submission
//
// Revision History
// -----------------------------------------------------------
// Name Date Reason
//
/////////////////////////////////////////////////////////////////
***********************************************************************/
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int getNoOfStudents(void);
int getAverage(int NumberOfStudents);
void printReport(int NumberOfStudents, int average);
int main(void) {
 int num;
 int average;
 printf("Class test marks report program...\n\n");
 num = getNoOfStudents();
 average = getAverage(num);
 printReport(num, average);
 return 0;
}


void prnGrade(int mark){

    printf("Mark: %d ", mark);

    if(mark < 50){

        printf("F");

    } else if (mark >= 50 && mark <= 54)
    {
        printf("D");

    } else if (mark >= 55 && mark <= 59)
    {
        printf("D+");

    } else if (mark >= 60 && mark <= 64)
    {
        printf("C");

    } else if (mark >= 65 && mark <= 69)
    {
        printf("C+");

    }else if (mark >= 70 && mark <= 74)
    {
        printf("B");

    }else if (mark >= 75 && mark <= 79)
    {
        printf("B+");

    }else if (mark >= 80 && mark <= 89)
    {
        printf("A");

    }else if (mark >= 90 && mark <= 100)
    {
        printf("A+");
    }

}

int getNoOfStudents (void) {

    int noofstudents;
    printf("Enter the number of students: ");
    scanf("%d", &noofstudents);
    return noofstudents;
}

int getAverage (int NumberOfStudents) {

    int count=0;
    int mark;
    int sum=0;
    printf("Enter %d student marks...\n", NumberOfStudents);
    while(count < NumberOfStudents) {
        
        printf("%d> ", count + 1);
        scanf("%d", &mark);

        if(mark < 0) 
        {
            printf("Invalid Mark, values should be greater than or equal 0.\n");
        } 
        else if(mark > 100) 
        {
            printf("Invalid Mark, values should be less than or equal to 100.\n");
        }
        else {
            sum += mark;
            count++;
        }

    }
    return sum / NumberOfStudents;
}

void printReport (int NumberOfStudents, int average) {

    printf("Number of students: %d\n", NumberOfStudents);
    printf("Class average: %d%%\n", average);
    prnGrade(average);
}