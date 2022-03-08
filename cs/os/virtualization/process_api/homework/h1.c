#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
    printf("main process (pid:%d)\n", (int)getpid());

    int x = 100;

    printf("main process' X is... %d\n", x);

    int rc = fork();

    if(rc < 0) {
        fprintf(stderr, "fork failed\n");
        exit(1);
    } else if(rc == 0) {
        printf("child process (pid:%d)\n", (int)getpid());
        printf("child process' X is... %d\n", x);
        
        x = 200;
        printf("child process change X from 100 to 200\n");
    } else {
        printf("parent process of %d (pid:%d)\n", rc, (int)getpid());
        printf("parent process' X is... %d\n", x);
    }

    return 0;
}