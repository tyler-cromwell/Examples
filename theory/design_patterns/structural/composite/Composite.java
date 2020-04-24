import java.util.ArrayList;


public class Composite implements Component {
    private ArrayList<Component> components;

    public Composite() {
        this.components = new ArrayList<Component>();
    }

    @Override
    public void add(Component c) {
        this.components.add(c);
    }

    @Override
    public void remove(Component c) {
    }

    @Override
    public void operation() {
        for (Component c : this.components) {
            c.operation();
        }
    }
}
