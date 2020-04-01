public class Director {
    private Builder builder;

    public Director(Builder b) {
        this.builder = b;
    }

    public void constructProduct() {
        this.builder.buildProduct("ConcreteProduct", "A Director managed my construction");
    }

    public Product getResult() {
        return this.builder.getProduct();
    }
}
