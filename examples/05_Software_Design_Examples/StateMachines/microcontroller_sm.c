#include <stdio.h>
#include "timing.h"

typedef enum State {
    ST_START,
    ST_STATE_A,
    ST_STATE_B,
    ST_STATE_EXIT
} State;

State state = ST_START;
int start_wait_b;

void main(){
    start_wait_b = get_time_ms();

    while(1){
        switch(state){
            case ST_START:
                printf("I'm in start state - Loading initial data\n");
                state = ST_STATE_A;
                break;
    
            case ST_STATE_A:
                printf("I'm in state A - Sending data somewhere\n");
                state = ST_STATE_B;
                start_wait_b = get_time_ms(); //Reset wait time for state B
                break;
    
            case ST_STATE_B:
                printf("I'm in state B - Waiting without blocking\n");
                if(get_time_ms() - start_wait_b > 30000){
                    state = ST_STATE_EXIT;
                    start_wait_b = get_time_ms();
                }
                break;

            case ST_STATE_EXIT:
                printf("I'm in exit state - exiting gracefully\n");
                state = ST_START;
                break;
        }
    }
}