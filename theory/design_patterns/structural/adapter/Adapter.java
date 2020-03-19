public class Adapter implements Target {
    private Adaptee adaptee;

    public Adapter(Adaptee a) {
        this.adaptee = a;
    }

    @Override
    public void request() {
        this.adaptee.specificRequest();
    }
}
