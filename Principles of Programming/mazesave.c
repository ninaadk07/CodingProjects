
#include "graphics.h"
#include <stdio.h>
#include <stdlib.h>
#define Size 83;

const int Sizeofgrid = 30;
const int Sizeofrobot = 10;
int xfinalpoint, yfinalpoint;
int top = -1;
int celltocheckx, celltochecky;
int moveFwdCheck;
int dfs_stack[83], visited_stack[83];
int deadend = 3;


int maze[11][11]={{1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1},
                  {0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1},
                  {1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1},
                  {1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1},
                  {1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1},
                  {1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1},
                  {1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1},
                  {1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1},
                  {1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1},
                  {1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1},
                  {1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1}};





struct robot
{
    int robotX[3];
    int robotY[3];
    char Directionrb;
};



int atMarker(struct robot *r1, int x, int y)
{
    int x1 = (*r1).robotX[1];
    int y1 = (*r1).robotY[1];
    int markerboolean;

    int xCell = ((x1 - 50) / 30);
    int yCell = ((y1 - 50) / 30);


    if ((xCell == 9) && (yCell ==10)){
        markerboolean = 1;
    }
    else
    {
        markerboolean = 0;
    }
    return markerboolean;

}
void dfspush(int x){
    if (top==(82)){
        printf("Stack overflow error");
    }
    else {
        top = top + 1;
        dfs_stack[top] = x;

    }
}

void visitedpush(int x){
    if (top==(82)){
        printf("Stack overflow error");
    }
    else {
        top = top + 1;
        visited_stack[top] = x;

    }
}


void dfspop(){
    if (top == -1){
        printf("Stack underflow error");
    }
    else{
        top = top - 1;
    }
}

int isInStack(int x){
    int stackcheck = 0;
    for (int i = top; i>=0; i --){
        if (x == dfs_stack[i]){
            stackcheck = 1;
        }
    }
    return stackcheck;
}
int isVisited(int x){
    int stackcheck = 0;
    for (int i = top; i>=0; i --){
        if (x == visited_stack[i]){
            stackcheck = 1;
        }
    }
    return stackcheck;
}

int canMoveForward(struct robot *r1)
{
    char Dir = (*r1).Directionrb;
    int x = (*r1).robotX[1];
    int y = (*r1).robotY[1];

    int xCell = ((x - 50) / 30);
    int yCell = ((y - 50) / 30);

    int check;

    if (Dir == 'e'){celltochecky = yCell; celltocheckx = xCell + 1;   }
    if (Dir == 'n'){ celltochecky = yCell - 1; celltocheckx = xCell;  }
    if (Dir == 's'){  celltochecky = yCell + 1; celltocheckx = xCell; }
    if (Dir == 'w'){  celltochecky = yCell ; celltocheckx = xCell - 1;}

    if (maze[celltochecky][celltocheckx] == 1)
    {
        moveFwdCheck = 0;
    }
    else
    {
        moveFwdCheck = 1;

    }


    return moveFwdCheck;
}

void drawRobot(struct robot *r1)
{
    foreground();
    foreground();
    setColour(pink);

    drawPolygon(3, (*r1).robotX, (*r1).robotY);
    fillPolygon(3, (*r1).robotX, (*r1).robotY);
    
   
}

void drawMaze(struct robot *r1)
{
    background();
    int x = 50;
    int y = 50;

    for (int i = 0; i < 11; i++)
    {
        for (int j = 0; j < 11; j++)
        {
            if (maze[i][j] == 1)
            {
                drawRect(x, y, Sizeofgrid, Sizeofgrid);
                setColour(black);
                fillRect(x, y, Sizeofgrid, Sizeofgrid);
            }
            else if (maze[i][j] == 0)
            {
                setColour(black);
                drawRect(x, y, Sizeofgrid, Sizeofgrid);
            }
            else if (maze[i][j] == 2)
            {
                setColour(gray);
                drawRect(x, y, Sizeofgrid, Sizeofgrid);
                fillRect(x, y, Sizeofgrid, Sizeofgrid);
            }
            x += Sizeofgrid;
        }
        x = 50;
        y += Sizeofgrid;
    }

    for (int p = 0; p < 11; p++)
    {
        for (int q = 0; q < 11; q++)
        {
            if (maze[p][q] == 2)
            {

                xfinalpoint = p + 1;
                yfinalpoint = q + 1;
            }
        }
    }

}

void moveForward(struct robot *r1)
{
    foreground();
    clear();

    if ((*r1).Directionrb == 'e')
    {

        for (int a = 0; a < 3; a++)
        {
            (*r1).robotX[a] += 30;
        }
        drawRobot(r1);
    }
    else if ((*r1).Directionrb == 's')
    {

        for (int a = 0; a < 3; a++)
        {
            (*r1).robotY[a] += 30;
        }
        drawRobot(r1);
    }
    else if ((*r1).Directionrb == 'w')
    {

        for (int a = 0; a < 3; a++)
        {
            (*r1).robotX[a] -= 30;
        }
        drawRobot(r1);
    }
    else if ((*r1).Directionrb == 'n')
    {

        for (int a = 0; a < 3; a++)
        {
            (*r1).robotY[a] -= 30;
        }
        drawRobot(r1);
    }
}

void turnLeft(struct robot *r1)
{
    foreground();
    if ((*r1).Directionrb == 'e')
    {
        clear();
        int tempX[3], tempY[3];

        for (int i = 0; i < 3; i++)
        {
            tempX[i] = (*r1).robotX[i];
            tempY[i] = (*r1).robotY[i];
        }
        (*r1).Directionrb = 'n';
        (*r1).robotX[1] = (tempX[1] + 10);
        (*r1).robotY[2] = (tempY[2] + 10);
    }
    else if ((*r1).Directionrb == 'n')
    {
        clear();
        int tempX[3], tempY[3];

        for (int i = 0; i < 3; i++)
        {
            tempX[i] = (*r1).robotX[i];
            tempY[i] = (*r1).robotY[i];
        }
        (*r1).Directionrb = 'w';
        (*r1).robotY[0] = (tempY[0] - 10);
        (*r1).robotX[1] = (tempX[1] + 10);
    }
    else if ((*r1).Directionrb == 'w')
    {
        clear();
        int tempX[3], tempY[3];

        for (int i = 0; i < 3; i++)
        {
            tempX[i] = (*r1).robotX[i];
            tempY[i] = (*r1).robotY[i];
        }
        (*r1).Directionrb = 's';
        (*r1).robotY[0] = (tempY[0] - 10);
        (*r1).robotX[2] = (tempX[2] - 10);
    }
    else if ((*r1).Directionrb == 's')
    {
        clear();
        int tempX[3], tempY[3];

        for (int i = 0; i < 3; i++)
        {
            tempX[i] = (*r1).robotX[i];
            tempY[i] = (*r1).robotY[i];
        }
        
        (*r1).Directionrb = 'e';
        (*r1).robotY[0] = (tempY[0] + 20);
        (*r1).robotX[1] = (tempX[1] - 20);
        (*r1).robotY[2] = (tempY[2] - 10);
        (*r1).robotX[2] = (tempX[2] + 10);
       
     }

    drawRobot(r1);
}


void turnRight(struct robot *r1)
{
    foreground();
    if ((*r1).Directionrb == 'e')
    {
        clear();
        int tempX[3], tempY[3];

        for (int i = 0; i < 3; i++)
        {
            tempX[i] = (*r1).robotX[i];
            tempY[i] = (*r1).robotY[i];
        }
        (*r1).Directionrb = 's';

        (*r1).robotY[0] = (tempY[0] - 20);
        (*r1).robotX[1] = (tempX[1] + 20);
        (*r1).robotY[2] = (tempY[2] + 10);
        (*r1).robotX[2] = (tempX[2] - 10);
    }
    else if ((*r1).Directionrb == 's')
    {
        clear();
        int tempX[3], tempY[3];

        for (int i = 0; i < 3; i++)
        {
            tempX[i] = (*r1).robotX[i];
            tempY[i] = (*r1).robotY[i];
        }
        (*r1).Directionrb = 'w';
        (*r1).robotX[2] = (tempX[2] + 10);
        (*r1).robotY[0] = (tempY[0] + 10);
    }
    else if ((*r1).Directionrb == 'w')
    {
        clear();
        int tempX[3], tempY[3];

        for (int i = 0; i < 3; i++)
        {
            tempX[i] = (*r1).robotX[i];
            tempY[i] = (*r1).robotY[i];
        }
        (*r1).Directionrb = 'n';
        (*r1).robotY[0] = (tempY[0] + 10);
        (*r1).robotX[1] = (tempX[1] - 10);
    }
    else if ((*r1).Directionrb == 'n')
    {
        clear();
        int tempX[3], tempY[3];

        for (int i = 0; i < 3; i++)
        {
            tempX[i] = (*r1).robotX[i];
            tempY[i] = (*r1).robotY[i];
        }
        (*r1).Directionrb = 'e';
        (*r1).robotX[1] = (tempX[1] - 10);
        (*r1).robotY[2] = (tempY[2] - 10);
    }
    drawRobot(r1);
}


void basicsearch(struct robot *r1){
    int *basicsearch2 = malloc(10000);
    if (atMarker(r1, xfinalpoint, yfinalpoint) == 1){
        printf("Maze solved");
        free(basicsearch2);
    }
    else {
        while (canMoveForward(r1) == 1) {
            if (atMarker(r1, xfinalpoint, yfinalpoint) == 1) {
                printf("Maze solved");
                free(basicsearch2);
                break;
            }
            else {
                moveForward(r1);
                sleep(100);
                turnLeft(r1);

                if (canMoveForward(r1) == 1) {
                    basicsearch(r1);
                }
                turnRight(r1);
                sleep(100);
            }
        }
        turnRight(r1);
        if (canMoveForward(r1) == 1) {
            basicsearch(r1);
        }
        else {
            turnRight(r1);
            sleep(100);
            basicsearch(r1);
        }

    }
}

void hardcode(struct robot *r1){
        moveForward(r1);
        sleep(250);
        turnRight(r1);
        sleep(250);
        moveForward(r1);
        sleep(250);moveForward(r1);
        sleep(250);moveForward(r1);
        sleep(250);moveForward(r1);
        sleep(250);moveForward(r1);
        sleep(250);moveForward(r1);
        sleep(250);moveForward(r1);
        sleep(250);moveForward(r1);
        sleep(250);
        turnLeft(r1);
        sleep(250);
        moveForward(r1);
        sleep(250);moveForward(r1);
        sleep(250);
        turnLeft(r1);
        sleep(250);
        moveForward(r1);
        sleep(250);moveForward(r1);
        sleep(250);
        turnRight(r1);
        sleep(250);
        moveForward(r1);
        sleep(250);moveForward(r1);
        sleep(250);
        turnRight(r1);
        sleep(250);
        moveForward(r1);
        sleep(250);moveForward(r1);
        sleep(250);
        turnLeft(r1);
        sleep(250);
        moveForward(r1);
        sleep(250);moveForward(r1);
        sleep(250);moveForward(r1);
        sleep(250);moveForward(r1);
        sleep(250);
        turnRight(r1);
        sleep(250);
        moveForward(r1);
        sleep(250);
        printf("Maze solved");
        }

int encode_coords(int y, int x){
    int encodedans;
    encodedans = ((47 * y) + (89 * x));
    return encodedans;
}

int decode_coords(int e, int* decode_y, int* decode_x){
    int ansy, ansx;
    for (int i = 0; i < 11; i++){
        for (int j = 0; j < 11; j ++){
            if (((47 * i) + (89 * j))==e){
                ansy = i;
                ansx = j;
            }
        }
    }
    *decode_y = ansy;
    *decode_x = ansx;
}


void pushstartvalue(struct robot *r1){
    int startvalue_encoded;
    int x = (*r1).robotX[0];
    int y = (*r1).robotY[0];
    int xCell = ((x - 50) / 30);
    int yCell = ((y - 50) / 30);
    startvalue_encoded = encode_coords(yCell, xCell);
    dfspush(startvalue_encoded);
}

int celltocheckxfunc(char dir, int xCell){
    if (dir == 'e'){ celltocheckx = xCell + 1; }
    if (dir == 'n'){ celltocheckx = xCell; }
    if (dir == 's'){ celltocheckx = xCell; }
    if (dir == 'w'){ celltocheckx = xCell - 1; }

    return celltocheckx;
}

int celltocheckyfunc(char dir, int yCell){
    if (dir == 'e'){ celltochecky = yCell;}
    if (dir == 'n'){ celltochecky = yCell - 1;}
    if (dir == 's'){  celltochecky = yCell + 1;}
    if (dir == 'w'){  celltochecky = yCell;}

    return celltochecky;
}

int depthfirst(struct robot *r1){
    int nextvalue_encoded;
    int backtrackon = 0;
    int backtrackdir = ' ';
    deadend = 3;
    char robDir = (*r1).Directionrb; int x = (*r1).robotX[0]; int y = (*r1).robotY[0];
    int xCell = ((x - 50) / 30); int yCell = ((y - 50) / 30);
    celltocheckx = celltocheckxfunc(robDir, xCell);
    celltochecky = celltocheckyfunc(robDir, yCell);
    nextvalue_encoded = encode_coords(celltochecky, celltocheckx);
    int *dfs_stack2 = malloc(10000);
    if (atMarker(r1, xfinalpoint, yfinalpoint) == 1){
        printf("Maze solved");
        free(dfs_stack2);
        return 0;
    }
    else {
        char robDir = (*r1).Directionrb;
        int xC = (*r1).robotX[0];
        int y= (*r1).robotY[0];
        int xCell = ((x - 50) / 30);
        int yCell = ((y - 50) / 30);
        celltocheckx = celltocheckxfunc(robDir, xCell);
        celltochecky = celltocheckyfunc(robDir, yCell);
        nextvalue_encoded = encode_coords(celltochecky, celltocheckx);
        if ((canMoveForward(r1) == 1) && (isInStack(nextvalue_encoded) == 0)&&(isVisited(nextvalue_encoded)==0)){
            dfspush(nextvalue_encoded);
            moveForward(r1);

            sleep(250);

            depthfirst(r1);
        }
        else{
            turnLeft(r1);
            char robDir = (*r1).Directionrb;
            int x = (*r1).robotX[0];
            int y = (*r1).robotY[0];
            int xCell = ((x - 50) / 30);
            int yCell = ((y - 50) / 30);
            celltocheckx = celltocheckxfunc(robDir, xCell);
            celltochecky = celltocheckyfunc(robDir, yCell);
            nextvalue_encoded = encode_coords(celltochecky, celltocheckx);
            sleep(250);
            if ((canMoveForward(r1) == 1) && (isInStack(nextvalue_encoded) == 0)&&(isVisited(nextvalue_encoded)==0)) {
                dfspush(nextvalue_encoded);
                visitedpush(nextvalue_encoded);
                moveForward(r1);
                sleep(250);

                depthfirst(r1);
            }
            else{
                turnRight(r1);
                turnRight(r1);
                sleep(250);
                char robDir = (*r1).Directionrb; int x = (*r1).robotX[0]; int y = (*r1).robotY[0];
                int xCell = ((x - 50) / 30); int yCell = ((y - 50) / 30);
                celltocheckx = celltocheckxfunc(robDir, xCell); celltochecky = celltocheckyfunc(robDir, yCell);
                nextvalue_encoded = encode_coords(celltochecky, celltocheckx);int currentvalue_encoded = encode_coords(yCell, xCell);
                if ((canMoveForward(r1) == 1) && (isInStack(nextvalue_encoded) == 0)&&(isVisited(nextvalue_encoded)==0)) {
                    nextvalue_encoded = encode_coords(celltochecky, celltocheckx);
                    visitedpush(nextvalue_encoded);
                    dfspush(nextvalue_encoded);

                    moveForward(r1);

                    sleep(250);

                    depthfirst(r1);
                }
                else {



                    turnRight(r1);
                    backtrackon = 1;
                    sleep(150);
                    while (backtrackon == 1) {

                        if (atMarker(r1, xfinalpoint, yfinalpoint) == 1) {
                            printf("Maze solved");
                            free(dfs_stack2);
                            return 0;
                            break;
                        } else {
                            char backtrackdir;
                            int nextvalue_encoded, currentvalue_encoded;
                            char robDir = (*r1).Directionrb; int x = (*r1).robotX[0]; int y = (*r1).robotY[0];
                            int xCell = ((x - 50) / 30); int yCell = ((y - 50) / 30);
                            celltocheckx = celltocheckxfunc(robDir, xCell); celltochecky = celltocheckyfunc(robDir, yCell);
                            currentvalue_encoded = encode_coords(yCell, xCell); nextvalue_encoded = encode_coords(celltochecky, celltocheckx);
                            printf("\nElements present in the stack: \n");
                            int tst = 0;
                            for (int i = top; i >= 0; --i) {
                                printf("%d , ", dfs_stack[i]);
                                tst = tst + 1;
                            }
                            printf("\n");
                            if (canMoveForward(r1) == 1) {
                                if ((isInStack(nextvalue_encoded) == 0)&&(isVisited(nextvalue_encoded)==0)) {
                                    backtrackon = 0;
                                    sleep(250);
                                    backtrackdir = ' ';
                                    depthfirst(r1);
                                } else {
                                    backtrackdir = 'f';
                                }
                            }
                            turnLeft(r1);
                            sleep(250);
                            robDir = (*r1).Directionrb; x = (*r1).robotX[0]; y = (*r1).robotY[0];
                            xCell = ((x - 50) / 30); yCell = ((y - 50) / 30);
                            celltocheckx = celltocheckxfunc(robDir, xCell); celltochecky = celltocheckyfunc(robDir, yCell);
                            nextvalue_encoded = encode_coords(celltochecky, celltocheckx);
                            if (canMoveForward(r1) == 1) {
                                if ((isInStack(nextvalue_encoded) == 0)&&(isVisited(nextvalue_encoded)==0)) {
                                    backtrackon = 0;
                                    depthfirst(r1);
                                    backtrackdir = ' ';

                                } else {
                                    backtrackdir = 'l';
                                }
                            }
                            turnRight(r1);
                            turnRight(r1);
                            sleep(250);
                            robDir = (*r1).Directionrb; x = (*r1).robotX[0]; y = (*r1).robotY[0];
                            xCell = ((x - 50) / 30); yCell = ((y - 50) / 30);
                            celltocheckx = celltocheckxfunc(robDir, xCell); celltochecky = celltocheckyfunc(robDir, yCell);
                            nextvalue_encoded = encode_coords(celltochecky, celltocheckx);
                            if (canMoveForward(r1) == 1) {
                                if ((isInStack(nextvalue_encoded) == 0)&&(isVisited(nextvalue_encoded)==0)) {
                                    backtrackon = 0;
                                    depthfirst(r1);
                                    backtrackdir = ' ';
                                } else {

                                    backtrackdir = 'r';
                                }
                            }
                            if (backtrackdir == 'r') {
                                sleep(250);
                                moveForward(r1);
                                dfspop();
                               
                                sleep(250);
                                continue;
                            } else if (backtrackdir == 'l') {
                                turnLeft(r1);
                                turnLeft(r1);
                                sleep(250);
                                moveForward(r1);
                                dfspop();
                             
                                sleep(250);
                                sleep(250);

                                continue;

                            } else if (backtrackdir == 'f') {
                                turnLeft(r1);
                                sleep(250);
                                moveForward(r1);
                                dfspop();
                                
                                sleep(250);
                                continue;
                            }
                        }
                    }
                }
            }

        }

    }
}






int main(void)
{
    setWindowSize(500, 500);

    
    struct robot r1 = {{55, 55, 75}, {105, 85, 95}, 'e'};
    
    drawMaze(&r1);
    drawRobot(&r1);
    //basicsearch(&r1); <- for the basic search algorithm (stage 3)
    pushstartvalue(&r1); // <- pushes the first value into the stack to start depth first search
    depthfirst(&r1); // <- for the depth first search algorithm (stage 5)
    //hardcode(&r1); <- for the hardcoded algorithm to test mobility



}
