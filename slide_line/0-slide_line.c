#include "slide_line.h"



int slide_line(int *line, size_t size, int direction)
{
    int ctrl, i, end;
    int *temp = NULL;

    if (direction)
    {
        ctrl = 1;
        i = 0;
        end = (int)size + 1;
    }
    else
    {
        ctrl = -1;
        i = size - 1;
        end = -1;
    }

    for (; i != end; i += ctrl)
    {
        if (!line[i])
            continue;
        if (!temp)
        {
            temp = &(line[i]);
            continue;
        }
        if (line[i] == *temp)
        {
            line[i] += *temp;
            *temp = 0;
            temp = NULL;
        }
    }
    return 1;
}