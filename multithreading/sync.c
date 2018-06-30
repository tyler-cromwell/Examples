#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>

#include <pthread.h>

#define MAX         3       // Maximum sleep time
#define MIN         0       // Minimum sleep time
#define NTHREADS    10      // Number of threads to spawn

typedef struct {
    pthread_mutex_t mutex;  // Mutex for locking
    pthread_cond_t cond;    // Condition variable for signaling
    size_t *done;           // Queue of finished threads
    size_t di;              // Index into done
    char asleep;            // Sleep / wakeup flag for the main thread
} globals_t;

typedef struct {
    globals_t *globals;     // Pointer to global data
    size_t index;           // Thread index / id number
} thread_data_t;


void * thread_main(void *param) {
    // Get thread data
    thread_data_t *data = param;
    globals_t *g = data->globals;

    // Thread is now active
    pthread_mutex_lock(&g->mutex);
    printf("[%.4lu]: Spawned!\n", data->index);
    pthread_mutex_unlock(&g->mutex);

    // Pretend to do work
    sleep(rand() % (MAX + 1 - MIN) + MIN);

    // Thread has finished
    pthread_mutex_lock(&g->mutex);
    printf("[%.4lu]: Finished!\n", data->index);
    g->done[g->di] = data->index;
    g->di++;
    g->asleep = 0;
    pthread_mutex_unlock(&g->mutex);
    pthread_cond_signal(&g->cond);  // Wake up the main thread
    return NULL;
}


int main(void) {
    // Initialization
    size_t active = 0, spawned = 0, finished = 0;
    size_t ncpus = sysconf(_SC_NPROCESSORS_ONLN);   // Get the number of online CPUs
    globals_t globals = {0};
    pthread_t threads[NTHREADS] = {0};
    thread_data_t data[NTHREADS] = {0};
    globals.done = calloc(ncpus, sizeof(size_t));
    pthread_mutex_init(&globals.mutex, NULL);
    pthread_cond_init(&globals.cond, NULL);

    // For all necessary threads
    for (size_t t = 0; finished < NTHREADS;) {
        // Assign threads to all available CPUs
        pthread_mutex_lock(&globals.mutex);
        for (; active < ncpus && spawned < NTHREADS;) {
            // At least 1 CPU is available
            data[t].globals = &globals;
            data[t].index = t;

            // Attempt to spawn thread
            printf("[main]: Spawning thread %lu... ", t);
            if (pthread_create(&threads[t], NULL, thread_main, &data[t]) != 0) {
                // Failed spawn
                puts("FAILED!");
                fprintf(stderr, "pthread_create: could not create thread %lu: %s\n", t, strerror(errno));
                return EXIT_FAILURE;
            } else {
                // Successful spawn
                puts("done");
                spawned++;
                active++;
                t++;    // Move to next thread
            }
        }
        pthread_mutex_unlock(&globals.mutex);

        pthread_mutex_lock(&globals.mutex);
        puts("[main]: Waiting");
        pthread_cond_wait(&globals.cond, &globals.mutex);
        puts("[main]: Resuming");

        // Attempt to join all finished threads
        for (size_t i = 0; i < globals.di; i++) {
            printf("[main]: Joining thread %lu... ", globals.done[i]);
            if (pthread_join(threads[globals.done[i]], NULL) != 0) {
                // Failed join
                puts("FAILED!");
                fprintf(stderr, "pthread_join: could not join thread %lu: %s\n", i, strerror(errno));
                return EXIT_FAILURE;
            } else {
                // Successful join
                puts("done");
                finished++;
                active--;
            }
        }
        globals.di = 0;
        pthread_mutex_unlock(&globals.mutex);
    }

    // Cleanup
    free(globals.done);
    pthread_mutex_destroy(&globals.mutex);
    pthread_cond_destroy(&globals.cond);
    return EXIT_SUCCESS;
}
