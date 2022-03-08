#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/wait.h>

int main(int argc, char *argv[]) {
    printf("main process (pid:%d)\n", (int)getpid());

    int f_descripter = open("./h2.out", O_CREAT | O_WRONLY | O_TRUNC, S_IRWXU);

    int rc = fork();

    if(rc < 0) {
        fprintf(stderr, "fork failed\n");
        exit(1);
    } else if(rc == 0) {
        char text[] = "here is the child process\n";

        if(write(f_descripter, text, sizeof(text)) == -1) {
            fprintf(stderr, "write failed on child process\n");
        }
    } else {
        char text[] = "here is the parent process\n";

        if(write(f_descripter, text, sizeof(text)) == -1) {
            fprintf(stderr, "write failed on parent process\n");
        }
    }

    close(f_descripter);
    return 0;
}