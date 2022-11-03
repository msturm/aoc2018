public class Node {
    private Node prev;
    private Node next;
    private int value;

    public Node(Node prev, Node next, int value) {
        this.prev = prev;
        this.next = next;
        this.value = value;
    }

    public Node getPrev() {
        return prev;
    }

    public Node insertNode(int value) {
        Node newNode = new Node(this, getNext(), value);
        this.getNext().setPrev(newNode);
        this.setNext(newNode);
//        System.out.printf("%d %d %d%n", newNode.getPrev().getValue(), newNode.getValue(), newNode.getNext().getValue());
        return newNode;
    }

    public Node remove() {
        getPrev().setNext(this.getNext());
        getNext().setPrev(this.getPrev());
//        System.out.println("removing " + this.getValue() + " " + getPrev().getValue() + " " + getNext().getValue());
        return getNext();
    }

    public void setPrev(Node prev) {
        this.prev = prev;
    }

    public Node getNext() {
        return next;
    }

    public void setNext(Node next) {
        this.next = next;
    }

    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }
}
