#include <stdio.h>
#include <stdlib.h>
#include <getopt.h>

/*
 * Notes
 * -----
 * optarg: the parameter passed to the 'option'.
 * long_options.val: the value 'getopt_long' returns if the 'flag' member is NULL, or
 *                   the value loaded into the variable pointed to by 'flag'.
 * long optional arguments must use '=' to specify values.
 * short optional arguments must NOT have a space (' ') between option and its value.
 */

static int flag_verbose = 0;    // Flag set by ‘--verbose’


int main(int argc, char **argv) {
    int option_index = 0, option = 0;

    static struct option long_options[] = {
        {"verbose",     no_argument,        &flag_verbose,  1},     // Will trigger part of case 0, sets 'flag_verbose' to 1.
        {"none",        no_argument,        NULL,           'n'},   // -n for short, no argument needed.
        {"required",    required_argument,  NULL,           'r'},   // -r for short, argument required.
        {"optional",    optional_argument,  NULL,           'o'},   // -o for short, argument optional.
        {"no-short",    optional_argument,  NULL,           0},     // Will trigger all of case 0.
        {NULL,          0,                  NULL,           0}
    };

    while ((option = getopt_long(argc, argv, "nr:o::", long_options, &option_index)) != -1) {
        switch (option) {
            case 0:
                /*
                 * Long options only (no short options associated)
                 */

                // If this option set a flag, do nothing else now
                if (long_options[option_index].flag != NULL) {
                    break;
                }

                printf("option %s", long_options[option_index].name);

                if (optarg) {
                    printf(" with arg '%s'\n", optarg);
                } else {
                    puts("");
                }

                break;

            // Long name: --none
            case 'n':
                puts("option -n");
                break;

            // Long name: --required
            case 'r':
                printf("option -r with value '%s'\n", optarg);
                break;

            // Long name: --optional
            case 'o':
                printf("option -o");

                if (optarg) {
                    printf(" with value '%s'\n", optarg);
                } else {
                    puts("");
                }

                break;

            case '?':
                break;  // getopt_long already printed an error message

            default:
                abort();
        }
    }

    // Check flags
    if (flag_verbose) {
        puts("verbose flag is set");
    }

    // Print any remaining command line arguments (not options)
    if (optind < argc) {
        printf("non-option ARGV-elements: ");

        while (optind < argc) {
            printf("%s ", argv[optind++]);
        }

        putchar('\n');
    }

    return EXIT_SUCCESS;
}
