#ifndef SLIDE_H
#define SLIDE_H
#define SLIDE_LEFT 0
#define SLIDE_RIGHT 1

#include <stddef.h>
#include <stdio.h>

int slide_line(int *line, size_t size, int direction);

#endif