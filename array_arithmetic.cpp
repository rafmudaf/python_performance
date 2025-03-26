
#include <iostream>
#include <vector>
#include <time.h>


int main()
{

    std::cout << "Configuration" << std::endl;

    // Python float is 64 bit / 8 byte
    int ARRAY_SIZE = 1000 * 1000 * 5;
    // int ARRAY_SIZE =  5;
    std::cout << "- Size of data array: " << ARRAY_SIZE * 8 / (1000 * 1000) << "MB" << std::endl;

    int N = 10;
    std::cout << "- Number of iterations to average: " << N << std::endl;


    time_t t_start, t_end;
    double elapsed_time = 0.0;
    double average;

    {
        std::vector<double> array1(ARRAY_SIZE), array2(ARRAY_SIZE), buffer_array(ARRAY_SIZE);
        std::vector<int> index_map(ARRAY_SIZE);

        for(int i=0; i<ARRAY_SIZE; i++) {
            index_map[i] = rand()%ARRAY_SIZE;
        }

        for (int i=0; i<N; i++) {
            t_start = time(NULL);
            for (int j=0; j<ARRAY_SIZE; j++) {
                int index = index_map[j];
                buffer_array[j] = array1[index] * array2[index] + array1[index] * array2[index];
            }
            t_end = time(NULL);

            elapsed_time += difftime(t_end, t_start);
        }
        average = elapsed_time / N;
        std::cout << "Non-contiguous access, vectorization: " << elapsed_time << " " << average << std::endl;
    }


    {
        std::vector<double> array1(ARRAY_SIZE), array2(ARRAY_SIZE), buffer_array(ARRAY_SIZE);
        std::vector<int> index_map(ARRAY_SIZE);

        for(int i=0; i<ARRAY_SIZE; i++) {
            index_map[i] = i;
        }

        for (int i=0; i<N; i++) {
            t_start = time(NULL);
            for (int j=0; j<ARRAY_SIZE; j++) {
                int index = index_map[j];
                buffer_array[j] = array1[index] * array2[index] + array1[index] * array2[index];
            }
            t_end = time(NULL);

            elapsed_time += difftime(t_end, t_start);
        }
        average = elapsed_time / N;
        std::cout << "Contiguous access, vectorization: " << elapsed_time << " " << average << std::endl;
    }


    // {
    //     std::vector<double> array1(ARRAY_SIZE), array2(ARRAY_SIZE), buffer_array(ARRAY_SIZE);

    //     for (int i=0; i<N; i++) {
    //         t_start = time(NULL);
    //         buffer_array = array1 * array2 + array1 * array2;
    //         t_end = time(NULL);

    //         elapsed_time += difftime(t_end, t_start);
    //     }
    //     average = elapsed_time / N;
    //     std::cout << "No indexing: " << elapsed_time << " " << average << std::endl;
    // }

    return 0;
}
