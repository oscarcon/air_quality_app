#include <stdlib.h>
#include <stdint.h>
#include <stdio.h>

#include <errno.h>
#include <termios.h>
#include <unistd.h>
#include <pty.h>

int main(int argc, char *argv[]) {
	openpty();
	return 0;
}