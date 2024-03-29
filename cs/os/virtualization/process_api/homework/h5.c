#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main(int argc, char *argv[]) {
    int rc = fork();

    if(rc < 0) {
        fprintf(stderr, "fork failed\n");
        exit(1);
    } else if(rc == 0) {
        int rc_wait = wait(NULL);

        printf("child (rc_wait:%d) (pid:%d)\n", rc_wait, (int)getpid());
    } else {
        int rc_wait = wait(NULL);

        printf("parent of %d (rc_wait:%d) (pid:%d)\n", rc, rc_wait, (int)getpid());
    }

    return 0;
}