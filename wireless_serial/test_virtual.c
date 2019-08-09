#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>

int main()
{
    int fd = posix_openpt(O_RDWR | O_NOCTTY);
    printf("%s\n", ptsname(fd));
    /* ... read and write to fd ... */
    return 0;
}