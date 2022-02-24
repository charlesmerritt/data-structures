/**
 * A simple implementation of the Queue interface.
 */
public class SimpleQueue implements Queue {

    private String[] data;
    private int numItems;
    private static final int DEFAULT_CAPACITY = 50;

    /**
     * Constructs an empty stack.
     */
    public SimpleQueue() {
        data = new String[DEFAULT_CAPACITY];
        numItems = 0;
    } // OracleStack

    /** {@inheritDoc} */
    public int size() {
        return numItems;
    }

    /** {@inheritDoc} */
    public void enqueue(String item) {
        throw new UnsupportedOperationException("Method not implemented");
    }

    /** {@inheritDoc} */
    public String dequeue() {
        throw new UnsupportedOperationException("Method not implemented");
    }

    /** {@inheritDoc} */
    public String peek() {
        throw new UnsupportedOperationException("Method not implemented");
    }

    /** {@inheritDoc} */
    @Override
    public String toString() {
        throw new UnsupportedOperationException("Method not implemented");
    }
}
