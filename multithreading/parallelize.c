#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>


typedef struct job job_t;
typedef struct session session_t;


typedef enum {
    DEAD = 0,
    ALIVE = 1,
    JOINED = 2
} state_t;


struct job {
    session_t *session;
    void * (*action)(void*);
    size_t id;
    state_t state;
};


struct session {
    pthread_mutex_t mutex;
    pthread_cond_t cond;
    job_t *jobs;
    size_t id;
    size_t njobs;
    size_t alive;
    size_t unjoined;
};


void * job_test(void *param) {
    job_t *job = param;
pthread_mutex_lock(&job->session->mutex);
    printf("[%lu]: I'm dead now\n", job->id);
    job->session->unjoined++;
    job->state = DEAD;
pthread_mutex_unlock(&job->session->mutex);
    pthread_cond_signal(&job->session->cond);   // Tell manager I'm done
    return NULL;
}


void parallelize(session_t *session) {
    // Allocate threading memory
    pthread_mutex_init(&session->mutex, NULL);
    pthread_cond_init(&session->cond, NULL);
    pthread_t *threads = calloc(session->njobs, sizeof(pthread_t));
    int *rets = calloc(session->njobs, sizeof(int));

    // Spawn all threads
    for (size_t t = 0; t < session->njobs; t++) {
        session->jobs[t].session = session;
        session->jobs[t].id = t;
        session->jobs[t].state = ALIVE;
        rets[t] = pthread_create(&threads[t], NULL, session->jobs[t].action, &session->jobs[t]);

        if (rets[t]) {
            fprintf(stderr, "pthread_create (%d): %s\n", rets[t], strerror(errno));
            exit(EXIT_FAILURE);
        }
    }

    session->alive = session->njobs;
    session->unjoined = 0;

    // Wait for threads to die
    while (session->alive > 0) {
pthread_mutex_lock(&session->mutex);

        while (session->unjoined == 0) {
            pthread_cond_wait(&session->cond, &session->mutex);
        }

        for (size_t i = 0; i < session->njobs; i++) {
            if (session->jobs[i].state == DEAD) {
                rets[i] = pthread_join(threads[i], NULL);

                if (rets[i]) {
                    fprintf(stderr, "pthread_join (%d): %s\n", rets[i], strerror(errno));
                    exit(EXIT_FAILURE);
                } else {
                    session->jobs[i].state = JOINED;
                    session->unjoined--;
                    session->alive--;
                }
            }
        }

pthread_mutex_unlock(&session->mutex);
    }

    // Cleanup
    pthread_mutex_destroy(&session->mutex);
    pthread_cond_destroy(&session->cond);
    free(threads);
    free(rets);
}


int main(int argc, char *argv[]) {
    if (argc == 1) {
        fprintf(stderr, "Need at least one argument.\n");
        return EXIT_FAILURE;
    }

    size_t njobs = atoi(argv[1]);
    job_t *jobs = calloc(njobs, sizeof(job_t));

    for (size_t i = 0; i < njobs; i++) {
        jobs[i].action = job_test;
    }

    session_t session;
    session.jobs = jobs;
    session.id = 0;
    session.njobs = njobs;

    parallelize(&session);

    free(jobs);
    return EXIT_SUCCESS;
}
