cdef extern from "c-algorithms-master/src/queue.h":
    ctypedef struct Queue:
        pass
    ctypedef void* QueueValue

    Queue* queue_new()
    void queue_free(Queue* queue)

    int queue_push_head(Queue* queue, QueueValue data)
    QueueValue queue_pop_head(Queue* queue)
    QueueValue queue_peak_head(Queue* queue)
    
    int queue_push_tail(Queue* queue, QueueValue data)
    QueueValue queue_pop_tail(Queue* queue)
    QueueValue queue_peak_tail(Queue* queue)

    bint queue_is_empty(Queue* queue)