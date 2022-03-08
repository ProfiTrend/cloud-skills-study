# 숙제

## 문제 1

### Problem

> `fork()`를 호출하는 프로그램을 작성하라. `fork()`를 호출하기 전에 메인 프로세스는 변수에 접근하고 (예, `x`) 변수에 값을 지정하라 (예, `100`). 자식 프로세스에서 그 변수의 값은 무엇인가? 부모와 자식이 변수 `x`를 변경한 후에 변수는 어떻게 변했는가?

### [Code](./h1.c)

```c
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
```

### Compile & Execute

```bash
gcc -o h1.o h1.c -Wall
```

### Result

```
main process (pid:614)
main process' X is... 100
parent process of 615 (pid:614)
parent process' X is... 100
child process (pid:615)
child process' X is... 100
child process change X from 100 to 200
```

### Conclusion

비결정성(nondeterminism)으로 인해 변수가 변했는지 확인하는 것은 어렵다.

## 문제 2

### Problem

> `open()` 시스템 콜을 사용하여 파일을 여는 프로그램을 작성하고 새 프로세스를 생성하기 위하여 `fork()`를 호출하라. 자식과 부모가 `open()`에 의해 반환된 파일 디스크립터에 접근할 수 있는가? 부모와 자식 프로세스가 동시에 파일에 쓰기 작업을 할 수 있는가?

### [Code](./h2.c)

```c
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
```

### Compile & Execute

```bash
gcc -o h2.o h2.c -Wall
./h2.o
cat h2.out
```

### Result
```
here is the parent process
here is the child process
```

### Conclusion

부모와 자식 모두 파일 디스크립터에 접근할 수 있고, 동시에 파일 쓰기 작업이 가능하다.

## 문제 3

### Problem

> `fork()`를 사용하는 다른 프로그램을 작성하라. 자식 프로세스는 "hello"를 출력하고 부모 프로세스는 "goodbye"를 출력해야 한다. 항상 자식 프로세스가 먼저 출력하게 하라. 부모가 `wait()`를 호출하지 않고 할 수 있는가?

### [Code](./h3.c)

```c
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
```

### Compile & Execution

```bash
gcc -o h3.o h3.c -Wall
./h3.o
```

### Result

```
child (pid:2213) : hello
parent 2213 (pid:2212) : goodbye
```

### Conclusion

비결정성으로 인해 부모가 `wait()`를 호출하지 않고서는 항상 자식 프로세스가 먼저 출력된다는 보장이 없다.

단, 부모가 `wait()`를 호출하면 반드시 자식 프로세스가 먼저 실행된다.

## 문제 4

### Problem

> `fork()`를 호출하고 `/bin/ls`를 실행하기 위하여 `exec()` 계열의 함수를 호출하는 프로그램을 작성하라. `exec()`의 변형 `execl()`, `execle()`, `execlp()`, `execv()`, `execvp()`, `execve()` 모두를 사용할 수 있는지 시도해 보라. 기본적으로는 동일한 기능을 수행하는 시스템 콜에 여러 변형이 있는 이유를 생각해 보라.

### [Code](./h4.c)

```c
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
```

### Compile & Execute

```bash
gcc -o h4.o h4.c -Wall
```

### Result(execl)

```
execl
```

### Conclusion

`exec()`의 변형 모두를 사용할 수 있다. 단, 새로운 프로세스를 생성하는 것이 아니기 때문에 뒤에 있는 콜들은 리턴하지 않는다.

`exec()`의 변형들에 대한 설명은 다음과 같다.

- l : char* 타입의 argv 인자를 넘겨줄 때 사용한다.
- v : char*[] 타입의 argv 인자를 넘겨줄 때 사용한다.
- e : 환경변수를 넘겨줄 때 사용한다.
- p : 환경변수 PATH를 참조한다. 절대경로를 입력하지 않아도 된다.

## 문제 5

### Problem

> `wait()`를 사용하여 자식 프로세스가 종료되기를 기다리는 프로그램을 작성하라. `wait()`가 반환하는 것은 무엇인가? 자식 프로세스가 `wait()`를 호출하면 어떤 결과가 발생하는가?

### [Code](./h5.c)

```c
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
```

### Compile & Execute

```bash
gcc -o h5.o h5.c -Wall
./h5.o
```

### Result

```
child (rc_wait:-1) (pid:2416)
parent of 2416 (rc_wait:2416) (pid:2415)
```

### Conclusion

`wait()` 호출 시 성공하면 PID, 실패하면 -1을 반환한다.

자식 프로세스가 `wait()`를 호출하면 자식의 자식 프로세스가 없기 때문에 -1을 반환한다.

## 문제 6

### Problem

> 위 문제에서 작성한 프로그램을 수정하여 `wait()` 대신에 `waitpid()`를 사용하라. 어떤 경우에 `waitpid()`를 사용하는 것이 좋은가?

### [Code](./h6.c)

```c
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
        int rc_wait = waitpid(rc, NULL, 0);
        
        printf("child (rc_wait:%d) (pid:%d)\n", rc_wait, (int)getpid());
    } else {
        int rc_wait = waitpid(rc, NULL, 0);

        printf("parent of %d (rc_wait:%d) (pid:%d)\n", rc, rc_wait, (int)getpid());
    }

    return 0;
}
```

### Compile & Execute

```bash
gcc -o h6.o h6.c -Wall
```

### Result

```
child (rc_wait:-1) (pid:2577)
parent of 2577 (rc_wait:2577) (pid:2576)
```

### Conclusion

`waitpid()`는 `wait()`보다 더 많은 옵션을 지정할 수 있다

또한, 기다릴 자식 프로세스에 대해 더 상세히 지정할 수 있다.

## 문제 7

### Problem

> 자식 프로세스를 생성하고 자식 프로세스가 표준 출력(STDOUT_FILENO)을 닫는 프로그램을 작성하라. 자식이 표준출력을 닫은 후에 출력을 위해 `printf()`를 호출하면 무슨 일이 생기는가?

### [Code](./h7.c)

```c
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
```

### Compile & Execute

```bash
gcc -o h7.o h7.c -Wall
```

### Result

```
call printf() on parent
```

### Conclusion

자식 프로세스가 표준 출력을 닫으면, 자식 프로세스에서는 `printf()`를 호출해도 아무일도 일어나지 않는다.

하지만, 부모 프로세스에서는 정상적으로 호출된다.

## 문제 8

### Problem

> 두 개의 자식 프로세스를 생성하고 `pipe()` 시스템 콜을 사용하여 한 자식의 표준 출력을 다른 자식의 입력으로 연결하는 프로그램을 작성해라.

### [Code](./h8.c)

```c
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
```

### Compile & Execute

```bash
gcc -o h8.o h8.c -Wall
./h8.o
```

### Result

Nothing.

### Conclusion

실패. `pipe()`를 호출하지 않고서는 두 프로세스 간 전달을 어떻게 짜야 할지 아직 이해가 덜 되었다.