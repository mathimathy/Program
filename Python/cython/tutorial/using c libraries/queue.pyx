# distutils: sources = c-algorithms-master/src/queue.c
# distutils: include_dirs = c-algorithms-master/src/

cimport cqueue

cdef class Queue:
    cdef cqueue.Queue* _c_queue

    def __cinit__(self):
        self._c_queue = cqueue.queue_new()
        if self._c_queue is NULL:
            raise MemoryError()
        
    def __dealloc__(self):
        if self._c_queue is not NULL:
            cqueue.queue_free(self._c_queue)
    
    cpdef append(self, int value):
        if not cqueue.queue_push_tail(self._c_queue, <void*>value):
            raise MemoryError()
    
    cpdef extend(self, values):
        for value in values:
            self.append(value)

    cdef extend_ints(self, int* values, size_t count):
        cdef int value
        for value in values[:count]:
            self.append(value)
    
    cpdef int peek(self) except? -1:
        cdef int value = <Py_ssize_t>cqueue.queue_peak_head(self._c_queue)
        if value == 0:
            if cqueue.queue_is_empty(self._c_queue):
                raise IndexError("Queue is empty")
        return value
    
    cpdef int pop(self) except? -1:
        if cqueue.queue_is_empty(self._c_queue):
            raise IndexError("Queue is empty")
        return <Py_ssize_t>cqueue.queue_pop_head(self._c_queue)
    
    def __bool__(self):
        return not cqueue.queue_is_empty(self._c_queue)