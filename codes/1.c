#include <stdio.h>
#include <math.h>

void linespace(int start, int stop, int step, int* n_values, int* y_values, int num_values) {
    for (int i = 0; i < num_values; ++i) {
        n_values[i] = start + i * step;
        int sum = (n_values[i]+1) * (240+ (n_values[i]) *5) / 2;
        y_values[i] = sum;
    }  // Add this closing bracket
}

int main() {
    // Define the range and step size
    int start = 0;
    int stop = 9;
    int step = 1;

    // Calculate the number of values in the range
    int num_values = (stop - start) / step + 1;

    // Allocate arrays to store the generated values
    int n_values[num_values];
    int y_values[num_values];

    // Call the linespace function
    linespace(start, stop, step, n_values, y_values, num_values);

    // Save data to a file
    FILE* file = fopen("output.dat", "w");

    if (file != NULL) {
        for (int i = 0; i < num_values; ++i) {
            fprintf(file, "%d %d\n", n_values[i], y_values[i]);
        }

        fclose(file);
        printf("Data saved to 'output.dat'.\n");
    } else {
        printf("Error opening file for writing.\n");
    }

    return 0;
}

