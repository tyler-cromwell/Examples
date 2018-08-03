#define _DEFAULT_SOURCE // alphasort

#include <dirent.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>


int filter(const struct dirent *entry) {
    return (entry->d_name[0] != '.') ? 1 : 0;   // Skip hidden files
}


// "d_name" is just the name, directories don't have a slash
char ** listdir(const char *dir, size_t *amount, int (*filter)(const struct dirent *), bool prepend) {
    // Test if dir exists
    if (access(dir, F_OK)) {
        if (amount != NULL) {
            amount = 0;
        }
        return NULL;
    }

    bool slash = false;
    size_t ldir = 0;
    size_t bufsiz = 1;
    char **list = NULL;
    struct dirent **entries = NULL;
    int n = scandir(dir, &entries, filter, alphasort); // Get all files

    // Allocate space for "dir" and '/'
    if (prepend) {
        ldir = strlen(dir);
        bufsiz += ldir;

        if (dir[ldir-1] != '/') {
            slash = true;
            bufsiz++;
        }
    }

    // Construct string array
    for (int i = 0; i < n; i++) {
        char *name = entries[i]->d_name;
        size_t lname = strlen(name);
        struct stat fstatus;

        bufsiz += lname;
        stat(name, &fstatus);

        // Allocate space for trailing '/'
        if (S_ISDIR(fstatus.st_mode)) {
            bufsiz++;
        }

        // Allocate entry
        list = realloc(list, ++(*amount) * sizeof(char*));
        list[i] = calloc(bufsiz, sizeof(char));

        if (prepend) {
            // Include value of "dir"
            strncpy(list[i], dir, ldir);
            if (slash) {
                strncat(list[i], "/", 1);
            }
            strncat(list[i], name, lname);
        } else {
            // Just file name
            strncpy(list[i], name, lname);
        }

        if (S_ISDIR(fstatus.st_mode)) {
            // Include trailing '/'
            strncat(list[i], "/", 1);
        }

        free(entries[i]);
    }

    free(entries);
    return list;
}


void freelistdir(char **list, size_t amount) {
    for (size_t i = 0; i < amount; i++) free(list[i]);
    free(list);
}


int main(int argc, char *argv[]) {
    if (argc == 1) {
        fprintf(stderr, "Need at least one argument.");
        return EXIT_FAILURE;
    }

    size_t amount = 0;
    char **list = listdir(argv[1], &amount, filter, true);
    printf("Amount: %lu\n", amount);

    for (size_t i = 0; i < amount; i++) {
        printf("%s\n", list[i]);
    }

    freelistdir(list, amount);
    return EXIT_SUCCESS;
}
