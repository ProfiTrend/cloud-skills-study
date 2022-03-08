#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/wait.h>

int main(int argc, char *argv[]) {
    int first_rc = fork();
    int second_rc = fork();
    int f_description;
    int buf = 0;

    if(first_rc < 0) {
        fprintf(stderr, "fork failed\n");
        exit(1);
    } else if(first_rc == 0) {
        pipe(f_description);

        write(f_description, 1, sizeof(int));
        
        if(second_rc < 0) {
            fprintf(stderr, "fork failed\n");
            exit(1);
        } else if(second_rc == 0) {
            read(f_description, buf, sizeof(int));
            printf("%d", buf);
        } else {
            int rc_wait = wait(NULL);
        }
    } else {
        int rc_wait = wait(NULL);
    }

    return 0;
}