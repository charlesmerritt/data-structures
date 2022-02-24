/**
 * A queue represents a FIFO collection of strings.
 * FIFO just means that items are always added (enqueued) and removed
 * (dequeued) from opposite ends. Items are added to the back and removed
 * from the front. Implementing classes are expected
 * to have a default constructor that results in an empty queue.
 */
public interface Queue {

    /**
     * Returns the number of items currently in the queue.
     * @return the number of items currently in the queue.
     */
    int size();

    /**
     * Adds {@code item} to the back of this queue, and
     * increases the size of this queu by one.
     * @param item the item to be added to this queue.
     */
    void enqueue(String item);

    /**
     * Removes and returns the last object from the front of this queue,
     * and decreases the size of this queue by one. The returned item
     * should always be the oldest one in the queue.
     * @return the itm at the front of this queue.
     * @throws NoSuchElementException when this queue is empty.
     */
    String dequeue();

    /**
     * Returns the item at the front of this queue without removing it
     * from the queue. The returned item should always be the oldest one
     * in the queue.
     * @return the item at the front of this queue.
     * @throws NoSuchElementException when this queue is empty.
     */
    String peek();

}
