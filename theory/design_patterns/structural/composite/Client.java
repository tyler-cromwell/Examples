public class Client {
    public static void main(String[] args) {
        Component top = new Composite();
        Component middle = new Composite();
        Leaf side = new Leaf();
        Leaf bottom = new Leaf();

        top.add(middle);
        top.add(side);
        middle.add(bottom);
        top.operation();
    }
}
