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
        char *execv_data[] = {"echo", "execv", 0};
        char *execvp_data[] = {"echo", "execvp", 0};
        char *execve_data[] = {"echo", "execve", 0};

        // execl("/bin/echo", "echo", "execl", 0);
        // execle("/bin/echo", "echo", "execle", 0);
        // execlp("echo", "echo", "execle", 0);
        // execv("/bin/echo", execv_data);
        // execvp("echo", execvp_data);
        // execve("/bin/echo", execve_data, 0);
    }

    return 0;
}