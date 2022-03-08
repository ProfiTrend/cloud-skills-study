#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/wait.h>

int main(int argc, char *argv[]) {
    int rc = fork();

    if(rc < 0) {
        fprintf(stderr, "fork failed\n");
        exit(1);
    } else if(rc == 0) {
        close(STDOUT_FILENO);

        printf("call printf() on child\n");
    } else {
        int rc_wait = wait(NULL);

        printf("call printf() on parent\n");
    }

    return 0;
}