// Ruslan Parkhomenko 991749321, parkhomr@shernet.sheridancollege.ca, 2024.09.16
// I have done all the coding by myself and only copied the code that my professor provided to
// complete my workshops and assignments.

#include <stdio.h>

void line (char fill, int lenght);
int getInt(void);
int getIntMM(int min, int max);
double getDouble(void);
double getDoubleMM(double min, double max);
void clear(void);

void line (char fill, int lenght) {

    for (int i = 0; i < lenght; i++) {
        printf("%c", fill);
    }
}

void clear (void) {
    while (getchar() != '\n');
}


int getInt (void) {

    int value, keeptrying = 1, rc;
    char after;

    while (keeptrying == 1) {

        rc = scanf("%d%c", &value, &after);

        if (rc == 0) {
            printf("\n Bad Input, Try again... ");
            clear();
        }
        else if (after != '\n') {
            printf("\n Trailing buffer, Try again... ");
            clear();
        }
        else {
            keeptrying = 0;
        }
    }
    return value;
}


int getIntMM (int min, int max) {

    int value=0, keeptrying = 1, rc;
    char after;

    while (keeptrying == 1) {

        rc = scanf("%d%c", &value,&after);


        if (rc == 0) {
            printf("\n  Bad Input, Try again... ");
            clear();
        }

        else if (after != '\n') {
            printf("  Trailing buffer, Try again... ");
            clear();
        }

        else if (value <= min || value >= max) {
            printf("The values are out of range, Try again...");
            clear();
        }
        else
            keeptrying = 0;
    }

    return value;
}

double getDouble (void) {

    double value;
    char after;
    int keeptrying = 1, rc;

    while (keeptrying == 1) {

        rc = scanf("%lf%c", &value, &after);

        if (rc == 0) {
            printf("\n Bad Input, Try again... ");
            clear();
        }
        else if (after != '\n') {
            printf("\n Trailing buffer, Try again...");
            clear();
        }
        else {
            keeptrying = 0;
        }
    }
    return value;
}

double getDoubleMM (double min, double max) {

    double value;
    char after;
    int keeptrying = 1, rc;

    while (keeptrying == 1) {

        rc = scanf("%lf%c", &value, &after);

        if (rc == 0) {
            printf("\n Bad Input, Try again... ");
            clear();
        }
        else if (after != '\n') {
            printf("\n Trailing buffer, Try again...");
            clear();
        }
        else if (value <= min || value >= max) {
            printf("\n The values are out of range, Try again... ");
            clear();
        }
        else {
            keeptrying = 0;
        }
    }
    return value;
}

int main(void) {
 int value;
 double dvalue;
 printf("Enter an integer value: ");
 value = getInt();
 printf("You entered: %d\n", value);
 line('*', 50);
 //********************************************
 printf("\n Enter an integer value between 10 and 20 inclusive: ");
 value = getIntMM(10, 20);
 printf("You entered: %d\n", value);
 line('*', 50);
 //********************************************
 printf("\n Enter a double value: ");
 dvalue = getDouble();
 printf("You entered: %.2lf\n", dvalue);
 line('*', 50);
 //********************************************
 printf("\n Enter a double value between 10.1 and 20.9 inclusive: ");
 dvalue = getDoubleMM(10.1, 20.9);
 printf("You entered: %.2lf\n", dvalue);
 line('*', 50);
 //********************************************
 return 0;
}