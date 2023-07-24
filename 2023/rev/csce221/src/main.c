#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <main.h>

typedef unsigned char byte;

void list_init(struct list *list, byte *data, int len){
    struct listnode *head = malloc(sizeof(struct listnode));
    head->data = data[0];
    head->ptr = NULL;
    struct listnode *ptr = head;
    for(int i = 1; i < len; i++){
        ptr->ptr = malloc(sizeof(struct listnode));
        ptr = ptr->ptr;
        ptr->data = data[i];
        ptr->ptr = NULL;
    }   
    list->head = head;
    list->len = len;
};


void list_mix(struct list *list){
    struct listnode *ptr_a = list->head;
    struct listnode *ptr_b = list->head->ptr;
    int len = list->len;

    for (int i = 1; i < len; i++){
        struct listnode *tmp = (struct listnode *)((long)ptr_a ^ (long)ptr_b->ptr);
        ptr_a = ptr_b;
        ptr_b = ptr_b->ptr;
        ptr_a->ptr = tmp;
    }
}

int main(int argc, char *argv[]){
    setbuf(stdout, NULL);
    if (argc != 2){
        printf("Usage: %s <string>\n", argv[0]);
        return 1;
    }

    byte *input = argv[1];
    int len = strlen(input);
    list_init(&list, input, len);
    list_mix(&list);
    
    return 0;
}
