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
        printf("child (pid:%d) : hello\n", (int)getpid());
    } else {
        int rc_wait = wait(NULL);

        // with wait
        printf("parent %d (rc_wait:%d) (pid:%d) : goodbye\n", rc, rc_wait, (int)getpid());

        // without wait
        // printf("parent %d (pid:%d) : goodbye\n", rc, (int)getpid());
    }

    return 0;
}