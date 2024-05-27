#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Function to generate random numbers distributed according to an exponential distribution
double exponential(double lambda) {
    // Generate a random number between 0 and 1
    double u = (double)rand() / RAND_MAX;
    // Transform the random number using the inverse CDF of the exponential distribution
    return -log(1 - u) / lambda;
}

int main() {
    int i, n = 10000;
    double lambda = 0.5; // Mean of the exponential distribution

    // Seed the random number generator
    srand(42);

    // Array to store the generated random numbers
    double *random_numbers = (double*)malloc(n * sizeof(double));

    // Generate random numbers using the exponential function
    for (i = 0; i < n; i++) {
        random_numbers[i] = exponential(lambda);
    }

    // Print the generated random numbers
    printf("Generated random numbers:\n");
    for (i = 0; i < n; i++) {
        printf("%lf\n", random_numbers[i]);
    }

    // Free memory
    free(random_numbers);

    return 0;
}
