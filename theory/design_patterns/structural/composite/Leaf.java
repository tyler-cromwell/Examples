public class Leaf implements Component {
    @Override
    public void add(Component c) {}

    @Override
    public void remove(Component c) {}

    @Override
    public void operation() {
        System.out.println("I'm doing stuff");
    }
}
